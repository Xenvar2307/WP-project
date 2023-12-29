from abc import ABC, abstractmethod


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
    def factory(self, surface, text, font, x, y, width, height) -> Button:
        pass


# HealthBars
class Health_bar(ABC):
    @abstractmethod
    def notify(self, character) -> None:
        pass

    @abstractmethod
    def draw(self, surface) -> None:
        pass


# Characters
class Character(ABC):
    @abstractmethod
    def draw(self, surface) -> None:
        pass

    @abstractmethod
    def add_health_bar(self, new_health_bar: Health_bar) -> None:
        pass

    @abstractmethod
    def remove_health_bar(self, health_bar) -> Health_bar:
        pass


# Damage Texts
class DamageText(ABC):
    @abstractmethod
    def update(self):
        pass


# for use in characters
class DamageTextFactory(ABC):
    @abstractmethod
    def factory(self, value):
        pass
