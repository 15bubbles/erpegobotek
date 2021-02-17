import re
from typing import Any, Awaitable, Callable, Dict, Protocol, Type, Union

import discord

DiscordMessageHandler = Callable[[discord.Message, re.Match], Awaitable]


class Registry(Protocol):
    @classmethod
    def register(cls, pattern: str, handler_function: Callable) -> None:
        pass

    @classmethod
    def unregister(cls, pattern: str) -> None:
        pass

    @classmethod
    async def handle_message(cls, message: Any, use_full_match: bool = False) -> None:
        pass


class DiscordMessageHandlersRegistry:
    _handlers: Dict[str, DiscordMessageHandler] = {}

    def __init__(self, handlers: Dict[str, DiscordMessageHandler]) -> None:
        self._handlers = handlers

    @classmethod
    def register(cls, pattern: str, handler_function: DiscordMessageHandler) -> None:
        cls._handlers[pattern] = handler_function

    @classmethod
    def unregister(cls, pattern: str) -> None:
        cls._handlers.pop(pattern, None)

    @classmethod
    async def handle_message(cls, message: discord.Message, full_match: bool = False) -> None:
        matching_function = re.match if full_match is True else re.search

        for pattern, handler_function in cls._handlers.items():
            if (match := matching_function(pattern, message.content)) is not None:
                await handler_function(message, match)


def register(
    pattern: str,
    handler_function: DiscordMessageHandler,
    registry: Union[Type[Registry], Registry] = DiscordMessageHandlersRegistry,
) -> None:
    registry.register(pattern, handler_function)
