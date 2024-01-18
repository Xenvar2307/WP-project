from abc import ABC, abstractmethod
import pygame


# Modules
class Module(ABC):
    @abstractmethod
    def run(self, dev_mode: bool):
        pass


# Buttons
class Button(ABC):
    # draws itself and returns if it was clicked with left mouse button
    @abstractmethod
    def draw(self) -> bool:
        pass


class Buttonfactory_middle_text(ABC):
    @abstractmethod
    def factory(
        self,
        surface: pygame.Surface,
        text: str,
        font: pygame.font,
        x: int,
        y: int,
        width: int,
        height: int,
    ) -> Button:
        pass


# HealthBars
class Health_bar(ABC):
    @abstractmethod
    def notify(self, character) -> None:
        pass

    @abstractmethod
    def draw(self, surface: pygame.Surface) -> None:
        pass


# Characters
class Character(ABC):
    @abstractmethod
    def update(self) -> None:
        pass

    @abstractmethod
    def draw(self, surface: pygame.Surface) -> None:
        pass

    @abstractmethod
    def play_animation(self, animation_name: str) -> None:
        pass

    @abstractmethod
    def add_health_bar(self, new_health_bar: Health_bar) -> None:
        pass

    @abstractmethod
    def remove_health_bar(self, health_bar) -> Health_bar:
        pass

    @abstractmethod
    def heal(self, value: int) -> None:
        pass

    @abstractmethod
    def take_damage(self, value: int) -> None:
        pass


# Damage Texts
class DamageText(ABC):
    @abstractmethod
    def update(self):
        pass


# for use in characters
class DamageTextFactory(ABC):
    @abstractmethod
    def factory(self, value: int, color) -> pygame.sprite.Sprite:
        pass


class Ability(ABC):
    @abstractmethod
    def action(self, caster: Character, target: Character) -> None:
        pass
