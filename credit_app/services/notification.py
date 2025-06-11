"""Notification service using smtplib (placeholder)."""
from typing import Optional
import os
import smtplib
from email.message import EmailMessage


def send_email(to_address: str, subject: str, body: str) -> None:
    host = os.getenv("SMTP_HOST", "localhost")
    try:
        with smtplib.SMTP(host) as server:
            msg = EmailMessage()
            msg["From"] = "noreply@example.com"
            msg["To"] = to_address
            msg["Subject"] = subject
            msg.set_content(body)
            server.send_message(msg)
    except Exception:
        # In tests or missing server, ignore
        pass
