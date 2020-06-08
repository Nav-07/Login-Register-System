from twilio.rest import Client
import os

class SMS:
    def __init__(self, receiver, message):
        self.receiver = receiver
        self.message = message

    def send(self): # Send the Message to the Phone Number
        client = Client(os.environ['SID'], os.environ['AUTH'])
        message = client.messages.create(body=self.message, from_=os.environ['TWILIO_PHONE'], to=self.receiver)

    def json(self):
        return {
            "receiver": self.receiver,
            "message": self.message
        }