from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper, Score

from . import crud


async def score_by_id(
    score_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Score:
    score = await crud.get_score(session=session, score_id=score_id)
    if score is not None:
        return score

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Score {score_id} not found!",
    )
