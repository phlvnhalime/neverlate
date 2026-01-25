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

@app.get("/tasks")
def get_tasks():
    """Fetch all tasks (currently returnning an empty files)"""
    return []