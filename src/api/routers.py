from fastapi import APIRouter

from src.api.controllers import users, tasks
from src.api.controllers.public import auth, health

router = APIRouter(prefix='/api')
router.include_router(health.router)
router.include_router(users.router)
router.include_router(tasks.router)
router.include_router(auth.router)
