class User:
    def __init__(self, name, phone, mail, password):
        self.name = name
        self.mail = mail
        self.phone = phone
        self.password = password

    def json(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "mail": self.mail
        }