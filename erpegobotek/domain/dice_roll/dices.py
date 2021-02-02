import random
from dataclasses import dataclass
from typing import Iterable

from erpegobotek.domain.dice_roll.config import POSSIBLE_DICE_SIDES
from erpegobotek.domain.dice_roll.exceptions import InvalidDice


@dataclass
class Dice:
    sides: int

    def roll(self) -> int:
        return random.randint(1, self.sides)


def get_dice(sides: int, possible_dice_sides: Iterable[int] = POSSIBLE_DICE_SIDES) -> Dice:
    if sides not in possible_dice_sides:
        raise InvalidDice(f"Not possible to get a dice with {sides} number of sides")

    return Dice(sides)
