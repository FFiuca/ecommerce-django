class PasswordInvalidException(Exception):

    def __init__(self, message='Password Invalid') -> None:
        super().__init__(message)

class AccountInactive(Exception):

    def __init__(self, message='Account Inactive') -> None:
        super().__init__(message)
