import pygame
import app.constants.main.constants as constants
import app.constants.colors.colors as colors

class Button():
    def __init__(self, screen, x: int, y: int, image, hover_image, button_text: str, function):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = image
        self.image = pygame.transform.scale(self.image, (150, 50))
        self.hover_image = hover_image
        self.hover_image = pygame.transform.scale(self.hover_image, (150, 50))
        self.button_image = self.image
        self.rect = self.button_image.get_rect()
        self.rect.center = (self.x, self.y)
        self.clicked = False
        self.text = button_text
        self.function = function
        self.empty = ""
    
    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.button_image = self.hover_image
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.function()
                action = True
        else:
            self.button_image = self.image
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        self.button_text = constants.FONT.render(self.text, True, colors.WHITE)
        self.button_text_rect = self.button_text.get_rect(center=(self.x, self.y))
        self.screen.blit(self.button_image, self.rect)
        self.screen.blit(self.button_text, self.button_text_rect)
        return action