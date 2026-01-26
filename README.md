# 📅 NeverLate - Smart Organization App

NeverLate is a modern organization application built with a microservices architecture using Python (FastAPI) and Node.js. It aims to provide a unified platform to manage both Google and Outlook calendars efficiently. This project is being developed as part of the curriculum at 42 Heilbronn.

## 🚀 Current Progress (Done)
We have successfully established the core foundations of the project:

- **Backend Architecture:** A robust API structure has been implemented using FastAPI (Python).
- **Dockerization:** All services (Python, Node.js, PostgreSQL) are containerized and orchestrated via `docker-compose`.
- **Google Calendar Integration:** Completed the integration of Google API, including OAuth2 authentication and fetching calendar events.
- **Database Schema:** Developed user and task models using Pydantic and SQLAlchemy for structured data management.
- **CI/CD Pipeline:** Configured automated build and test pipelines on GitLab.

## 🎯 Roadmap (Future Goals)
The following features are planned for the next phases:

- [ ] **Microsoft Outlook Integration:** Integrating Microsoft Graph API via Azure Portal to sync Outlook calendars.
- [ ] **Unified Dashboard:** Merging Google and Outlook events into a single, cohesive user interface.
- [ ] **AI-Powered Task Priority:** Implementing algorithms to automatically rank tasks based on urgency and importance.
- [ ] **Frontend Development:** Creating an intuitive web interface for seamless schedule management.
- [ ] **Notification System:** Real-time alerts and reminders for critical tasks.

## 🛠️ Tech Stack
- **Backend:** Python 3.11, FastAPI, Node.js
- **Database:** PostgreSQL
- **DevOps:** Docker, Docker Compose, GitLab CI/CD
- **APIs:** Google Calendar API, Microsoft Graph API

## ⚙️ Installation
To run this project locally:

1. Clone the repository:
   ```bash
   git clone [https://gitlab.com/phlvnhalime/organization-todo-app.git](https://gitlab.com/phlvnhalime/organization-todo-app.git)