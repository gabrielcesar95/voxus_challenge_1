class ValidationException(Exception):
    error: str

    def __init__(self, error: str):
        self.error = error