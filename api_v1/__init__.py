from fastapi import APIRouter

from .levels.views import router as levels_router

router = APIRouter()
router.include_router(router=levels_router, prefix="/levels")
