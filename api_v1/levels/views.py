from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from . import crud
from .dependencies import level_by_id
from .schemas import LevelSchema, LevelCreate

router = APIRouter(tags=["Levels"])


@router.get("/", response_model=list[LevelSchema])
async def get_levels(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_levels(session=session)


@router.post(
    "/",
    response_model=LevelSchema,
    status_code=status.HTTP_201_CREATED,
)
async def create_level(
    level_in: LevelCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_level(session=session, level_in=level_in)


@router.get("/{level_id}/", response_model=LevelSchema)
async def get_level(
    product: LevelSchema = Depends(level_by_id),
):
    return product


@router.delete("/{level_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_level(
    level: LevelSchema = Depends(level_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    await crud.delete_level(session=session, level=level)
