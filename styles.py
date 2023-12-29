import pygame

# colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)

menu_background_color = (105, 93, 74)
battle_background_color = (69, 58, 48)


def draw_text(surface, text, font, text_col, x, y, width, height):
    text_image = font.render(text, True, text_col)

    # focus on height if text fits
    if text_image.get_width() * height / text_image.get_height() < width:
        text_image = pygame.transform.scale(
            text_image,
            (text_image.get_width() * height / text_image.get_height(), height),
        )
    else:
        text_image = pygame.transform.scale(
            text_image,
            (
                width,
                text_image.get_height() * width / text_image.get_width(),
            ),
        )

    surface.blit(text_image, (x, y))
