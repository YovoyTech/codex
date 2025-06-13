"""Notification helpers."""

from typing import Optional

try:
    from twilio.rest import Client as TwilioClient  # type: ignore
except ImportError:  # pragma: no cover
    TwilioClient = None  # type: ignore

import smtplib
from email.message import EmailMessage


def send_email(
    to_address: str, subject: str, body: str, smtp_server: str = "localhost"
) -> None:
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = "no-reply@example.com"
    msg["To"] = to_address
    msg.set_content(body)

    try:
        with smtplib.SMTP(smtp_server) as server:
            server.send_message(msg)
    except Exception:
        pass  # ignore errors in sandbox


def send_sms(
    phone: str,
    body: str,
    twilio_sid: Optional[str] = None,
    twilio_token: Optional[str] = None,
    from_phone: Optional[str] = None,
) -> None:
    if TwilioClient is None or not (twilio_sid and twilio_token and from_phone):
        return
    client = TwilioClient(twilio_sid, twilio_token)
    client.messages.create(body=body, from_=from_phone, to=phone)
