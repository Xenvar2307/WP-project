import pygame
from interfaces import Character
from styles import *
from number_values import *
from interfaces import *


class AttackAction_single_target(ABC):
    def __init__(self, icon) -> None:
        self.icon = icon
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
    def __init__(self, icon) -> None:
        self.icon = icon
        self.targets = 0

    @abstractmethod
    def calc_heal(self, caster: Character, target) -> int:
        pass

    def action(self, caster, target):
        if self.targets == 0:
            caster.heal(self.calc_heal(caster, target))
        else:
            target.heal(self.calc_heal(caster, target))


class HealAction_Bandage(HealAction_no_target):
    def calc_heal(self, caster: Character, target) -> int:
        return caster.dexterity + 1


class HealAction_Magic(HealAction_no_target):
    def calc_heal(self, caster: Character, target) -> int:
        return caster.power * 2


class AttackSTAbility_Factory:
    def __init__(self) -> None:
        self.AttackAction_Fists_icon = pygame.image.load(
            "img/Icons/Attack_fists.png"
        ).convert_alpha()
        self.AttackAction_Sword_icon = pygame.image.load(
            "img/Icons/Attack_sword.png"
        ).convert_alpha()
        self.AttackAction_Battleaxe_icon = pygame.image.load(
            "img/Icons/Attack_battleaxe.png"
        ).convert_alpha()
        self.AttackAction_MagicMissile_icon = pygame.image.load(
            "img/Icons/Attack_magicmissile.png"
        ).convert_alpha()

    def factory(self, weapon: str) -> AttackAction_single_target:
        match weapon:
            case "Fists":
                return AttackAction_Fists(self.AttackAction_Fists_icon)
            case "Sword":
                return AttackAction_Sword(self.AttackAction_Sword_icon)
            case "Battleaxe":
                return AttackAction_BattleAxe(self.AttackAction_Battleaxe_icon)
            case "MagicMissile":
                return AttackAction_MagicMissile(self.AttackAction_MagicMissile_icon)
            case _:
                print("Not recognised weapon type!")
                return None


class HealNTAbility_Factory:
    def __init__(self) -> None:
        self.HealAction_Bandage_icon = pygame.image.load(
            "img/Icons/Heal_bandage.png"
        ).convert_alpha()
        self.HealAction_Magic_icon = pygame.image.load(
            "img/Icons/Heal_magic.png"
        ).convert_alpha()

    def factory(self, tool: str) -> AttackAction_single_target:
        match tool:
            case "Bandage":
                return HealAction_Bandage(self.HealAction_Bandage_icon)
            case "Magic":
                return HealAction_Magic(self.HealAction_Magic_icon)
            case _:
                print("Not recognised healing tool type!")
                return None
