from fastapi import APIRouter

router = APIRouter()


@router.get("/roles/", tags=["roles"])
async def read_roles():
    return [{"rolename": "Rick"}, {"rolename": "Morty"}]
