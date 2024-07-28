from fastapi import APIRouter
from src.api.controllers.admin import users

router = APIRouter(prefix='/admin')
router.include_router(users.router)
