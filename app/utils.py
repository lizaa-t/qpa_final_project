from functools import wraps

from pydantic import ValidationError

from app.exceptions import GenomicValidationError


def custom_exception(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except ValidationError:
            raise GenomicValidationError("The invalid genomic data value")
    return wrapper
