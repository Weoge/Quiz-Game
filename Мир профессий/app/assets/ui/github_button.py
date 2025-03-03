import pygame
import app.constants.main.constants as constants
import app.constants.colors.colors as colors
import webbrowser

class GithubButton():
    def __init__(self, screen, x: int, y: int, image, hover_image):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = image
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.hover_image = hover_image
        self.hover_image = pygame.transform.scale(self.hover_image, (50, 50))
        self.button_image = self.image
        self.rect = self.button_image.get_rect()
        self.rect.center = (self.x, self.y)
        self.clicked = False
    
    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.button_image = self.hover_image
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                webbrowser.open(constants.GITHUB_LINK)
        else:
            self.button_image = self.image
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        self.screen.blit(self.button_image, self.rect)
        return action