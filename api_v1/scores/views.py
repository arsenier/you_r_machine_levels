from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from . import crud
from .dependencies import score_by_id
from .schemas import ScoreSchema, ScoreCreate

router = APIRouter(tags=["Scores"])


@router.get("/", response_model=list[ScoreSchema])
async def get_scores(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_scores(session=session)


@router.get("/top10/", response_model=list[ScoreSchema])
async def get_top10(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_top10(session=session)


@router.get("/top/{limit}/", response_model=list[ScoreSchema])
async def get_top10(
    limit: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_top(session=session, limit=limit)


@router.post(
    "/",
    response_model=ScoreSchema,
    status_code=status.HTTP_201_CREATED,
)
async def create_score(
    score_in: ScoreCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_score(session=session, score_in=score_in)


@router.get("/{score_id}/", response_model=ScoreSchema)
async def get_score(
    product: ScoreSchema = Depends(score_by_id),
):
    return product


@router.delete("/{score_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_score(
    score: ScoreSchema = Depends(score_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    await crud.delete_score(session=session, score=score)
