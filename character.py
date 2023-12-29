import pygame
from styles import *
from number_values import *
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

        # animation control
        self.animation_dict = {}
        self.frame_index = 0

        self.state = "Idle"
        self.update_time = pygame.time.get_ticks()

        # load images idle
        temp_list = []
        for i in range(8):
            img = pygame.image.load(f"img/Animation/Place_Holder/idle_{i}.png")
            img = pygame.transform.scale(
                img, (character_width_normal, character_height_normal)
            )
            temp_list.append(img)
        self.animation_dict["Idle"] = temp_list

        # load images hurt
        temp_list = []
        for i in range(8):
            img = pygame.image.load(f"img/Animation/Place_Holder/Hurt_{i}.png")
            img = pygame.transform.scale(
                img, (character_width_normal, character_height_normal)
            )
            temp_list.append(img)
        self.animation_dict["Hurt"] = temp_list

        # load images Attack
        temp_list = []
        for i in range(8):
            img = pygame.image.load(f"img/Animation/Place_Holder/Attack_{i}.png")
            img = pygame.transform.scale(
                img, (character_width_normal, character_height_normal)
            )
            temp_list.append(img)
        self.animation_dict["Attack"] = temp_list

        # load images dead
        temp_list = []
        for i in range(9):
            img = pygame.image.load(f"img/Animation/Place_Holder/Dead_{i}.png")
            img = pygame.transform.scale(
                img, (character_width_normal, character_height_normal)
            )
            temp_list.append(img)
        self.animation_dict["Dead"] = temp_list

        self.image = self.animation_dict.get("Idle")[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        animation_cooldown = 100
        self.image = self.animation_dict.get(self.state)[self.frame_index]
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1

        if self.frame_index >= len(self.animation_dict.get(self.state)):
            if self.state == "Dead":
                self.frame_index = len(self.animation_dict.get(self.state)) - 1
            else:
                # put this into function probably
                self.state = "Idle"
                self.frame_index = 0
                self.update_time = pygame.time.get_ticks()

        self.sprite_group.update()

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        # temporary
        for HB in self.health_bars:
            HB.draw(surface)

        # not temporary
        self.sprite_group.draw(surface)

    def add_health_bar(self, new_health_bar: Health_bar):
        self.health_bars.add(new_health_bar)
        new_health_bar.notify(self)

    def remove_health_bar(self, health_bar: Health_bar):
        self.health_bars.discard(health_bar)
        return health_bar
