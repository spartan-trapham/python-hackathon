import os
import re

import yaml
from pydantic import BaseModel, Field


class AppConfig(BaseModel):
    environment: str
    title: str
    description: str
    host: str
    port: int
    root_path: str
    workers: int
    log_level: str = Field(default="DEBUG", alias="logLevel")


class DatabaseConfig(BaseModel):
    url: str
    replica_enabled: bool = Field(..., alias="replicaEnabled")
    replica_url: str = Field(..., alias="replicaUrl")
    name: str
    username: str
    password: str
    prepare_threshold: int = Field(..., alias="prepareThreshold")
    replica_timeout_seconds: int = Field(..., alias="replicaTimeoutSeconds")
    primary_timeout_seconds: int = Field(..., alias="primaryTimeoutSeconds")
    port_number: int = Field(..., alias="portNumber")


class AWSConfig:
    access_key_id: str
    secret_access_key: str
    region: str


class SQSConfig:
    url: str
    general_queue_url: str


class S3Config:
    url: str
    public_bucket_name: str
    private_bucket_name: str


class RedisConfig:
    hosts: str
    user: str
    password: str
    ssl: bool
    timeout: int
    port: int


class Config(BaseModel):
    app: AppConfig
    databases: DatabaseConfig
    # aws: AWSConfig
    # sqs: SQSConfig
    # s3: S3Config
    # redis: RedisConfig


class Configuration:
    def __init__(self, config_path: str = '/config.yml'):
        self.config_path = config_path
        self.config = self.load_config()

    @staticmethod
    def substitute_env_vars(value):
        pattern = re.compile(r'\${(\w+):?(.*?)}')
        matches = pattern.findall(value)
        if not matches:
            return value

        for var, default in matches:
            env_value = os.getenv(var, default)
            value = value.replace(f'${{{var}:{default}}}', env_value)
        return value

    def parse_config(self, config):
        if isinstance(config, dict):
            return {k: self.parse_config(self.substitute_env_vars(v)) if isinstance(v, str) else self.parse_config(v)
                    for k, v in config.items()}
        elif isinstance(config, list):
            return [self.parse_config(self.substitute_env_vars(i)) if isinstance(i, str) else self.parse_config(i) for i
                    in config]
        else:
            return config

    def load_config(self):
        with open(os.path.dirname(__file__) + self.config_path, 'r') as file:
            config = yaml.safe_load(file)
        parsed_config = self.parse_config(config)
        return self.create_dataclass(parsed_config)

    def create_dataclass(self, config):
        config_obj = Config(
            app=AppConfig(**config['app']),
            databases=DatabaseConfig(**config['databases']),
            # aws=AWSConfig(**config['aws']),
            # sqs=SQSConfig(**config['sqs']),
            # s3=S3Config(**config['s3']),
            # redis=RedisConfig(**config['redis'])
        )
        return config_obj

    def get_config(self):
        return self.config
