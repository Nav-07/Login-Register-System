import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import abort

class Mail:
    def __init__(self, receiver, subject, message):
        self.receiver = receiver
        self.subject = subject
        self.message = message

    def send(self): # Send the Mail using SMTPLib
        message = MIMEMultipart()
        message['To'] = self.receiver
        message['From'] = os.environ['GMAIL_ADDRESS']
        message['Subject'] = self.subject
        message.attach(MIMEText(self.message, 'plain'))

        
        server = smtplib.SMTP('smtp.gmail.com', port=587)
        server.ehlo()
        server.starttls()
        server.login(os.environ['GMAIL_ADDRESS'], os.environ['GMAIL_PASSWORD'])
        server.sendmail(os.environ['GMAIL_ADDRESS'], self.receiver, message.as_string())
        server.quit()

    def json(self):
        return {
            "receiver": self.receiver,
            "subject": self.subject,
            "message": self.message
        }