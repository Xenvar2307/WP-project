import pygame
from abc import ABC, abstractmethod


# Buttons
class Button(ABC):
    @abstractmethod
    def draw(self):
        pass


class Buttonfactory_middle_text(ABC):
    @abstractmethod
    def factory(self, surface, text, font, x, y, width, height):
        pass


# HealthBars
class Health_bar(ABC):
    @abstractmethod
    def notify(self, character):
        pass

    @abstractmethod
    def draw(self, surface):
        pass


# Characters
class Character(ABC):
    @abstractmethod
    def draw(self, surface):
        pass

    @abstractmethod
    def add_health_bar(self, new_health_bar: Health_bar):
        pass

    @abstractmethod
    def remove_health_bar(self, health_bar):
        pass
