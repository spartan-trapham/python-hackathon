+++
weight = 1000
date = "2023-05-03T22:37:22+01:00"
draft = false
author = "Pham Xuan Tra"
title = "Getting started"
icon = "rocket_launch"
toc = true
description = "A quickstart guide to run python template"
publishdate = "2023-05-03T22:37:22+01:00"
tags = ["Beginners"]
+++

## Requirements

- Python v3.12

## Setup

Step 1: Create venv

```shell
python -m venv .venv
```

Step 2: Activate venv

```shell
source .venv/bin/activate
```

Step 3: Install poetry

```shell
pip install --upgrade pip
pip install poetry
```

Step 4: Run poetry install

```shell
poetry install
```

## Development

```shell
export PYTHONPATH="$PWD"
python src/main.py 
```

If everything is set up correctly, you will get this
```shell
INFO:     Will watch for changes in these directories: ['<PROJ_DIR>/python-hackathon']
INFO:     Uvicorn running on http://127.0.0.1:8080 (Press CTRL+C to quit)
INFO:     Started reloader process [17442] using WatchFiles
INFO:     Started server process [17447]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

You can call `/api/health`, the message "Hello world" will be printed under object schema.

```
{"Hello":"World"}
```

## Start Celery worker

For distributed and micro-service architecture, worker services should be in separated processes. All workers are managed by Celery framework

```shell
celery -A src.workers.brokers.scheduler worker -l INFO
```

Console output:
```
 -------------- celery@MB-Pro---TraPham.local v5.4.0 (opalescent)
--- ***** ----- 
-- ******* ---- macOS-14.5-arm64-arm-64bit 2024-08-13 00:34:09
- *** --- * --- 
- ** ---------- [config]
- ** ---------- .> app:         __main__:0x1057d42d0
- ** ---------- .> transport:   redis://localhost:6379/0
- ** ---------- .> results:     disabled://
- *** --- * --- .> concurrency: 11 (prefork)
-- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
--- ***** ----- 
 -------------- [queues]
                .> celery           exchange=celery(direct) key=celery
                

[tasks]
  . scheduler.notificationtask_fire_notification
  . scheduler.s3task_clean_up
  . scheduler.usertask_send_email

[2024-08-13 00:34:09,399: INFO/MainProcess] mingle: searching for neighbors
[2024-08-13 00:34:10,408: INFO/MainProcess] mingle: all alone
[2024-08-13 00:34:10,439: INFO/MainProcess] celery@MB-Pro---TraPham.local ready.
```
