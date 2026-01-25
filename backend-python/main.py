import schemas
from database import fake_tasks
from typing import List
from fastapi import FastAPI

app = FastAPI(title = "NeverLate API", version = "0.1.0")


@app.get("/")
def read_root():
    """Welcome message for API"""
    return {"Message" : "Welcome to NeverLate API - This is our clever calender assistance"}

@app.get("/health")
def health_check():
    """Endpoints the check if the server is alive"""
    return {"status" : "up", "service" : "backend-python"}


@app.get("/tasks", response_model=List[schemas.Task])
def get_tasks():
    """All tasks came"""
    """Fetch all tasks (currently returnning an empty files)"""
    return fake_tasks

@app.post("/tasks", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate):
    """Create a new task with an auto-genarated ID"""
    new_id = len(fake_tasks) + 1

    new_task = {
        "id": new_id,
        "title": task.title,
        "description": task.description,
        "duration_start": task.duration_start,
        "duration_end": task.duration_end,
        "is_complete": False

    }
    fake_tasks.append(new_task)
    return new_task


