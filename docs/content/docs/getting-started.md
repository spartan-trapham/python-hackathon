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

```
python -m venv .venv
```

Step 2: Activate venv

```
source .venv/bin/activate
```

Step 3: Install poetry

```
pip install --upgrade pip
pip install poetry
```

Step 4: Run poetry install

```
poetry install
```

## Development

```
export PYTHONPATH="$PWD"
python src/main.py 
```

If everything is set up correctly, you will get this
```
INFO:     Will watch for changes in these directories: ['/Users/sontc/Documents/Data/Project/C0X/python/python-hackathon']
INFO:     Uvicorn running on http://127.0.0.1:8080 (Press CTRL+C to quit)
INFO:     Started reloader process [99878] using WatchFiles
INFO:     Started server process [99884]
INFO:     Waiting for application startup.
INFO:     Application startup complete.    
```

You can call `/api/health`, the message "Hello world" will be printed under object schema.

```
{"Hello":"World"}
```

## Start Celery worker
```shell
celery -A src.celery_app.app worker
```
