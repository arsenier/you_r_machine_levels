"""
Create
Read
Update
Delete
"""

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Score

from .schemas import ScoreCreate


async def get_scores(session: AsyncSession) -> list[Score]:
    stmt = select(Score).order_by(Score.id)
    result: Result = await session.execute(stmt)
    scores = result.scalars().all()
    return list(scores)


async def get_top10(session: AsyncSession) -> list[Score]:
    stmt = select(Score).order_by(-Score.score).limit(10)
    result: Result = await session.execute(stmt)
    scores = result.scalars().all()
    return list(scores)


async def get_top(session: AsyncSession, limit: int) -> list[Score]:
    stmt = select(Score).order_by(-Score.score).limit(limit)
    result: Result = await session.execute(stmt)
    scores = result.scalars().all()
    return list(scores)


async def get_score(session: AsyncSession, score_id: int) -> Score | None:
    return await session.get(Score, score_id)


async def create_score(session: AsyncSession, score_in: ScoreCreate) -> Score:
    score = Score(**score_in.model_dump())
    session.add(score)
    await session.commit()
    # await session.refresh(product)
    return score


async def delete_score(
    session: AsyncSession,
    score: Score,
) -> None:
    await session.delete(score)
    await session.commit()
