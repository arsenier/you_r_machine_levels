from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper, Level

from . import crud


async def level_by_id(
    level_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Level:
    level = await crud.get_level(session=session, level_id=level_id)
    if level is not None:
        return level

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Level {level_id} not found!",
    )
