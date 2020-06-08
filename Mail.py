class Mail:
    def __init__(self, receiver, subject, message):
        self.receiver = receiver
        self.subject = subject
        self.message = message

    def json(self):
        return {
            "receiver": self.receiver,
            "subject": self.subject,
            "message": self.message
        }