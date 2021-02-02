import asyncio
from typing import Optional, Type

import discord

from erpegobotek.bot.discord.handlers.base import MessageHandlers


# NOTE: check if it is better practice to pass loggers or to just use logger object
# NOTE: eventually force message_handlers to be passed as kwarg
# NOTE: move logic of dice rolling to message handlers
class DiscordBotClient(discord.Client):
    def __init__(
        self,
        message_handlers: Type[MessageHandlers],
        *,
        loop: Optional[asyncio.AbstractEventLoop] = None,
        **options,
    ):
        self.message_handlers = message_handlers
        super().__init__(loop=loop, **options)

    async def on_ready(self):
        print("Logged in to channel")

    async def on_message(self, message: discord.Message):
        if message.author == self.user:
            return

        await self.message_handlers.match(message)
