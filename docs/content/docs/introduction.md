+++
weight = 100
date = "2023-05-03T22:37:22+01:00"
draft = true
author = "Pham Xuan Tra"
title = "Introduction"
icon = "rocket_launch"
toc = true
description = "A quickstart guide to create new python project"
publishdate = "2023-05-03T22:37:22+01:00"
tags = ["Beginners"]
+++
## Project structure

```bash
src
├── api
│   ├── controllers
│   │   ├── admin
│   │   │   └── dtos
│   │   ├── client
│   │   │   └── dtos
│   │   └── superadmin
│   │       └── dtos
│   ├── middlewares
│   └── validators
├── common
├── entities
├── helpers
├── libs
│   ├── config
│   ├── db
│   ├── log
│   ├── redis
│   ├── s3
│   └── sqs
├── services
│   ├── roles
│   └── users
├── utils
└── worker
    └── processors
```

- `API` includes components building routers for HTTP server: `controllers` (aka handlers), `middlewares`, `validators`
  - `controllers` (aka handlers) is designed following role-based architect so that each group of endpoints will have the best security management.
- `worker` includes components building worker management for background tasks. The architecture of this directory is similar to `api` where it is connect to a message queue service to listen incomming message (request in http server). Each incomming message will be dispatched to workers via queue as a http server dispatches requests to controllers/handlers via routers.
- `common` includes common functions which can be used in various places. The function can import any packages. Please take care this directory. If it grows bigger than normal, the project is going to be a _ball of mud_
- `entities` contains description of database tables and common queries/mutations for that table. Don't try to import any other entities unless they are relations. We will do complex query in repositories of particular services.
- `helpers` contains some common functions for specific places. For example: transforming data structure between layers, building response message of a http request, wrap a message to conventional log message.
- `libs` contains configurations to use 3rd party libraries in the project. For example, `s3` has its own library but instead of using directly in the project, `libs/s3` will cover common functionalities like `init,deinit,upload,download` to form up the methods which are compatible with the project requriements
- `utils` contains pure functions which are not depended on any other library to do specific logic for example: string transformation, rounding number, etc
- `services` the core logics to serve the business live here. Please build the services directory with specific architectures with clear descriptions so that developers can manage all logic, testing and documentations correctly following bussiness requirements changed.
