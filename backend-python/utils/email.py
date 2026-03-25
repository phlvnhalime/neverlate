import os
import secrets
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

GMAIL_ADDRESS      = os.getenv("GMAIL_ADDRESS", "")
GMAIL_APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD", "")


def generate_verification_code() -> str:
    return str(secrets.randbelow(900000) + 100000)


def send_verification_email(to_email: str, code: str):
    if not GMAIL_ADDRESS or not GMAIL_APP_PASSWORD:
        print(f"[DEV MODE] Verification code for {to_email}: {code}")
        return

    msg = MIMEMultipart()
    msg["From"]    = GMAIL_ADDRESS
    msg["To"]      = to_email
    msg["Subject"] = "NeverLate — Verify your email"

    body = f"""
    <h2>Welcome to NeverLate!</h2>
    <p>Your verification code is:</p>
    <h1 style="letter-spacing: 8px; font-size: 36px; color: #6366f1;">{code}</h1>
    <p>Enter this code in the app to verify your account.</p>
    <p>If you didn't sign up, you can ignore this email.</p>
    """

    msg.attach(MIMEText(body, "html"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(GMAIL_ADDRESS, GMAIL_APP_PASSWORD)
            server.send_message(msg)
    except Exception as e:
        print(f"[EMAIL FAILED] Could not send email: {e}")
        print(f"[DEV MODE] Verification code for {to_email}: {code}")
