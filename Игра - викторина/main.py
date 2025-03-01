import pygame
import app.constants.main.constants as constants
import app.constants.colors.colors as colors
import app.assets.ui.Button as button
import app.assets.ui.github_button as githubButton
import app.functions.playButtonClicked as playButtonClicked

def main():
    #initialization
    pygame.init()
    screen = pygame.display.set_mode(constants.SCREEN_SIZE)
    pygame.display.set_caption(constants.GAME_NAME)
    pygame.display.set_icon(pygame.image.load("app/assets/images/icon.png"))
    screen.fill(colors.BLACK)

    #ui
    play_Button = button.Button(screen, 320, 130, pygame.image.load("app/assets/images/green_button.png"), pygame.image.load("app/assets/images/green_button_hover.png"), "Играть", lambda: playButtonClicked.playButtonClicked())
    github_button = githubButton.GithubButton(screen, 605, 445, pygame.image.load("app/assets/images/github_button.png"), pygame.image.load("app/assets/images/github_button_hover.png"))
    level_easy = button.Button(screen, 320, 200, pygame.image.load("app/assets/images/green_button.png"), pygame.image.load("app/assets/images/green_button_hover.png"), "Легкий", lambda: print("easy"))
    level_medium = button.Button(screen, 320, 270, pygame.image.load("app/assets/images/yellow_button.png"), pygame.image.load("app/assets/images/yellow_button_hover.png"), "Средний", lambda: print("medium"))
    level_hard = button.Button(screen, 320, 340, pygame.image.load("app/assets/images/red_button.png"), pygame.image.load("app/assets/images/red_button_hover.png"), "Сложный", lambda: print("hard"))

    Running = True
    #main cycle
    while Running:
        if playButtonClicked.clicked == False:
            screen.fill(colors.BLACK)
            play_Button.draw()
            github_button.draw()
        elif playButtonClicked.clicked == True:
            screen.fill(colors.BLACK)
            level_easy.draw()
            level_medium.draw()
            level_hard.draw()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Running = False
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()