from celery import Celery

from src.configs.config import CeleryConfig, SQSConfig, DatabaseConfig


class CeleryApp:
    client = None

    def __init__(self, config: CeleryConfig, queue_config: SQSConfig, db_config: DatabaseConfig):
        self.result_expires = config.result_expires
        self.result_extended = "name, args, kwargs, worker, retries, queue, delivery_info"
        self.task_annotations = {"*": {"max_retries": config.max_retry}}
        self.result_backend = "db+postgresql+psycopg2://{username}:{password}@{host}:{port}/{name}".format_map(
            db_config.dict()
        )

        # queue_url: https://sqs.<region>.amazonaws.com/<account_id>/<queue_name>
        queue_url = queue_config.celery_queue_url
        queue_name = queue_url[queue_url.rfind("/") + 1:]

        self.broker_url = "sqs://localstack:localstack@localhost:4566"

        # self.broker_url = "sqs://{access_key_id}:{secret_access_key}@".format(
        #     access_key_id=safequote(queue_config.access_key_id),
        #     secret_access_key=safequote(queue_config.secret_access_key),
        # )

        self.broker_transport_options = {
            "predefined_queues": {
                queue_name: {
                    "url": queue_url,
                    # "access_key_id": safequote(queue_config.access_key_id),
                    # "secret_access_key": safequote(queue_config.secret_access_key),
                }
            },
        }
        self.task_default_queue = queue_name

        self.client = Celery(config_source=self)
