from fastapi import APIRouter

from src.api.controllers import health, users

router = APIRouter(prefix='/api')
router.include_router(health.router)
router.include_router(users.router)
