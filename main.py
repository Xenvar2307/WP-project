import pygame
from sizes import *
from button import *
from health_bar import *
from character import *
from styles import *
from interfaces import *

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
font_caslon_for_scaling = pygame.font.SysFont("Caslon Antique", 120)

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

# global classes
BFactory_GreyText = ButtonFactory_GreyMiddleText()


# fill screen with black to reset vision
def reset_screen():
    screen.fill(black)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


class MainMenu_module:
    def run(self, dev_mode):
        run = True
        Next_module = -1

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
                Next_module = 1

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
                    "Title of the game",
                    font_main,
                    yellow,
                    middle_width - title_width / 2,
                    0,
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
                    "Run button",
                    font_main,
                    yellow,
                    middle_width - menu_button_width / 2,
                    title_height + menu_button_padding,
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
                    "2nd button",
                    font_main,
                    yellow,
                    middle_width - menu_button_width / 2,
                    title_height + 3 * menu_button_padding + 1 * menu_button_height,
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
                    "3rd button",
                    font_main,
                    yellow,
                    middle_width - menu_button_width / 2,
                    title_height + 5 * menu_button_padding + 2 * menu_button_height,
                )

            # event control
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    Next_module = -1
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
        Next_module = -1

        return_to_main_button = BFactory_GreyText.factory(
            screen,
            "Return to Main Menu",
            font_caslon_for_scaling,
            screen_width - 250,
            0,
            250,
            50,
        )

        test_character = Basic_Character(
            "Test character",
            15,
            30,
            team_padding + character_padding,
            ground_level - character_height_normal,
        )

        test_character.add_health_bar(Health_bar_normal(test_character))

        while run:
            # drawing background
            screen.fill(battle_background_color)

            test_character.draw(screen)

            if return_to_main_button.draw():
                run = False
                Next_module = 0

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
                    "Bottom panel",
                    font_main,
                    yellow,
                    0,
                    screen_height - bottom_panel_height,
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

            # event control
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    Next_module = -1
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clicked = True
                else:
                    clicked = False

            # updating display
            pygame.display.update()

        return Next_module


# starting module control
# -1 exit
# 0
MainMenu = MainMenu_module()
# 1
Battle = Battle_module()

# main control
current_module = 0

while current_module != -1:
    reset_screen()
    match current_module:
        case 0:
            current_module = MainMenu.run(dev_mode)
        case 1:
            current_module = Battle.run(dev_mode)
        case _:
            print("Module number not recognised!")
            current_module = -1

pygame.quit()
