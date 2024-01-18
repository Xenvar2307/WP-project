import pygame
from enum import Enum
from number_values import *
from button import *
from health_bar import *
from damage_text import *
from character import *
from styles import *
from interfaces import *
from ability import *
from action_panel import *
import random
from itertools import cycle

pygame.init()

# frames control
fps = 60
clock = pygame.time.Clock()


# get screen setup
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("WP-project")
# pygame.display.set_icon()
dev_mode = True

# fonts
font_main = pygame.font.SysFont("Caslon Antique", 30)
font_caslon_for_scaling = pygame.font.SysFont("Caslon Antique", 200)
font_damagetext_normal = pygame.font.SysFont(
    "Caslon Antique", 36
)  # check if correct size
HealthBar_font = pygame.font.SysFont("Caslon Antique", 25)

# load images
# menu module
menu_run_button = pygame.image.load("img/buttons/menu_run.png").convert_alpha()
menu_place_holder_button = pygame.image.load(
    "img/buttons/menu_place_holder.png"
).convert_alpha()

# battle module
battle_return_to_main_menu_button = pygame.image.load(
    "img/buttons/return_to_main_menu.png"
).convert_alpha()

bottom_panel = pygame.image.load("img/Background/bottom_panel.png").convert_alpha()
battle_background = pygame.image.load(
    "img/Background/battle_background.png"
).convert_alpha()

# global classes FACTORIES
BFactory_GreyText = ButtonFactory_GreyMiddleText()
AttackSTFactory = AttackSTAbility_Factory()
HealNTFactory = HealNTAbility_Factory()


# fill screen with black to reset vision
def reset_screen():
    screen.fill(black)


def draw_bottom_panel():
    screen.blit(bottom_panel, (0, screen_height - bottom_panel_height))


def draw_battle_background():
    screen.blit(battle_background, (0, 0))


class Exit_app_module:
    def run(self):
        pygame.quit()
        return Module_names.Exit_app


class MainMenu_module:
    def run(self, dev_mode):
        clock.tick(fps)
        run = True
        Next_module = Module_names.Exit_app

        # create menu buttons
        Run_button = BFactory_GreyText.factory(
            screen,
            "Run",
            font_caslon_for_scaling,
            middle_width - menu_button_width / 2,
            title_height + menu_button_padding,
            menu_button_width,
            menu_button_height,
        )

        second_button = BFactory_GreyText.factory(
            screen,
            "Second Button",
            font_caslon_for_scaling,
            middle_width - menu_button_width / 2,
            title_height + 3 * menu_button_padding + 1 * menu_button_height,
            menu_button_width,
            menu_button_height,
        )

        third_button = BFactory_GreyText.factory(
            screen,
            "Third Button",
            font_caslon_for_scaling,
            middle_width - menu_button_width / 2,
            title_height + 5 * menu_button_padding + 2 * menu_button_height,
            menu_button_width,
            menu_button_height,
        )

        while run:
            # draw basic image
            screen.fill(menu_background_color)

            # menu buttons
            if Run_button.draw():
                run = False
                Next_module = Module_names.Battle

            if second_button.draw():
                pass

            if third_button.draw():
                pass

            if dev_mode:
                # Game title
                pygame.draw.rect(
                    screen,
                    yellow,
                    (middle_width - title_width / 2, 0, title_width, title_height),
                    width=1,
                )
                draw_text(
                    screen,
                    "Title of the game",
                    font_caslon_for_scaling,
                    yellow,
                    middle_width - title_width / 2,
                    0,
                    title_width,
                    title_height,
                )
                # run button
                pygame.draw.rect(
                    screen,
                    yellow,
                    (
                        middle_width - menu_button_width / 2,
                        title_height + menu_button_padding,
                        menu_button_width,
                        menu_button_height,
                    ),
                    width=1,
                )
                draw_text(
                    screen,
                    "Run button",
                    font_caslon_for_scaling,
                    yellow,
                    middle_width - menu_button_width / 2,
                    title_height + menu_button_padding,
                    int(menu_button_width / 5),
                    int(menu_button_height / 1),
                )
                # 2nd button
                pygame.draw.rect(
                    screen,
                    yellow,
                    (
                        middle_width - menu_button_width / 2,
                        title_height + 3 * menu_button_padding + 1 * menu_button_height,
                        menu_button_width,
                        menu_button_height,
                    ),
                    width=1,
                )
                draw_text(
                    screen,
                    "2nd button",
                    font_caslon_for_scaling,
                    yellow,
                    middle_width - menu_button_width / 2,
                    title_height + 3 * menu_button_padding + 1 * menu_button_height,
                    int(menu_button_width / 5),
                    int(menu_button_height / 1),
                )
                # 3rd button
                pygame.draw.rect(
                    screen,
                    yellow,
                    (
                        middle_width - menu_button_width / 2,
                        title_height + 5 * menu_button_padding + 2 * menu_button_height,
                        menu_button_width,
                        menu_button_height,
                    ),
                    width=1,
                )
                draw_text(
                    screen,
                    "3rd button",
                    font_caslon_for_scaling,
                    yellow,
                    middle_width - menu_button_width / 2,
                    title_height + 5 * menu_button_padding + 2 * menu_button_height,
                    int(menu_button_width / 5),
                    int(menu_button_height / 1),
                )

            # event control
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    Next_module = Module_names.Exit_app
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clicked = True
                else:
                    clicked = False

            # updating display
            pygame.display.update()

        return Next_module


class Battle_module:
    def run(self, dev_mode):
        run = True
        Next_module = Module_names.Exit_app

        return_to_main_button = BFactory_GreyText.factory(
            screen,
            "Return to Main Menu",
            font_caslon_for_scaling,
            screen_width - 250,
            0,
            250,
            50,
        )

        restart_button = BFactory_GreyText.factory(
            screen,
            "Restart Battle",
            font_caslon_for_scaling,
            screen_width / 2 - 125,
            0,
            250,
            50,
        )

        allies = []
        enemies = []

        ally_mage = Basic_Character(
            "Mage",
            25,
            25,
            3,
            5,
            3,
            HealNTFactory.factory("Magic"),
            AttackSTFactory.factory("MagicMissile"),
            None,
            team_padding + 3 * character_padding + 1 * character_width_normal,
            ground_level - character_height_normal,
            DamageTextFactory_normal(
                team_padding
                + 3 * character_padding
                + 1 * character_width_normal
                + character_width_normal / 2,
                ground_level - character_height_normal,
                font_damagetext_normal,
            ),
        )

        ally_swordman = Basic_Character(
            "Swordman",
            30,
            30,
            3,
            3,
            5,
            HealNTFactory.factory("Bandage"),
            AttackSTFactory.factory("Sword"),
            None,
            team_padding + 5 * character_padding + 2 * character_width_normal,
            ground_level - character_height_normal,
            DamageTextFactory_normal(
                team_padding
                + 5 * character_padding
                + 2 * character_width_normal
                + character_width_normal / 2,
                ground_level - character_height_normal,
                font_damagetext_normal,
            ),
        )

        ally_barbarian = Basic_Character(
            "Barbarian",
            35,
            35,
            5,
            3,
            3,
            None,
            AttackSTFactory.factory("Battleaxe"),
            None,
            team_padding + 7 * character_padding + 3 * character_width_normal,
            ground_level - character_height_normal,
            DamageTextFactory_normal(
                team_padding
                + 7 * character_padding
                + 3 * character_width_normal
                + character_width_normal / 2,
                ground_level - character_height_normal,
                font_damagetext_normal,
            ),
        )

        ally_mage.add_health_bar(Health_bar_normal(ally_mage, HealthBar_font))
        ally_swordman.add_health_bar(Health_bar_normal(ally_swordman, HealthBar_font))
        ally_barbarian.add_health_bar(Health_bar_normal(ally_barbarian, HealthBar_font))
        allies.append(ally_mage)
        allies.append(ally_swordman)
        allies.append(ally_barbarian)

        enemy_first = Basic_Enemy(
            "Warrior",
            20,
            20,
            3,
            3,
            3,
            None,
            AttackSTFactory.factory("Sword"),
            None,
            screen_width
            - team_padding
            - 4 * character_width_normal
            - 7 * character_padding,
            ground_level - character_height_normal,
            DamageTextFactory_normal(
                screen_width
                - team_padding
                - 4 * character_width_normal
                - 7 * character_padding
                + character_width_normal / 2,
                ground_level - character_height_normal,
                font_damagetext_normal,
            ),
        )

        enemy_second = Basic_Enemy(
            "Warrior",
            20,
            20,
            3,
            3,
            3,
            HealNTFactory.factory("Bandage"),
            AttackSTFactory.factory("Battleaxe"),
            None,
            screen_width
            - team_padding
            - 3 * character_width_normal
            - 5 * character_padding,
            ground_level - character_height_normal,
            DamageTextFactory_normal(
                screen_width
                - team_padding
                - 3 * character_width_normal
                - 5 * character_padding
                + character_width_normal / 2,
                ground_level - character_height_normal,
                font_damagetext_normal,
            ),
        )

        enemy_first.add_health_bar(Health_bar_normal(enemy_first, HealthBar_font))
        enemy_second.add_health_bar(Health_bar_normal(enemy_second, HealthBar_font))
        enemies.append(enemy_first)
        enemies.append(enemy_second)

        action_panel = Main_Action_Panel(screen)

        # setup initiative cycle
        initiative_cycle = allies + enemies
        current_character_iter = cycle(initiative_cycle)
        current_character = next(current_character_iter)
        chosen_target = None
        clicked_action = None
        chosen_action = None

        action_cooldown = 90
        action_wait_time = 90
        game_over = 0

        while run:
            clock.tick(fps)
            action_cooldown += 1

            # drawing background

            screen.fill(battle_background_color)
            draw_battle_background()
            draw_bottom_panel()

            draw_raw_text(
                screen,
                f"Current Character: {current_character.name} Chosen action: {str(type(chosen_action))}",
                font_main,
                white,
                0,
                0,
            )

            # drawing characters
            for character in allies:
                character.update()
                character.draw(screen)

            for character in enemies:
                character.update()
                character.draw(screen)

            # drawing menu buttons
            if return_to_main_button.draw():
                run = False
                Next_module = Module_names.Main_menu

            # drawing guiding lines
            if dev_mode:
                # bottom panel
                pygame.draw.rect(
                    screen,
                    yellow,
                    (
                        0,
                        screen_height - bottom_panel_height,
                        screen_width,
                        bottom_panel_height,
                    ),
                    width=1,
                )
                draw_text(
                    screen,
                    "Bottom panel",
                    font_caslon_for_scaling,
                    yellow,
                    0,
                    screen_height - bottom_panel_height,
                    int(menu_button_width / 5),
                    int(menu_button_height / 1),
                )
                # allies
                pygame.draw.rect(
                    screen,
                    yellow,
                    (
                        team_padding + character_padding,
                        ground_level - character_height_normal,
                        character_width_normal,
                        character_height_normal,
                    ),
                    width=1,
                )
                pygame.draw.rect(
                    screen,
                    yellow,
                    (
                        team_padding + character_width_normal + 3 * character_padding,
                        ground_level - character_height_normal,
                        character_width_normal,
                        character_height_normal,
                    ),
                    width=1,
                )
                pygame.draw.rect(
                    screen,
                    yellow,
                    (
                        team_padding
                        + 2 * character_width_normal
                        + 5 * character_padding,
                        ground_level - character_height_normal,
                        character_width_normal,
                        character_height_normal,
                    ),
                    width=1,
                )
                pygame.draw.rect(
                    screen,
                    yellow,
                    (
                        team_padding
                        + 3 * character_width_normal
                        + 7 * character_padding,
                        ground_level - character_height_normal,
                        character_width_normal,
                        character_height_normal,
                    ),
                    width=1,
                )
                # enemies
                pygame.draw.rect(
                    screen,
                    yellow,
                    (
                        middle_width + team_padding + character_padding,
                        ground_level - character_height_normal,
                        character_width_normal,
                        character_height_normal,
                    ),
                    width=1,
                )
                pygame.draw.rect(
                    screen,
                    yellow,
                    (
                        middle_width
                        + team_padding
                        + character_width_normal
                        + 3 * character_padding,
                        ground_level - character_height_normal,
                        character_width_normal,
                        character_height_normal,
                    ),
                    width=1,
                )
                pygame.draw.rect(
                    screen,
                    yellow,
                    (
                        middle_width
                        + team_padding
                        + 2 * character_width_normal
                        + 5 * character_padding,
                        ground_level - character_height_normal,
                        character_width_normal,
                        character_height_normal,
                    ),
                    width=1,
                )
                pygame.draw.rect(
                    screen,
                    yellow,
                    (
                        middle_width
                        + team_padding
                        + 3 * character_width_normal
                        + 7 * character_padding,
                        ground_level - character_height_normal,
                        character_width_normal,
                        character_height_normal,
                    ),
                    width=1,
                )
            if game_over == 0:
                # draw action panel for ally or get enemy
                if current_character in allies:
                    if action_cooldown >= action_wait_time:
                        action_panel.notify(current_character)
                        clicked_action = action_panel.draw()
                        if clicked_action != None and clicked_action != chosen_action:
                            chosen_action = clicked_action
                else:
                    # get action from AI and resolve it at the same time
                    if action_cooldown >= action_wait_time:
                        AI_attack_targets = list(
                            filter(lambda ch: ch.state != "Dead", allies)
                        )
                        current_character.main_attack_ability.action(
                            current_character, random.choice(AI_attack_targets)
                        )
                        current_character = next(current_character_iter)
                        action_cooldown = 0

                # resolve player action
                if chosen_action != None and action_cooldown >= action_wait_time:
                    # resolve action
                    match chosen_action.targets:
                        case 0:  # resolve now
                            chosen_action.action(current_character, chosen_target)
                            action_cooldown = 0
                            chosen_action = None
                            # get next character
                            current_character = next(current_character_iter)
                            while current_character.state == "Dead":
                                current_character = next(current_character_iter)
                        case 1:
                            pygame.mouse.set_visible(True)
                            pos = pygame.mouse.get_pos()
                            for count, enemy in enumerate(
                                list(filter(lambda en: en.state != "Dead", enemies))
                            ):
                                if enemy.rect.collidepoint(pos):
                                    # hide mouse
                                    pygame.mouse.set_visible(False)
                                    # show ability icon
                                    screen.blit(
                                        pygame.transform.scale(
                                            chosen_action.icon, (32, 32)
                                        ),
                                        pos,
                                    )
                                    if clicked == True and enemy.state is not "Dead":
                                        chosen_target = enemy

                            # perform action
                            if chosen_target != None:
                                chosen_action.action(current_character, chosen_target)
                                action_cooldown = 0
                                chosen_action = None
                                chosen_target = None
                                pygame.mouse.set_visible(True)
                                # get next character
                                current_character = next(current_character_iter)
                                while current_character.state == "Dead":
                                    current_character = next(current_character_iter)

                        case _:
                            pass
                else:
                    # wait for choice
                    pass

            # check for dead teams
            alive_allies = 0
            for ally in allies:
                if ally.state != "Dead":
                    alive_allies += 1

            if alive_allies == 0:
                game_over = -1

            alive_enemies = 0
            for enemy in enemies:
                if enemy.state != "Dead":
                    alive_enemies += 1

            if alive_enemies == 0:
                game_over = 1

            # check for end of battle
            if game_over != 0:
                if game_over == 1:
                    draw_raw_text(
                        screen,
                        "Victory!",
                        font_caslon_for_scaling,
                        white,
                        screen_width / 2 - 250,
                        50,
                    )
                if game_over == -1:
                    draw_raw_text(
                        screen,
                        "Defeat!",
                        font_caslon_for_scaling,
                        white,
                        screen_width / 2 - 250,
                        50,
                    )
                if restart_button.draw():
                    for character in initiative_cycle:
                        character.reset()
                        current_character_iter = cycle(initiative_cycle)
                        current_character = next(current_character_iter)
                        action_cooldown = 80
                        game_over = 0

            # event control
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    Next_module = Module_names.Exit_app
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clicked = True
                else:
                    clicked = False

            # updating display
            pygame.display.update()

        return Next_module


# module control
class Module_names(Enum):
    Exit_app = Exit_app_module()
    Main_menu = MainMenu_module()
    Battle = Battle_module()


# main control
current_module = Module_names.Main_menu

while current_module != Module_names.Exit_app:
    reset_screen()
    current_module = current_module.value.run(dev_mode)

pygame.quit()
