import pygame
from styles import *
from number_values import *
from interfaces import *


class Health_bar_normal:
    def __init__(self, character: Character, font):
        self.id = "normal_health_bar"
        self.current_hp = character.current_hp
        self.max_hp = character.max_hp
        self.character_name = character.name
        self.x = character.x
        self.y = character.y + character_height_normal
        self.font = font

    def notify(self, character: Character):
        self.current_hp = character.current_hp
        self.max_hp = character.max_hp
        self.character_name = character.name
        self.x = character.x + character_width_normal / 2 - health_bar_normal_width / 2
        self.y = character.y + character_height_normal + 30

    def draw(self, surface):
        draw_raw_text(
            surface, self.character_name, self.font, white, self.x, self.y - 30
        )
        pygame.draw.rect(
            surface,
            red,
            (self.x, self.y, health_bar_normal_width, health_bar_normal_height),
        )
        pygame.draw.rect(
            surface,
            green,
            (
                self.x,
                self.y,
                int(health_bar_normal_width * self.current_hp / self.max_hp),
                health_bar_normal_height,
            ),
        )
