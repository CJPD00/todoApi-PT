from datetime import datetime
from typing import Literal
from pydantic import BaseModel


class TaskBase(BaseModel):
    title: str
    description: str | None = None


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    state: Literal["pendiente", "completado"] | None = None

    class Config:
        extra = "forbid"


class TaskOut(TaskBase):
    id: int
    owner_id: int
    state: str
    created_at: datetime

    class Config:
        from_attributes = True
