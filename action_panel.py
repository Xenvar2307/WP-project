import pygame
from interfaces import Character
from styles import *
from number_values import *
from interfaces import *
from button import *
from health_bar import *


class Main_Action_Panel:
    def __init__(self, surface) -> None:
        self.surface = surface
        self.empty_ability_icon = pygame.image.load(
            "img/Icons/NoAbility.png"
        ).convert_alpha()
        self.font = pygame.font.SysFont("Caslon Antique", 22)

        self.heal_button = BasicButton(
            surface,
            self.empty_ability_icon,
            25,
            screen_height - 100,
            icon_size,
            icon_size,
        )
        self.attack_button = BasicButton(
            surface,
            self.empty_ability_icon,
            25 + 64 + 16,
            screen_height - 100,
            icon_size,
            icon_size,
        )
        self.special_ability_button = BasicButton(
            surface,
            self.empty_ability_icon,
            25 + 2 * 64 + 2 * 16,
            screen_height - 100,
            icon_size,
            icon_size,
        )

        self.health_bar = Health_bar_action_panel(
            pygame.font.SysFont("Caslon Antique", 36)
        )

    def notify(self, character: Character):
        if character.healing_ability != None:
            self.heal_button.image = character.healing_ability.icon
        else:
            self.heal_button.image = self.empty_ability_icon
        if character.main_attack_ability != None:
            self.attack_button.image = character.main_attack_ability.icon
        else:
            self.attack_button.image = self.empty_ability_icon
        if character.special_ability != None:
            self.special_ability_button.image = character.special_ability.icon
        else:
            self.special_ability_button.image = self.empty_ability_icon

        self.health_bar.notify(character)

    def draw(self):
        draw_raw_text(
            self.surface,
            "Choose action:",
            self.font,
            white,
            25,
            screen_height - 150,
        )
        draw_raw_text(
            self.surface,
            "  Heal     Attack    Special  ",
            self.font,
            white,
            25,
            screen_height - 125,
        )
        self.heal_button.draw()
        self.attack_button.draw()
        self.special_ability_button.draw()

        self.health_bar.draw(self.surface)
