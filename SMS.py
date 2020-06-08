class SMS:
    def __init__(self, receiver, message):
        self.receiver = receiver
        self.message = message

    def json(self):
        return {
            "receiver": self.receiver,
            "message": self.message
        }