class DiscordBotException(Exception):
    """Generic Discord Bot Exception"""

    def __init__(self, message: str, *args):
        self.message = message
        super().__init__(message, *args)


class ImproperlyConfigured(DiscordBotException):
    """Raised when some necessary configuration is missing"""