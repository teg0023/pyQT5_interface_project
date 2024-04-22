class DuplicateOid(Exception):
    def __init__(self, message, value):
        super().__init__(message)
        self.value = value

class DuplicateEmail(Exception):
    def __init__(self, message, value):
        super().__init__(message)
        self.value = value