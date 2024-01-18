import pygame
from damage_text import DamageTextFactory
from interfaces import DamageTextFactory
from styles import *
from number_values import *
from interfaces import *
from damage_text import *


class Basic_Character:
    def __init__(
        self,
        name,
        HP,
        MAX_HP,
        strength,
        power,
        dexterity,
        healing_ability,
        main_attack_ability,
        special_ability,
        x,
        y,
        damagetexts_factory: DamageTextFactory,
    ):
        # basic stats
        self.name = name
        # health control
        self.current_hp = HP
        self.max_hp = MAX_HP
        self.health_bars = set()
        # stats
        self.strength = strength
        self.power = power
        self.dexterity = dexterity
        # abilities
        self.healing_ability = healing_ability
        self.main_attack_ability = main_attack_ability
        self.special_ability = special_ability

        # technical and design part

        # control of damage texts
        self.sprite_group = pygame.sprite.Group()
        self.damagetexts_factory = damagetexts_factory

        # position
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

        # set starting image
        self.image = self.animation_dict.get("Idle")[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        # image control
        animation_cooldown = 100
        self.image = self.animation_dict.get(self.state)[self.frame_index]
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1

        if self.frame_index >= len(self.animation_dict.get(self.state)):
            if self.state == "Dead":
                self.frame_index = len(self.animation_dict.get(self.state)) - 1
            else:
                self.play_animation("Idle")

        # update connected sprites
        self.sprite_group.update()

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        # temporary
        for HB in self.health_bars:
            HB.draw(surface)

        # draw connected sprites
        self.sprite_group.draw(surface)

    def play_animation(self, animation_name):
        if animation_name in self.animation_dict.keys():
            self.state = animation_name
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()
        else:
            print("No such animation name in loaded animations of this character")

    def add_health_bar(self, new_health_bar: Health_bar):
        self.health_bars.add(new_health_bar)
        new_health_bar.notify(self)

    def remove_health_bar(self, health_bar: Health_bar):
        self.health_bars.discard(health_bar)
        return health_bar

    def heal(self, value):
        if value <= self.max_hp - self.current_hp:
            healed_value = value
        else:
            healed_value = self.max_hp - self.current_hp

        self.current_hp += healed_value
        # TO DO add sprite for heal effect

        for HB in self.health_bars:
            HB.notify(self)

        self.damagetexts_factory.factory(healed_value, green)

    def take_damage(self, value):
        if value >= self.current_hp:
            damage_value = self.current_hp
            self.play_animation("Dead")
        else:
            damage_value = value
            self.play_animation("Hurt")

        self.current_hp -= damage_value

        for HB in self.health_bars:
            HB.notify(self)

        # not a mistake, show damage dealt not how much got to 0
        self.damagetexts_factory.factory(value, red)


class Basic_Enemy(Basic_Character):
    def __init__(
        self,
        name,
        HP,
        MAX_HP,
        strength,
        power,
        dexterity,
        healing_ability,
        main_attack_ability,
        special_ability,
        x,
        y,
        damagetexts_factory: DamageTextFactory,
    ):
        super().__init__(
            name,
            HP,
            MAX_HP,
            strength,
            power,
            dexterity,
            healing_ability,
            main_attack_ability,
            special_ability,
            x,
            y,
            damagetexts_factory,
        )
        for list in self.animation_dict.values():
            for i, frame in enumerate(list):
                list[i] = pygame.transform.flip(frame, True, False)

    def AI_act(self):
        pass
