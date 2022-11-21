class CustomException(Exception):
    pass


class GenomicValidationError(CustomException):
    def __init__(self, message, *args):
        super().__init__(message, *args)
