

class BaseRuntimeException(BaseException):
    def __init__(self, message):
        super().__init__(message)

class MemoryError(BaseRuntimeException):
    pass

class NameError(MemoryError):
    pass

