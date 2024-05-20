"""
Create
Read
Update
Delete
"""

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Level

from .schemas import LevelCreate


async def get_levels(session: AsyncSession) -> list[Level]:
    stmt = select(Level).order_by(Level.id)
    result: Result = await session.execute(stmt)
    levels = result.scalars().all()
    return list(levels)


async def get_top10(session: AsyncSession) -> list[Level]:
    stmt = select(Level).order_by(-Level.level).limit(10)
    result: Result = await session.execute(stmt)
    levels = result.scalars().all()
    return list(levels)


async def get_top(session: AsyncSession, limit: int) -> list[Level]:
    stmt = select(Level).order_by(-Level.level).limit(limit)
    result: Result = await session.execute(stmt)
    levels = result.scalars().all()
    return list(levels)


async def get_level(session: AsyncSession, level_id: int) -> Level | None:
    return await session.get(Level, level_id)


async def create_level(session: AsyncSession, level_in: LevelCreate) -> Level:
    level = Level(**level_in.model_dump())
    session.add(level)
    await session.commit()
    # await session.refresh(product)
    return level


async def delete_level(
    session: AsyncSession,
    level: Level,
) -> None:
    await session.delete(level)
    await session.commit()
