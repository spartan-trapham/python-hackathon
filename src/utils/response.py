from starlette.responses import JSONResponse
from pydantic import BaseModel
from src.core.app_exceptions import AppException


def response_item(item: BaseModel) -> dict:
    return {
        'data': item.dict,
    }


def response_pagination(items: list, total_records: int, current_page: int, total_pages: int, ) -> dict:
    return {
        'data': {
            'items': items,
            'pagination': {
                'total_records': total_records,
                'current_page': current_page,
                'total_pages': total_pages,
            },
        },
    }


def response_error(exception: AppException):
    return JSONResponse({'error': exception.to_dict()}, status_code=exception.status_code)
