import schemas
from database import fake_tasks
from typing import List
from services.google_calendar import get_calendar_service
from services.google_calendar import get_calendar_events
from services.outlook_calendar import get_msal_app
from services.outlook_calendar import get_auth_url, get_token_from_code, get_outlook_events
from fastapi import FastAPI , HTTPException
from fastapi.responses import RedirectResponse


app = FastAPI(title = "NeverLate API", version = "0.1.0")

outlook_access_token = None


@app.get("/")
def read_root():
    """Welcome message for API"""
    return {"Message" : "Welcome to NeverLate API - This is our clever calender assistance"}

@app.get("/login/outlook")
def login_outlook():
    auth_url = get_auth_url()
    return RedirectResponse(auth_url)

@app.get("/callback/outlook")
def callback_outlook(code: str):
    global outlook_access_token

    token = get_token_from_code(code)
    if not token:
        raise HTTPException(status_code = 400, detail="Failed to retrieve Microsoft access token")
    
    outlook_access_token = token

    return {"status": "Success", "message": "Microsoft access code received!", "code": code}


@app.get("/health")
def health_check():
    """Endpoints the check if the server is alive"""
    return {"status" : "up", "service" : "backend-python"}

@app.get("/tasks", response_model=List[schemas.Task])
def read_tasks(limit: int = 10):

    all_tasks = []
    for tasks in fake_tasks:
        all_tasks.append(tasks)
    # Fetch the google calender
    try:
        google_events = get_calendar_events()
        for event in google_events:
            all_tasks.append({
                "id": str(event.get("id")),
                "title": event.get("summary", "No Title"),
                "start": event["start"].get("dateTime", event["start"].get("date")),
                "provider": "google"
            })
    except Exception as e:
        print(f"Google Calendar error: {e}")

    # fetch outlook calender events

    if outlook_access_token:
        try:
            outlook_events = get_outlook_events()
            for event in outlook_events:
                all_tasks.append({
                    "id": str(event.get("id")),
                    "title": event.get("Subject", "No Title"),
                    "start": event["start"].get("dateTime"),
                    "provider": "outlook"
                })
        except Exception as e:
            print(f"Outlook Calendar error: {e}")
    return all_tasks

    # events = get_calendar_events()
    # tasks = []
    # for event in events:
    #     tasks.append({
    #         "id": event.get("id"),
    #         "title": event.get("summary", "No Title"),
    #         "start": event["start"].get("dateTime", event["start"].get("date")),
    #         "provider": "google_calendar"
    #     })
    # return {"Tasks":tasks}
    # try:
    #     events = get_calendar_events()
    #     return {"tasks": events}
    # except Exception as e:
    #     return {"Error" : str(e)}


# @app.get("/tasks", response_model=List[schemas.Task])
# def get_tasks():
#     """All tasks came"""
#     """Fetch all tasks (currently returnning an empty files)"""
#     return fake_tasks

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



