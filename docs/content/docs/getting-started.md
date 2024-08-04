+++
weight = 100
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
 fastapi dev src/main.py 
```

If everything is set up correctly, you will get this
```
INFO     Using path src/main.py                                                                                                                                                                                     
INFO     Resolved absolute path /Users/${USER_NAME}/${PATH}/python-hackathon/src/main.py                                                                                                                       
INFO     Searching for package file structure from directories with __init__.py files                                                                                                                               
INFO     Importing from /Users/${USER_NAME}/${PATH}/python-hackathon                                                                                                                                           
                                                                                                                                                                                                                    
 ╭─ Python package file structure ─╮                                                                                                                                                                                
 │                                 │                                                                                                                                                                                
 │  📁 src                         │                                                                                                                                                                                
 │  ├── 🐍 __init__.py             │                                                                                                                                                                                
 │  └── 🐍 main.py                 │                                                                                                                                                                                
 │                                 │                                                                                                                                                                                
 ╰─────────────────────────────────╯                                                                                                                                                                                
                                                                                                                                                                                                                    
INFO     Importing module src.main                                                                                                                                                                                  
INFO     Found importable FastAPI app                                                                                                                                                                               
                                                                                                                                                                                                                    
 ╭── Importable FastAPI app ──╮                                                                                                                                                                                     
 │                            │                                                                                                                                                                                     
 │  from src.main import app  │                                                                                                                                                                                     
 │                            │                                                                                                                                                                                     
 ╰────────────────────────────╯                                                                                                                                                                                     
                                                                                                                                                                                                                    
INFO     Using import string src.main:app                                                                                                                                                                           
                                                                                                                                                                                                                    
 ╭────────── FastAPI CLI - Development mode ───────────╮                                                                                                                                                            
 │                                                     │                                                                                                                                                            
 │  Serving at: http://127.0.0.1:8000                  │                                                                                                                                                            
 │                                                     │                                                                                                                                                            
 │  API docs: http://127.0.0.1:8000/docs               │                                                                                                                                                            
 │                                                     │                                                                                                                                                            
 │  Running in development mode, for production use:   │                                                                                                                                                            
 │                                                     │                                                                                                                                                            
 │  fastapi run                                        │                                                                                                                                                            
 │                                                     │                                                                                                                                                            
 ╰─────────────────────────────────────────────────────╯      
```

You can call `/api/health`, the message "Hello world" will be printed under object schema.

```
{"Hello":"World"}
```
