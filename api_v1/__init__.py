from fastapi import APIRouter

from .scores.views import router as leaderboard_router

router = APIRouter()
router.include_router(router=leaderboard_router, prefix="/leaderboard")
