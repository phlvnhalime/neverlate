import os.path
import datetime
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

#Skope
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def get_calendar_service():
    creds = None

    if(os.path.exists('token.json')):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
        
    return build('calendar', 'v3', credentials=creds)

def get_calendar_events(limit=10):
    service = get_calendar_service()
    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    events_result = service.events().list(calendarId='primary', 
                                          timeMin=now,
                                          maxResults=10,
                                          singleEvents=True,
                                          orderBy='startTime').execute()
    return events_result.get('items', [])



