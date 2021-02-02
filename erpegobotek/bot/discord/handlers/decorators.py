from typing import Callable

from erpegobotek.bot.discord.handlers.base import MessageHandlers


def register_handler(pattern: str) -> Callable:
    def register(func: Callable) -> Callable:
        MessageHandlers.register(pattern, func)
        return func

    return register
