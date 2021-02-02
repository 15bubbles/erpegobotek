import re

import discord

from erpegobotek.bot.discord.handlers.decorators import register_handler
from erpegobotek.services.dice_roll import roll_dice


@register_handler(r"^([k|d](\d+)),?(\d+)?$")
async def handle_dice_roll(message: discord.Message, match: re.Match):
    dice_type, sides, number_of_rolls = match.groups()
    sides = int(sides)
    number_of_rolls = int(number_of_rolls) if number_of_rolls is not None else 1

    rolls = roll_dice(sides, number_of_rolls)

    await message.channel.send(
        f"{message.author.name} throws {dice_type} die "
        f"{number_of_rolls if number_of_rolls > 1 else ''}"
        f"{'' if number_of_rolls == 1 else ' times'}"
    )
    await message.channel.send(f"Got {rolls.sum}! Individual rolls: {rolls.rolls}")
