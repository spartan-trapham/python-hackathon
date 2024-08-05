import uvicorn

from src.containers.container import Container

app_config = Container.configuration().app


if __name__ == "__main__":
    uvicorn.run(
        app="fast_api_app:app",
        host=app_config.host,
        port=app_config.port,
        workers=app_config.workers,
        reload=True if app_config.environment != 'production' else False
    )
