# Check the computer's public IP address

This script will check the computer's public IP address and send an email if it has changed.

## .env file template

```bash
GMAIL_PASSWORD=""
GMAIL_SENDER=""
GMAIL_RECIPIENT=""
GMAIL_SUBJECT="Public IP Address Changed"
GMAIL_SMTP_SERVER="smtp.gmail.com"
GMAIL_SMTP_PORT="465"
```

## crontab

You can run a cron job to check the public IP address every specified interval.

```bash
# crontab -e
* * * * * /usr/bin/python <path-to-working-dir>/check_ip.py
```
