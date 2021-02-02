import re
from typing import Awaitable, Callable, Dict

import discord


class MessageHandlers:
    _handlers: Dict[str, Callable] = {}

    @classmethod
    def register(cls, pattern: str, handler_func: Callable[[discord.Message], Awaitable]):
        cls._handlers[pattern] = handler_func

    @classmethod
    def unregister(cls, pattern: str):
        cls._handlers.pop(pattern)

    @classmethod
    async def match(cls, message: discord.Message):
        for pattern, handler_func in cls._handlers.items():
            if (match := re.match(pattern, message.content)) is not None:
                await handler_func(message, match)
