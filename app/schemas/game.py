from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional


class GameSchema(BaseModel):
    # Nothing needed from client for now - future: players?, names?, current wind? etc.
    pass


class GameOutSchema(BaseModel):
    id: int
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)
