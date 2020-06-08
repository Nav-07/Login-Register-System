class User:
    def __init__(self, name, mail, password):
        self.name = name
        self.mail = mail
        self.password = password

    def json(self):
        return {
            "name": self.name,
            "mail": self.mail
        }