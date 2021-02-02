import os

from erpegobotek.bot.discord.exceptions import ImproperlyConfigured

# NOTE: this could be validated if it's not an empty string, etc
try:
    DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]
except KeyError as err:
    raise ImproperlyConfigured(f"Missing configuration: {err.args}")
