+++
weight = 3101
date = "2023-05-03T22:37:22+01:00"
draft = true
author = "Pham Xuan Tra"
title = "Controllers/Handlers"
icon = "rocket_launch"
toc = true
description = "Reference for detail API structure"
publishdate = "2023-05-03T22:37:22+01:00"
tags = ["intermediate"]
+++

`controllers` (aka handlers) are designed following role-based architect in order to group endpoints following user types. There are some type of clients accessing to the API servers:
- Super Admin (Operator)
- Administrator
- Client (Web/Mobile/App)
- Public
- Internal

Although some endpoints may have similar functionalities and can be grouped together following features/domains, they are different in terms of maintenance.
- **Super Admin** (Operator) requires highly security. The endpoints may live behind a VPN.
- **Administrator** requires security. The endpoints may requires verified signatures and can be shutdown immediately if they found unexpected accesses.
- **Client** (Web/Mobile/App) requires high availability. The endpoints need to be recovered as soon as possible after a disaster.
- **Public** (Web/Mobile/App) requires CDN with simple query to optimize SEO score.
- **Internal** requires network classification with internal identification for each clients.

With those properties, it will reduce the cost greatly for long-term maintenance and development if those endpoints are separated. Almost user and system requirements are separated between users/clients. Developers and QA can break down, develop, testing and deploy tasks easily without interference between users.

```python
import uuid

from celery import Celery
from dependency_injector.wiring import (
    inject,
    Provide,
)
from fastapi import APIRouter, Depends
from starlette.requests import Request

from src.containers.service_container import ServiceContainer
from src.libs.log import logging

router = APIRouter(prefix="/tasks")
logger = logging.setup_logger(__name__)


@router.get('/send-email/{user_id}', response_model=uuid.UUID)
@inject
async def get(request: Request, user_id: uuid.UUID, scheduler: Celery = Depends(Provide[ServiceContainer.scheduler])):
    logger.info(f"Execute send email task for user id {user_id}")
    task = scheduler.send_task('scheduler.usertask_send_email', args=[[user_id]])
    return task.id
```