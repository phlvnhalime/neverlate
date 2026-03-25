from typing import Optional
from pydantic import BaseModel, EmailStr


# ── Task schemas ─────────────────────────────────────────────────────────────

class TaskCreate(BaseModel):
    """Shape of the JSON the frontend sends when CREATING a task."""
    title:          str
    description:    Optional[str] = None
    completed:      bool = False
    category:       str  = "General"
    priority:       str  = "Medium"
    duration_start: Optional[int] = None
    duration_end:   Optional[int] = None


class Task(TaskCreate):
    """Shape of the JSON the API sends BACK — includes the database-generated id."""
    id: int
    user_id: Optional[int] = None

    class Config:
        from_attributes = True


# ── Auth schemas ─────────────────────────────────────────────────────────────

class UserRegister(BaseModel):
    first_name:       str
    last_name:        str
    email:            EmailStr
    password:         str
    password_confirm: str


class UserLogin(BaseModel):
    email:    EmailStr
    password: str


class VerifyEmail(BaseModel):
    email: EmailStr
    code:  str


class UserResponse(BaseModel):
    id:          int
    first_name:  str
    last_name:   str
    email:       str
    is_verified: bool

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type:   str = "bearer"
