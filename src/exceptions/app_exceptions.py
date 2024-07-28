from src.core import logging
from src.exceptions.error_codes import UNKNOWN_ERROR, BAD_REQUEST_ERROR, UNAUTHENTICATED_ERROR, FORBIDDEN_ERROR, \
    NOT_FOUND_ERROR, INTERNAL_SERVER_ERROR

logger = logging.setup_logger(__name__)


class AppException(Exception):
    def __init__(self, error_code: dict = UNKNOWN_ERROR, message: str = None, **kwargs):
        self.status_code = error_code['http_status']
        self.error = {
            'code': error_code['code'],
            'message': error_code['message'] if message is None else message,
        }
        for key in kwargs:
            self.error[key] = kwargs[key]

    def to_dict(self):
        dict_data = self.error

        child_errors = self.error.get('errors')
        if child_errors:
            child_error_data = []
            for child_error in child_errors:
                if isinstance(child_error, AppException):
                    child_error_data.append(child_error.to_dict())
            dict_data['errors'] = child_error_data

        return dict_data

    @classmethod
    def bad_request(cls):
        return cls(BAD_REQUEST_ERROR)

    @classmethod
    def unauthorized(cls):
        return cls(UNAUTHENTICATED_ERROR)

    @classmethod
    def forbidden(cls):
        return cls(FORBIDDEN_ERROR)

    @classmethod
    def not_found(cls):
        return cls(NOT_FOUND_ERROR)

    @classmethod
    def server_error(cls):
        return cls(INTERNAL_SERVER_ERROR)

    @classmethod
    def unknown_error(cls):
        return cls(UNKNOWN_ERROR)


class AppFieldException(AppException):
    def __init__(self, type: str, field: str, message: str):
        super().__init__(type=type, field=field)
        self.error.pop('code')
        self.error['message'] = message


class AppValidationException(AppException):
    def __init__(self, errors: [AppFieldException]):
        super().__init__(BAD_REQUEST_ERROR, errors=errors)
