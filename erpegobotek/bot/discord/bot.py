import asyncio
from typing import Optional

import discord

from erpegobotek.bot.discord.handlers.base import Registry


# NOTE: check if it is better practice to pass loggers or to just use logger object
# NOTE: eventually force message_handlers to be passed as kwarg
# NOTE: move logic of dice rolling to message handlers
class DiscordBotClient(discord.Client):
    def __init__(
        self,
        message_handle_registry: Registry,
        *,
        loop: Optional[asyncio.AbstractEventLoop] = None,
        **options,
    ):
        self.message_handle_registry = message_handle_registry
        super().__init__(loop=loop, **options)

    async def on_ready(self):
        print("Logged in to channel")

    async def on_message(self, message: discord.Message):
        if message.author == self.user:
            return

        await self.message_handle_registry.handle_message(message)
