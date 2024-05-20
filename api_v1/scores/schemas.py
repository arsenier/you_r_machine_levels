from pydantic import BaseModel, ConfigDict


class ScoreBase(BaseModel):
    user_id: int
    username: str
    score: int


class ScoreCreate(ScoreBase):
    pass


class ScoreSchema(ScoreBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
