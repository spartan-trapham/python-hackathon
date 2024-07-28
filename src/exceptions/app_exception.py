from starlette.status import (
    HTTP_500_INTERNAL_SERVER_ERROR,
    HTTP_401_UNAUTHORIZED,
    HTTP_400_BAD_REQUEST,
    HTTP_403_FORBIDDEN,
    HTTP_404_NOT_FOUND,
)

ERROR_ID_BAD_REQUEST = 'SYS-0400'
ERROR_ID_UNAUTHENTICATED = 'SYS-0401'
ERROR_ID_FORBIDDEN = 'SYS-0403'
ERROR_ID_NOT_FOUND = 'SYS-0404'
ERROR_ID_SERVER_ERROR = 'SYS-0500'
ERROR_ID_UNKNOWN = 'SYS-0900'
ERROR_ID_RESOURCE_NOT_FOUND = 'RES-0404'


class AppException(Exception):
    def __init__(self, error_id: str = ERROR_ID_UNKNOWN, status_code: int = 500, **kwargs):
        self.status_code = status_code
        self.error = {
            'error_id': error_id,
            'title': error_id,
            'message': error_id,
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


class AppFieldException(AppException):
    def __init__(self, error_id: str, field: str, message: str):
        super().__init__(error_id, field=field)
        self.error.pop('error_id')
        self.error.pop('title')
        self.error['type'] = error_id
        self.error['message'] = message


class AppValidationException(AppException):
    def __init__(self, errors: [AppFieldException]):
        super().__init__(ERROR_ID_BAD_REQUEST, HTTP_400_BAD_REQUEST, errors=errors)


class AppBadRequestException(AppException):
    def __init__(self):
        super().__init__(ERROR_ID_BAD_REQUEST, HTTP_400_BAD_REQUEST)


class AppUnauthorizedException(AppException):
    def __init__(self):
        super().__init__(ERROR_ID_UNAUTHENTICATED, HTTP_401_UNAUTHORIZED)


class AppForbiddenException(AppException):
    def __init__(self):
        super().__init__(ERROR_ID_FORBIDDEN, HTTP_403_FORBIDDEN)


class AppNotFoundException(AppException):
    def __init__(self):
        super().__init__(ERROR_ID_NOT_FOUND, HTTP_404_NOT_FOUND)


class AppServerException(AppException):
    def __init__(self):
        super().__init__(ERROR_ID_SERVER_ERROR, HTTP_500_INTERNAL_SERVER_ERROR)


class AppUnknownException(AppException):
    def __init__(self):
        super().__init__(ERROR_ID_UNKNOWN, HTTP_400_BAD_REQUEST)
        self.need_report = True
