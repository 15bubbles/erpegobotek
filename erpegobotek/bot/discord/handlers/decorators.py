from typing import Callable

from erpegobotek.bot.discord.handlers.base import (
    DiscordMessageHandlersRegistry,
    Registry,
)


def register_handler(pattern: str, registry: Registry = DiscordMessageHandlersRegistry) -> Callable:
    def register(func: Callable) -> Callable:
        registry.register(pattern, func)
        return func

    return register
