from dataclasses import dataclass

from erpegobotek.domain.dice_roll.dices import Dice, get_dice


@dataclass
class DiceRoller:
    dice: Dice

    def roll(self, rolls: int):
        return (self.dice.roll() for _ in range(rolls))


def build_dice_roller(sides: int) -> DiceRoller:
    dice = get_dice(sides)
    return DiceRoller(dice)
