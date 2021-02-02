import re
from dataclasses import dataclass, field
from typing import Iterable

from erpegobotek.domain.dice_roll.dice_roller import build_dice_roller
from erpegobotek.domain.dice_roll.exceptions import InvalidDice


@dataclass
class RollResults:
    sum: int
    rolls: Iterable[int] = field(default_factory=list)


def roll_dice(sides: int, rolls: int = 1) -> RollResults:
    dice_roller = build_dice_roller(sides)
    dice_rolls = list(dice_roller.roll(rolls))

    return RollResults(sum(dice_rolls), dice_rolls)
