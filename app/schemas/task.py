from pydantic import BaseModel


class TaskBase(BaseModel):
    title: str
    description: str | None = None


class TaskCreate(TaskBase):
    pass


class TaskOut(TaskBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True
