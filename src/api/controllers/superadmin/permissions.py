from fastapi import APIRouter

router = APIRouter()


@router.get("/permissions/", tags=["permissions"])
async def read_permissions():
    return [{"rolename": "Rick"}, {"rolename": "Morty"}]
