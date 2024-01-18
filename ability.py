import pygame
from interfaces import Character
from styles import *
from number_values import *
from interfaces import *


class AttackAction_single_target(ABC):
    def __init__(self) -> None:
        self.icon = None
        self.targets = 1

    @abstractmethod
    def calc_damage(self, caster: Character, target: Character) -> int:
        pass

    def action(self, caster: Character, target: Character) -> None:
        caster.play_animation("Attack")
        target.play_animation("Hurt")
        target.take_damage(self.calc_damage(caster, target))


class AttackAction_Fists(AttackAction_single_target):
    def calc_damage(self, caster: Character, target: Character):
        return caster.strength + 1


class AttackAction_Sword(AttackAction_single_target):
    def calc_damage(self, caster: Character, target: Character):
        return caster.dexterity + 6


class AttackAction_BattleAxe(AttackAction_single_target):
    def calc_damage(self, caster: Character, target: Character) -> int:
        return caster.strength * 2 + 3


class AttackAction_MagicMissile(AttackAction_single_target):
    def calc_damage(self, caster: Character, target: Character) -> int:
        return caster.power * 3


class HealAction_no_target(ABC):
    def __init__(self) -> None:
        self.icon = None
        self.targets = 0

    @abstractmethod
    def calc_heal(self, caster: Character, target) -> int:
        pass

    def action(self, caster, target):
        if self.targets == 0:
            caster.heal(self.calc_heal())
        else:
            target.heal(self.calc_heal())


class HealAction_Bandage(HealAction_no_target):
    def calc_heal(self, caster: Character, target) -> int:
        return caster.dexterity + 1


class HealAction_Magic(HealAction_no_target):
    def calc_heal(self, caster: Character, target) -> int:
        return caster.power * 2
