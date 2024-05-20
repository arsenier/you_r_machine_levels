from sqlalchemy.orm import Mapped

from .base import Base


class Level(Base):
    creator_user_id: Mapped[int]
    creator_username: Mapped[str]
    level_data: Mapped[str]
