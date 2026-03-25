from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from database import Base


class User(Base):
    __tablename__ = "users"

    id                = Column(Integer, primary_key=True, index=True, autoincrement=True)
    first_name        = Column(String, nullable=False)
    last_name         = Column(String, nullable=False)
    email             = Column(String, unique=True, nullable=False, index=True)
    hashed_password   = Column(String, nullable=False)
    is_verified       = Column(Boolean, default=False)
    verification_code = Column(String, nullable=True)
    created_at        = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    tasks = relationship("Task", back_populates="owner")


class Task(Base):
    __tablename__ = "tasks"

    id          = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title       = Column(String, nullable=False)
    description = Column(String, nullable=True)
    completed   = Column(Boolean, default=False)
    category    = Column(String, default="General")
    priority       = Column(String, default="Medium")
    duration_start = Column(Integer, nullable=True)
    duration_end   = Column(Integer, nullable=True)
    user_id        = Column(Integer, ForeignKey("users.id"), nullable=True)

    owner = relationship("User", back_populates="tasks")
