import pygame
from sizes import *
import button

pygame.init()

# frames control
fps = 60
clock = pygame.time.Clock()


# get screen setup
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("WP-project")
# pygame.display.set_icon()
dev_mode = True

# STYLES:

# fonts
font_main = pygame.font.SysFont("Caslon Antique", 30)

# colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)

menu_background_color = (105, 93, 74)
battle_background_color = (69, 58, 48)


# fill screen with black to reset vision
def reset_screen():
    screen.fill(black)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


class MainMenu_module:
    def run(self, dev_mode):
        background_img = pygame.image.load(
            "img/Background/background.png"
        ).convert_alpha()
        run = True
        Next_module = -1

        while run:
            # draw basic image
            screen.fill(menu_background_color)

            if dev_mode:
                # Game title
                pygame.draw.rect(
                    screen, yellow, (screen_width / 2 - 300, 30, 600, 250), width=1
                )
                draw_text(
                    "Title of the game", font_main, yellow, screen_width / 2 - 300, 30
                )
                # run button
                pygame.draw.rect(
                    screen, yellow, (screen_width / 2 - 200, 370, 400, 50), width=1
                )
                draw_text("Run button", font_main, yellow, screen_width / 2 - 200, 370)
                # 2nd button
                pygame.draw.rect(
                    screen, yellow, (screen_width / 2 - 200, 440, 400, 50), width=1
                )
                draw_text("2nd button", font_main, yellow, screen_width / 2 - 200, 440)
                # 3rd button
                pygame.draw.rect(
                    screen, yellow, (screen_width / 2 - 200, 510, 400, 50), width=1
                )
                draw_text("3rd button", font_main, yellow, screen_width / 2 - 200, 510)

            # event control
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    Next_module = -1
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clicked = True
                    # TEMPORARY
                    run = False
                    Next_module = 1
                else:
                    clicked = False

            # updating display
            pygame.display.update()

        return Next_module


class Battle_module:
    def run(self, dev_mode):
        run = True
        Next_module = -1

        while run:
            # drawing background
            screen.fill(battle_background_color)

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
                    # TEMPORARY
                    run = False
                    Next_module = 0
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
