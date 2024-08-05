from ..libs.log.logging import setup_logger


class BaseService:
    def __init__(self) -> None:
        pass
        self.logger = setup_logger(self.__class__.__name__)
