import logging

from celery import signals

from src.containers.container import Container
from src.libs.log import logging

container = Container()
critical = container.critical()
internal = container.internal()
scheduler = container.scheduler()


# pylint: disable=unused-argument
@signals.after_setup_task_logger.connect
def setup_logger(**kwargs):
    logging.setup_logger(__name__)


critical.autodiscover_tasks(
    [
        "src.worker.brokers.critical",
    ]
)

internal.autodiscover_tasks(
    [
        "src.worker.brokers.internal",
    ]
)

scheduler.autodiscover_tasks(
    [
        "src.worker.brokers.scheduler",
    ]
)
