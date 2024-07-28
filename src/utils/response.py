from starlette.responses import JSONResponse

from src.exceptions.app_exception import AppException


def response_item(item) -> dict:
    return {
        'data': item,
    }


def response_pagination(items: list, limit: int, next_page_token: str = None) -> dict:
    return {
        'data': {
            'items': items,
            'pagination': {
                'limit': limit,
                'next_page_token': next_page_token,
            },
        },
    }


def response_error(exception: AppException):
    return JSONResponse({'error': exception.to_dict()}, status_code=exception.status_code)
