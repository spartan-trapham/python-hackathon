from dependency_injector import containers

from src.containers.service_container import ServiceContainer


class APIContainer(ServiceContainer):
    wiring_config = containers.WiringConfiguration(
        packages=[
            "..api",
            "..api.controllers",
        ]
    )
