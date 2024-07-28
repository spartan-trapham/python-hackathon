from fastapi import APIRouter

from src.api.controllers import admin
from src.api.controllers import health

router = APIRouter(prefix='/api')
router.include_router(health.router)
router.include_router(admin.router)
