#!/usr/bin/python

import datetime
import email
import os
import smtplib

# script constants
TRIGGERING_WORKFLOW_NAME = os.getenv("TRIGGERING_WORKFLOW_ID")
TRIGGERING_WORKFLOW_ID = os.getenv("TRIGGERING_WORKFLOW_ID")
TIMESTAMP_FORMAT = "%A %d/%m/%Y"
GITHUB_TEST_URL_BASE = "https://github.com/CCMS-UCSD/CCMS-Integration-Tests/actions/runs/"
SENDER = "ccms@proteomics.ucsd.edu"
RECIPIENT = "jjcarver@ucsd.edu,bandeira@ucsd.edu"

def test_notify_on_workflow_failure():
    subject = "[CCMS] GitHub CCMS-Integration-Tests Workflow Failure: " + TRIGGERING_WORKFLOW_NAME + " (" + TRIGGERING_WORKFLOW_ID + ")"
    now = datetime.datetime.now().strftime(TIMESTAMP_FORMAT)
    test_link = GITHUB_TEST_URL_BASE + TRIGGERING_WORKFLOW_ID
    email_body = """
<h3>{subject}, {now}:</h3>

Test workflow {TRIGGERING_WORKFLOW_NAME} (ID {TRIGGERING_WORKFLOW_ID}) failed: {test_link} 
"""
    message = email.message.EmailMessage()
    message.set_content(email_body, subtype="html")
    message["Subject"] = subject
    message["From"] = SENDER
    message["To"] = RECIPIENT
    smtp = smtplib.SMTP("localhost")
    smtp.send_message(message)
    smtp.quit()
