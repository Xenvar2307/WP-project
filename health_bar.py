import pygame
from styles import *
from number_values import *
from interfaces import *


class Health_bar_normal:
    def __init__(self, character: Character):
        self.id = "normal_health_bar"
        self.current_hp = character.current_hp
        self.max_hp = character.max_hp
        self.character_name = character.name
        self.x = character.x
        self.y = character.y + character_height_normal

    def notify(self, character: Character):
        self.current_hp = character.current_hp
        self.max_hp = character.max_hp
        self.character_name = character.name
        self.x = character.x
        self.y = character.y + character_height_normal

    def draw(self, surface):
        pygame.draw.rect(
            surface,
            red,
            (self.x, self.y, health_bar_normal_width, health_bar_normal_height),
        )
