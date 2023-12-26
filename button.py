import pygame


class Button:
    def __init__(self, surface, image, x, y, width, height):
        self.image = pygame.transform.scale(image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.surface = surface

    def draw(self):
        # return value, tells us if we should act
        action = False

        # mouse position
        pos = pygame.mouse.get_pos()

        # mouse on button
        if self.rect.collidepoint(pos):
            # check for release of button
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                action = True
                self.clicked = True

        # reset clicked status
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        self.surface.blit(self.image, (self.rect.x, self.rect.y))

        return action
