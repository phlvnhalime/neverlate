from typing import Optional
from pydantic import BaseModel

# ── CONCEPT: SCHEMAS vs MODELS ───────────────────────────────────────────────
#  models.py  → defines the DATABASE table (SQLAlchemy)
#  schemas.py → defines what JSON goes IN and OUT of your API (Pydantic)
#
#  They look similar but serve different purposes:
#  - Model = how data is stored in PostgreSQL
#  - Schema = how data is validated and shaped for the API
# ────────────────────────────────────────────────────────────────────────────

class TaskCreate(BaseModel):
    """Shape of the JSON the frontend sends when CREATING a task."""
    title:       str
    description: Optional[str] = None
    completed:   bool = False
    category:    str  = "General"
    priority:    str  = "Medium"


class Task(TaskCreate):
    """Shape of the JSON the API sends BACK — includes the database-generated id."""
    id: int

    class Config:
        from_attributes = True  # lets Pydantic read SQLAlchemy model objects
