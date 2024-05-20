from pydantic import BaseModel, ConfigDict


class LevelBase(BaseModel):
    creator_user_id: int
    creator_username: str
    level_data: str


class LevelCreate(LevelBase):
    pass


class LevelSchema(LevelBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
