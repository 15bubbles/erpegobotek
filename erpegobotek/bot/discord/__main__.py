from erpegobotek.bot.discord.bot import DiscordBotClient
from erpegobotek.bot.discord.config import DISCORD_TOKEN
from erpegobotek.bot.discord.handlers.dice_roll_handlers import *
from erpegobotek.bot.discord.handlers.base import MessageHandlers

client = DiscordBotClient(MessageHandlers)
client.run(DISCORD_TOKEN)
