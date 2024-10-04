#!/usr/bin/python

import datetime
import email
import os
import smtplib

# script constants
TRIGGERING_WORKFLOW_NAME = os.getenv("TRIGGERING_WORKFLOW_NAME")
TRIGGERING_WORKFLOW_ID = os.getenv("TRIGGERING_WORKFLOW_ID")
NOTIFICATION_EMAIL = os.getenv("NOTIFICATION_EMAIL")
NOTIFICATION_PASSWORD = os.getenv("NOTIFICATION_PASSWORD")
NOTIFICATION_RECIPIENT = "jjcarver@ucsd.edu,bandeira@ucsd.edu"
TIMESTAMP_FORMAT = "%I:%M:%S %p %A %d/%m/%Y"
GITHUB_TEST_URL_BASE = "https://github.com/CCMS-UCSD/CCMS-Integration-Tests/actions/runs/"

def test_notify_on_workflow_failure():
    subject = "GitHub CCMS-Integration-Tests Workflow Failure: " + TRIGGERING_WORKFLOW_NAME
    now = datetime.datetime.now().strftime(TIMESTAMP_FORMAT)
    test_link = GITHUB_TEST_URL_BASE + TRIGGERING_WORKFLOW_ID
    email_body = f"""
<h3>{subject}, {now}:</h3>

Test workflow {TRIGGERING_WORKFLOW_NAME} (ID {TRIGGERING_WORKFLOW_ID}) failed: {test_link} 
"""
    message = email.message.EmailMessage()
    message.set_content(email_body, subtype="html")
    message["Subject"] = "[CCMS] " + subject
    message["From"] = NOTIFICATION_EMAIL
    message["To"] = NOTIFICATION_RECIPIENT
    smtp = smtplib.SMTP("smtp.gmail.com", 587)
    smtp.starttls()
    smtp.login(NOTIFICATION_EMAIL, NOTIFICATION_PASSWORD)
    smtp.send_message(message)
    smtp.quit()
