from typing import Any
import pygame
from styles import *
from sizes import *
from interfaces import *


class BasicDamageText(pygame.sprite.Sprite):
    def __init__(self, x, y, value, font, color, life):
        pygame.sprite.Sprite.__init__(self)
        self.image = font.render(value, True, color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.counter = 0
        self.life = life

    def update(self):
        self.rect.y -= 1
        self.counter += 1
        if self.counter > self.life:
            self.kill()


class DamageTextFactory_normal:
    def __init__(self, x, y, font):
        self.x = x
        self.y = y
        self.font = font

    def factory(self, value) -> pygame.sprite.Sprite:
        if value > 0:
            color = green
            value_shown = value
        elif value < 0:
            color = red
            value_shown = -value
        else:
            color = white
            value_shown = value

        return BasicDamageText(
            self.x, self.y, str(value_shown), self.font, color, DamageTextLife_normal
        )
