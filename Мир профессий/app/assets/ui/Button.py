import pygame
import app.constants.main.constants as constants
import app.constants.colors.colors as colors
import time

class Button:
    def __init__(self, screen, x, y, image, hover_image, text, action, width, height):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(image, (width, height))
        self.hover_image = pygame.transform.scale(hover_image, (width, height))
        self.current_image = self.image
        self.rect = self.image.get_rect(center=(x, y))
        self.text = text
        self.action = action
        self.clicked = False
        self.creation_time = time.time()
        self.delay = 0
        self.visible = False

    def set_delay(self, delay):
        self.delay = delay
        self.creation_time = time.time()
        self.visible = False

    def draw(self):
        current_time = time.time()
        if not self.visible and current_time - self.creation_time >= self.delay:
            self.visible = True
        if not self.visible:
            return
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.current_image = self.hover_image
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                self.action()
        else:
            self.current_image = self.image
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        self.screen.blit(self.current_image, self.rect)
        if len(self.text) >= 25:
            text_surface = constants.SMALLER_FONT.render(self.text, True, colors.WHITE)
        elif len(self.text) >= 15:
            text_surface = constants.SMALL_FONT.render(self.text, True, colors.WHITE)
        else:
            text_surface = constants.FONT.render(self.text, True, colors.WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        self.screen.blit(text_surface, text_rect)
