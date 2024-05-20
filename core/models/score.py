from sqlalchemy.orm import Mapped

from .base import Base


class Score(Base):
    user_id: Mapped[int]
    username: Mapped[str]
    score: Mapped[int]
