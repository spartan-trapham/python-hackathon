+++
weight = 2000
date = "2023-05-03T22:37:22+01:00"
draft = true
author = "Pham Xuan Tra"
title = "Introduction"
icon = "rocket_launch"
toc = true
description = "Brief introduction about python project structure"
publishdate = "2023-05-03T22:37:22+01:00"
tags = ["Beginners"]
+++

## Requirements

- Python v3.11
- Poetry, FastAPI, SQLAlchemy, Celery
- PostgreSQL, Redis

## Getting started

Please check the [document](docs/getting-started) to run the project with poetry and celery.

## Project structure

The project contains some main features to build up a generic api-server:

- [APIs](#api-gateway)
- [services](#services)
- [libraries](#libraries)
- [databases](#database)
- [workers](#workers)

and [some other utilities](#common-utilities-and-helpers). All of them are managed by [Dependency-Injector](https://python-dependency-injector.ets-labs.org/)

![Project Structure](images/project-structure.png)

The project contains 2 separate application instances: API server powered by [FastAPI](https://fastapi.tiangolo.com/) and worker servers powered by [Celery](https://docs.celeryq.dev/en/stable/)

```
src
├── api
│   ├── controllers
│   │   ├── admin
│   │   ├── client
│   │   └── superadmin
│   ├── middlewares
│   └── validators
├── libs
│   ├── log
│   ├── redis
│   ├── s3
│   └── sqs
├── services
│   ├── roles
│   └── users
├── worker
│   ├── brokers
│   └── tasks
├── database
│   ├── migrations
│   ├── models
│   └── repositories
├── utils
├── common
├── entities
└── helpers
```
### API gateway
`API` includes components building routers for HTTP server: `controllers` (aka handlers), `middlewares`, `validators`

#### [Controllers / handlers](/docs/reference/api/controller)
`controllers` (aka handlers) is designed following role-based architect in order to group endpoints following user types. It will reduce the cost greatly for long-term maintenance and development. Almost user and system requirements are separated between users/clients. Developers and QA can break down, develop, testing and deploy tasks easily without interference between users.

### Services
`services` the core logics to serve the business live here. Please build the services directory with specific architectures with clear descriptions so that developers can manage all logic, testing and documentations correctly following bussiness requirements changed.

DI pattern helps this part to be well-tested and easily for refactoring other parts to achieve better quality.

### Database
`models` contains description of database tables and common queries/mutations for that table. Don't try to import any other entities unless they are relations. We will do complex query in repositories for particular services. [Read more](docs/content/docs/reference/database/models.md)

`migrations` is a collection of `SQL` scripts to form up the database structures and some initial data. This directory is followed [user guide of flyway](https://www.red-gate.com/hub/university/courses/flyway/getting-started-with-flyway/introduction-to-flyway/folder-structure-and-configuration-file). [Read more](docs/content/docs/reference/database/migrations.md)

### Workers
`workers` implement [Celery frameworks](https://docs.celeryq.dev/en/stable/index.html) to manage and distributed task queue. The structure would somehow similar with [API gateway](#api-gateway). `workers` contains 2 main parts: **brokers** and **tasks**

#### [Brokers](docs/content/docs/reference/workers/brokers.md)
`brokers` act as a dispatcher to get the message from the queue then deliver the message to the workers to run the tasks. Their roles are similar with API which routes requests to the controllers or handlers.
#### [Tasks](docs/content/docs/reference/workers/tasks.md)
`Tasks` is list of methods that workers can execute matched with message from the queue. In API, this part is similar with service that controllers will called to serve the requests.

### Libraries
`libs` contains configurations to use 3rd party libraries in the project. For example, `s3` has its own library but instead of using directly in the project, `libs/s3` will cover common functionalities like `init,deinit,upload,download` to form up the methods which are compatible with the project requriements

### Common utilities and helpers
- `common` includes common features like context extractor, error handler, error code. [Read more](docs/content/docs/reference/utilities/common.md)
- `helpers` contains some common functions for specific places. For example: transforming data structure between layers, building response message of a http request, wrap a message to conventional log message. [Read more](docs/content/docs/reference/utilities/helper.md)
- `utils` contains pure functions which are not depended on any other library to do specific logic for example: string transformation, rounding number, etc. [Read more](docs/content/docs/reference/utilities/utils.md)
