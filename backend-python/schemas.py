from typing import Optional
from pydantic import BaseModel

class TaskBase(BaseModel):
    id: Optional[str] = None
    title: str
    description : Optional[str] = None
    completed: bool = False
    category: str = "General"
    priority: str = "Medium"
    # duration_start: int
    # duration_end: int
    # is_completed: bool = False

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: str

    class Config:
        from_attributes = True
    