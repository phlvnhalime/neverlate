import msal 
import os
import requests
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("OUTLOOK_CLIENT_ID")
print(f"DEBUG: Outlook Client ID is: {CLIENT_ID}", flush=True)
CLIENT_SECRET = os.getenv("OUTLOOK_CLIENT_SECRET")
AUTHORITY = "https://login.microsoftonline.com/common"

SCOPES = ["Calendars.Read"]

def get_msal_app():
    return msal.ConfidentialClientApplication(
        CLIENT_ID,
        authority=AUTHORITY,
        client_credential=CLIENT_SECRET,
    )

def get_auth_url():
    app =get_msal_app()
    auth_url = app.get_authorization_request_url(SCOPES, redirect_uri="http://localhost:8000/callback/outlook")
    print(f"DEBUG: Redirecting user to: {auth_url}")
    return auth_url

def get_token_from_code(auth_code):
    app = get_msal_app()

    result = app.acquire_token_by_authorization_code(
        auth_code, scopes=SCOPES, redirect_uri="http://localhost:8000/callback/outlook"
    )
    return result.get("access_token")



def get_outlook_events(token):
    endpoints = "https://graph.microsoft.com/v1.0/me/events"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(endpoints, headers)
    return response.json().get("value", [])