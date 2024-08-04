from starlette.status import (
    HTTP_500_INTERNAL_SERVER_ERROR, HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST, HTTP_403_FORBIDDEN, HTTP_404_NOT_FOUND,
)

# System common error
BAD_REQUEST_ERROR = {
    'code': 'SYS-0400',
    'http_status': HTTP_400_BAD_REQUEST,
    'message': 'A bad request was made.'
}

UNAUTHENTICATED_ERROR = {
    'code': 'SYS-0401',
    'http_status': HTTP_401_UNAUTHORIZED,
    'message': 'User authentication is not done. You need to log in again.'
}

FORBIDDEN_ERROR = {
    'code': 'SYS-0403',
    'http_status': HTTP_403_FORBIDDEN,
    'message': 'Access is forbidden. You do not have the necessary permissions.'
}

NOT_FOUND_ERROR = {
    'code': 'SYS-0404',
    'http_status': HTTP_404_NOT_FOUND,
    'message': 'The requested resource was not found.'
}

INTERNAL_SERVER_ERROR = {
    'code': 'SYS-0500',
    'http_status': HTTP_500_INTERNAL_SERVER_ERROR,
    'message': 'An internal server error has occurred. Please contact support if the problem persists.'
}

UNKNOWN_ERROR = {
    'code': 'SYS-0900',
    'http_status': HTTP_500_INTERNAL_SERVER_ERROR,
    'message': 'An unknown error has occurred. Please contact support if the problem persists.'
}

# App error
# User errors
USER_NOT_FOUND = {
    'code': 'APP-0201',
    'http_status': HTTP_404_NOT_FOUND,
    'message': 'User not found.'
}

USER_ALREADY_EXISTS = {
    'code': 'APP-0202',
    'http_status': HTTP_400_BAD_REQUEST,
    'message': 'User already exists.'
}

# Company errors
COMPANY_NOT_FOUND = {
    'code': 'APP-0301',
    'http_status': HTTP_404_NOT_FOUND,
    'message': 'Company not found.'
}

COMPANY_ALREADY_EXISTS = {
    'code': 'APP-0302',
    'http_status': HTTP_400_BAD_REQUEST,
    'message': 'Company already exists.'
}
