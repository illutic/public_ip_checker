import smtplib
import os
import subprocess
from dotenv import load_dotenv
from email.mime.text import MIMEText

def write_ip_to_file(ip: str):
    with open("public_ip", "w") as f:
        f.write(ip)
    
def read_ip_from_file():
    try:
        with open("public_ip", "r") as f:
            return f.read()
    except FileNotFoundError:
        return ""

def send_email(body: str):
    sender = os.getenv("GMAIL_SENDER")
    password = os.getenv("GMAIL_PASSWORD")
    sender = os.getenv("GMAIL_SENDER")
    recipients = [os.getenv("GMAIL_RECIPIENT")]
    subject = os.getenv("GMAIL_SUBJECT")
    smtp_server = os.getenv("GMAIL_SMTP_SERVER")
    smtp_port = os.getenv("GMAIL_SMTP_PORT")

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ", ".join(recipients)
    with smtplib.SMTP_SSL(smtp_server, int(smtp_port)) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")

load_dotenv()
public_ip = subprocess.run(["dig", "+short", "myip.opendns.com", "@resolver1.opendns.com"], capture_output=True, text=True).stdout.strip()
print(f"Public IP: {public_ip}")
stored_ip = read_ip_from_file()
print(f"Stored IP: {stored_ip}")
if public_ip != stored_ip:
    print("IP has changed!")
    write_ip_to_file(public_ip)
    send_email(f"Your IP has changed to {public_ip}")