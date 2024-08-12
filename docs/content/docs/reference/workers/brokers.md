+++
weight = 3601
date = "2023-05-03T22:37:22+01:00"
draft = false
author = "Pham Xuan Tra"
title = "Brokers"
icon = "rocket_launch"
toc = true
description = "Dispatcher routing messages to workers or processors"
publishdate = "2023-05-03T22:37:22+01:00"
tags = ["intermediate"]
+++

Brokers are the ones who listen to the queue events then query message and dispatch to the processors based on matching route between message and processors. Those process are almost supported by [Celery](https://docs.celeryq.dev/en/main/index.html).

#### Define a message broker

The broker is defined in the Container so that it can be called by services to send requests as messages to the queues
```python
class ServiceContainer(containers.DeclarativeContainer):
    configuration = providers.Singleton(Configuration().get_config)

    # Background Tasks
    critical = providers.Singleton(Celery, broker=configuration.provided.celery.critical.broker_url, backend=configuration.provided.celery.critical.backend_url)
    scheduler = providers.Singleton(Celery, broker=configuration.provided.celery.scheduler.broker_url, backend=configuration.provided.celery.scheduler.backend_url)
    internal = providers.Singleton(Celery)
```
Broker URL is the URL to the message queue. It can be different between `redis`, `rabitmq`, `sqs`. The backend is the data store where status of a tasks will be saved. If both `broker` and `backend` is not available, `internal`, the broker is simply push a function into background of the API server. No distribution needed.

#### Define task processors

```python
container = ServiceContainer()
scheduler: Celery = container.scheduler()

@scheduler.task(name='scheduler.notificationtask_fire_notification')
def notificationtask_fire_notification(user_ids: list[uuid.UUID]):
    notification_service = container.notif_service()
    return notification_service.send_notification(user_ids)
```
The processor is managed by `Celery` instance. It may work in different servers from the API server. The container in this file should not be imported into API routes/handlers

#### Trigger task from API
```python
from src.containers.service_container import ServiceContainer

@router.get('/send-email/{user_id}', response_model=uuid.UUID)
@inject
async def get(request: Request, user_id: uuid.UUID, scheduler: Celery = Depends(Provide[ServiceContainer.scheduler])):
    task = scheduler.send_task('scheduler.usertask_send_email', args=[[user_id]])
    return task.id
```

Please note that the `scheduler: Celery` from `container` is not the `scheduler: Celery` in the processors. It main features here is sending a message to the broker URL as configured in the container.