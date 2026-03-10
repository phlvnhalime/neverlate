from typing import List
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

import models
import schemas
from database import engine, get_db

# ── Create all tables in PostgreSQL on startup ────────────────────────────────
#  This reads models.py and creates any tables that don't exist yet.
#  Safe to run every time — it skips tables that already exist.
# ─────────────────────────────────────────────────────────────────────────────
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="NeverLate API", version="0.1.0")


@app.get("/")
def read_root():
    return {"message": "Welcome to NeverLate API"}


@app.get("/health")
def health_check():
    return {"status": "up", "service": "backend-python"}


# ── TASK ENDPOINTS ────────────────────────────────────────────────────────────
#
#  BEFORE (fake list):    fake_tasks.append(...)
#  AFTER  (real DB):      db.add(...) then db.commit()
#
#  Depends(get_db) → FastAPI automatically gives each endpoint a DB session.
# ─────────────────────────────────────────────────────────────────────────────

@app.get("/tasks", response_model=List[schemas.Task])
def get_tasks(db: Session = Depends(get_db)):
    """Read all tasks from PostgreSQL."""
    # SQL equivalent: SELECT * FROM tasks;
    return db.query(models.Task).all()


@app.get("/tasks/{task_id}", response_model=schemas.Task)
def get_task(task_id: int, db: Session = Depends(get_db)):
    """Read one task by ID from PostgreSQL."""
    # SQL equivalent: SELECT * FROM tasks WHERE id = task_id;
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")
    return task


@app.post("/tasks", response_model=schemas.Task, status_code=201)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    """Save a new task to PostgreSQL."""
    # SQL equivalent: INSERT INTO tasks (title, description, ...) VALUES (...);
    new_task = models.Task(
        title=task.title,
        description=task.description,
        completed=task.completed,
        category=task.category,
        priority=task.priority,
    )
    db.add(new_task)      # stage the insert
    db.commit()           # write it to PostgreSQL
    db.refresh(new_task)  # get the auto-generated id back from the DB
    return new_task


@app.put("/tasks/{task_id}", response_model=schemas.Task)
def update_task(task_id: int, updated: schemas.TaskCreate, db: Session = Depends(get_db)):
    """Update an existing task in PostgreSQL."""
    # SQL equivalent: UPDATE tasks SET title=... WHERE id=task_id;
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")
    task.title       = updated.title
    task.description = updated.description
    task.completed   = updated.completed
    task.category    = updated.category
    task.priority    = updated.priority
    db.commit()
    db.refresh(task)
    return task


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    """Delete a task from PostgreSQL."""
    # SQL equivalent: DELETE FROM tasks WHERE id=task_id;
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")
    db.delete(task)
    db.commit()
    return {"message": f"Task {task_id} deleted"}
