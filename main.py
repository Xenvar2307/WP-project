import pygame

pygame.init()

# frames control
fps = 60
clock = pygame.time.Clock()


# window size
screen_width = 1280
screen_height = 720

# get screen setup
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("WP-project")
# pygame.display.set_icon()
dev_mode = True

# STYLES:

# fonts
font_main = pygame.font.SysFont("Caslon Antique", 26)

# colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)

menu_background_color = (105, 93, 74)


def reset_screen():
    screen.fill(black)


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
        background_img = pygame.image.load(
            "img/Background/background.png"
        ).convert_alpha()
        panel_img = pygame.image.load("img/Icons/panel.png").convert_alpha()
        run = True
        Next_module = -1

        while run:
            screen.blit(background_img, (0, 0))
            screen.blit(panel_img, (0, screen_height - 150))

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
