from typing import Optional
from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    description : Optional[str] = None
    duration_start: int
    duration_end: int
    is_completed: bool = False

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int

    class Config:
        from_attributes = True
    