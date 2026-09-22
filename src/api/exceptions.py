

class UserAlreadyExists(Exception):

    def __init__(self):
        self.msg = "User already exists!"
