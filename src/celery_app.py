# import logging
#
# from celery import signals
#
# from src.containers.container import Container
# from src.libs.log import logging
#
# app = Container.celery().client
#
#
# # pylint: disable=unused-argument
# @signals.after_setup_task_logger.connect
# def setup_logger(**kwargs):
#     logging.setup_logger(__name__)
#
#
# app.autodiscover_tasks(
#     [
#         "src.worker.brokers.critical",
#         "src.worker.brokers.internal",
#         "src.worker.brokers.scheduler",
#     ]
# )
