# Template API

## Requirements

- Python v3.11

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

## Project structure

```
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
