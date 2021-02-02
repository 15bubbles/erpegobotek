class DiceException(Exception):
    def __init__(self, message: str, *args):
        self.message = message
        super().__init__(message, *args)


class InvalidDice(DiceException):
    """Raised when a dice with invalid number of sides has been requested"""
