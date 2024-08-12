+++
weight = 1000
date = "2023-05-03T22:37:22+01:00"
draft = true
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
```shell
celery -A src.workers.brokers.scheduler worker -l INFO
```
