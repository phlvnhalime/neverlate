from typing import List
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import models
import schemas
from database import engine, get_db
from utils.security import hash_password, verify_password, create_access_token, get_current_user
from utils.email import generate_verification_code, send_verification_email

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="NeverLate API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:8080",
        "http://tauri.localhost",
        "https://tauri.localhost",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ── AUTH ENDPOINTS ───────────────────────────────────────────────────────────

@app.post("/auth/register", response_model=schemas.UserResponse)
def register(user: schemas.UserRegister, db: Session = Depends(get_db)):
    existing = db.query(models.User).filter(models.User.email == user.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    if user.password != user.password_confirm:
        raise HTTPException(status_code=400, detail="Passwords do not match")

    if len(user.password) < 6:
        raise HTTPException(status_code=400, detail="Password must be at least 6 characters")

    code = generate_verification_code()

    new_user = models.User(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        hashed_password=hash_password(user.password),
        verification_code=code,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    send_verification_email(user.email, code)

    return new_user


@app.post("/auth/verify", response_model=schemas.Token)
def verify_email(data: schemas.VerifyEmail, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == data.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user.is_verified:
        raise HTTPException(status_code=400, detail="Already verified")

    if user.verification_code != data.code:
        raise HTTPException(status_code=400, detail="Invalid verification code")

    user.is_verified = True
    user.verification_code = None
    db.commit()

    return schemas.Token(access_token=create_access_token(user.id))


@app.post("/auth/login", response_model=schemas.Token)
def login(data: schemas.UserLogin, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == data.email).first()
    if not user or not verify_password(data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    if not user.is_verified:
        raise HTTPException(status_code=403, detail="Email not verified. Check your inbox.")

    return schemas.Token(access_token=create_access_token(user.id))


@app.get("/auth/me", response_model=schemas.UserResponse)
def get_me(current_user: models.User = Depends(get_current_user)):
    return current_user


# ── GENERAL ENDPOINTS ────────────────────────────────────────────────────────

@app.get("/")
def read_root():
    return {"message": "Welcome to NeverLate API"}


@app.get("/health")
def health_check():
    return {"status": "up", "service": "backend-python"}


# ── TASK ENDPOINTS (protected) ───────────────────────────────────────────────

@app.get("/tasks", response_model=List[schemas.Task])
def get_tasks(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    return db.query(models.Task).filter(models.Task.user_id == current_user.id).all()


@app.get("/tasks/{task_id}", response_model=schemas.Task)
def get_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    task = db.query(models.Task).filter(
        models.Task.id == task_id,
        models.Task.user_id == current_user.id,
    ).first()
    if not task:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")
    return task


@app.post("/tasks", response_model=schemas.Task, status_code=201)
def create_task(
    task: schemas.TaskCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    new_task = models.Task(
        title=task.title,
        description=task.description,
        completed=task.completed,
        category=task.category,
        priority=task.priority,
        user_id=current_user.id,
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


@app.put("/tasks/{task_id}", response_model=schemas.Task)
def update_task(
    task_id: int,
    updated: schemas.TaskCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    task = db.query(models.Task).filter(
        models.Task.id == task_id,
        models.Task.user_id == current_user.id,
    ).first()
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
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    task = db.query(models.Task).filter(
        models.Task.id == task_id,
        models.Task.user_id == current_user.id,
    ).first()
    if not task:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")
    db.delete(task)
    db.commit()
    return {"message": f"Task {task_id} deleted"}
