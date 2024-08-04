from fastapi import APIRouter

from src.api.controllers import users
from src.api.controllers import tasks
from src.api.controllers.public import health

router = APIRouter(prefix='/api')
router.include_router(health.router)
router.include_router(users.router)
router.include_router(tasks.router)
