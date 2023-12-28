import pygame
from styles import *
from sizes import *
from interfaces import *
from damage_text import *


class Basic_Character:
    def __init__(self, name, HP, MAX_HP, x, y, damagetexts_factory: DamageTextFactory):
        self.name = name
        self.current_hp = HP
        self.max_hp = MAX_HP
        self.health_bars = set()
        self.sprite_group = pygame.sprite.Group()

        self.damagetexts_factory = damagetexts_factory

        self.x = x
        self.y = y

    def draw(self, surface):
        pygame.draw.rect(
            surface,
            white,
            (self.x, self.y, character_width_normal, character_height_normal),
        )
        # temporary
        for HB in self.health_bars:
            HB.draw(surface)

        # not temporary
        self.sprite_group.update()
        self.sprite_group.draw(surface)

    def add_health_bar(self, new_health_bar: Health_bar):
        self.health_bars.add(new_health_bar)
        new_health_bar.notify(self)

    def remove_health_bar(self, health_bar: Health_bar):
        self.health_bars.discard(health_bar)
        return health_bar
