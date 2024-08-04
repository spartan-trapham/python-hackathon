from abc import ABC

import celery

from ...core import logging

logger = logging.setup_logger(__name__)


class BaseTask(celery.Task, ABC):
    retry_backoff = True

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        logger.error(f"Task {task_id} failed: {exc}")
        super().on_failure(exc, task_id, args, kwargs, einfo)
