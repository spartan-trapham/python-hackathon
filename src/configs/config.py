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
    workers: int
    log_level: str = Field(default="DEBUG", alias="logLevel")


class DatabaseConfig(BaseModel):
    name: str
    username: str
    password: str
    host: str
    port: int
    max_connections: int = Field(default=5)
    overflow_connections: int = Field(default=5)


class AWSConfig(BaseModel):
    access_key_id: str
    secret_access_key: str
    region: str


class SQSConfig(BaseModel):
    general_queue_url: str = Field(default="")
    celery_queue_url: str = Field(
        default="http://sqs.us-east-1.localhost.localstack.cloud:4566/000000000000/celery_task_queue")


class S3Config(BaseModel):
    url: str
    public_bucket_name: str
    private_bucket_name: str


class RedisConfig(BaseModel):
    hosts: str = Field(default="localhost")
    user: str = Field(default="")
    password: str = Field(default="")
    ssl: bool = Field(default=False)
    timeout: int = Field(default=5)
    port: int = Field(default=6379)


# Celery configuration
class Task(BaseModel):
    enabled: bool = Field()
    task: str = Field()


class CrontabConfig(Task):
    minute: int = Field()
    hour: int = Field(default=None)
    day_of_week: int = Field(default=None)
    day_of_month: int = Field(default=None)
    month_of_year: int = Field(default=None)


class IntervalConfig(Task):
    seconds: int = Field()


class CrontabSchedulerConfigs(BaseModel):
    daily_service: CrontabConfig = Field()


class IntervalSchedulerConfigs(BaseModel):
    interval_service: IntervalConfig = Field()


class SchedulerConfigs(BaseModel):
    crontab: CrontabSchedulerConfigs = Field(default=None)
    interval: IntervalSchedulerConfigs = Field(default=None)


class CeleryConfig(BaseModel):
    result_expires: int = Field(default=0)
    max_retry: int = Field(default=3)
    schedulers: SchedulerConfigs = Field()


class Config(BaseModel):
    app: AppConfig
    database: DatabaseConfig
    # aws: AWSConfig
    sqs: SQSConfig
    # s3: S3Config
    # redis: RedisConfig
    celery: CeleryConfig


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
            database=DatabaseConfig(**config['database']),
            # aws=AWSConfig(**config['aws']),
            sqs=SQSConfig(**config['sqs']),
            # s3=S3Config(**config['s3']),
            # redis=RedisConfig(**config['redis'])
            celery=CeleryConfig(**config['celery']),
        )
        return config_obj

    def get_config(self):
        return self.config
