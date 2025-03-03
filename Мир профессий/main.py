import pygame
import app.constants.main.constants as constants
import app.constants.colors.colors as colors
from app.assets.ui.Button import Button
import app.assets.ui.github_button as githubButton
import app.functions.playButtonClicked as playButtonClicked
import app.generator.genrerate_questions as genrerate_questions
import json
import random

questionNumber = 1
correct_answers = 0
gaming = False
current_buttons = None

def create_question_buttons(screen, question_data, profession, level):
    answers = question_data["answers"]
    question_text = constants.FONT.render(question_data["question"], True, colors.WHITE)
    question_text_rect = question_text.get_rect(center=(constants.SCREEN_SIZE[0] // 2, 50))
    correct_answers_text = constants.FONT.render(f"Правильных ответов: {correct_answers}", True, colors.WHITE)
    correct_answers_text_rect = correct_answers_text.get_rect(center=(constants.SCREEN_SIZE[0] // 2, 10))
    button1 = Button(screen, 320, 100, 
        pygame.image.load(f"app/assets/images/{random.choice(colors.BUTTON_COLORS)}_button.png"),
        pygame.image.load(f"app/assets/images/{random.choice(colors.BUTTON_COLORS)}_button_hover.png"),
        answers[0], 
        lambda: check_answer(profession, level, answers[0], screen),
        350, 50)
    button1.set_delay(0.6)
    button2 = Button(screen, 320, 200,
        pygame.image.load(f"app/assets/images/{random.choice(colors.BUTTON_COLORS)}_button.png"),
        pygame.image.load(f"app/assets/images/{random.choice(colors.BUTTON_COLORS)}_button_hover.png"),
        answers[1],
        lambda: check_answer(profession, level, answers[1], screen),
        350, 50)
    button2.set_delay(0.8)
    button3 = Button(screen, 320, 300,
        pygame.image.load(f"app/assets/images/{random.choice(colors.BUTTON_COLORS)}_button.png"),
        pygame.image.load(f"app/assets/images/{random.choice(colors.BUTTON_COLORS)}_button_hover.png"),
        answers[2],
        lambda: check_answer(profession, level, answers[2], screen),
        350, 50)
    button3.set_delay(1)
    button4 = Button(screen, 320, 400,
        pygame.image.load(f"app/assets/images/{random.choice(colors.BUTTON_COLORS)}_button.png"),
        pygame.image.load(f"app/assets/images/{random.choice(colors.BUTTON_COLORS)}_button_hover.png"),
        answers[3],
        lambda: check_answer(profession, level, answers[3], screen),
        350, 50)
    button4.set_delay(1.2)
    return (button1, button2, button3, button4, 
            question_text, question_text_rect, 
            correct_answers_text, correct_answers_text_rect)

def check_answer(profession, level, button_text, screen):
    global questionNumber, correct_answers, gaming, current_buttons
    file_mapping = {
        1: "enginer_questions.json",
        2: "builder_questions.json",
        3: "bank_questions.json"
    }
    question_file = file_mapping.get(profession)
    if question_file:
        with open(f"app/assets/json/{question_file}", "r", encoding='utf-8') as f:
            questions = json.load(f)
            level_key = f"level_{level}"
            questions = questions[level_key]
            current_question = questions[f"question_{questionNumber}"]
            answer = current_question["correct_answer"]
            if button_text == answer:
                correct_answers += 1
            if f"question_{questionNumber + 1}" in questions:
                questionNumber += 1
                next_question = questions[f"question_{questionNumber}"]
                new_buttons = create_question_buttons(screen, next_question, profession, level)
                current_buttons = new_buttons
                gaming = True
            else:
                questionNumber = 4
                gaming = False
                current_buttons = None

def load_current_question(profession, level):
    file_mapping = {
        1: "enginer_questions.json",
        2: "builder_questions.json",
        3: "bank_questions.json"
    }
    question_file = file_mapping.get(profession)
    if question_file:
        with open(f"app/assets/json/{question_file}", "r", encoding='utf-8') as f:
            questions = json.load(f)
            level_questions = questions[f"level_{level}"]
            if f"question_{questionNumber}" in level_questions:
                return level_questions[f"question_{questionNumber}"]
    return None

def main():
    global questionNumber, correct_answers, gaming, current_buttons
    pygame.init()
    screen = pygame.display.set_mode(constants.SCREEN_SIZE)
    pygame.display.set_caption(constants.GAME_NAME)
    pygame.display.set_icon(pygame.image.load("app/assets/images/icon.png"))
    screen.fill(colors.BLACK)

    play_Button = Button(screen, 320, 130,
        pygame.image.load("app/assets/images/green_button.png"), 
        pygame.image.load("app/assets/images/green_button_hover.png"), 
        "Играть", 
        lambda: playButtonClicked.playButtonClicked(), 
        150, 50)
    github_button = githubButton.GithubButton(screen, 605, 445, 
        pygame.image.load("app/assets/images/github_button.png"), 
        pygame.image.load("app/assets/images/github_button_hover.png"))
    profession_engineer = Button(screen, 150, 200,
        pygame.image.load("app/assets/images/green_button.png"), 
        pygame.image.load("app/assets/images/green_button_hover.png"), 
        "Инженер", 
        lambda: genrerate_questions.select_prof(1), 
        150, 50)
    profession_engineer.set_delay(0.1)
    profession_builder = Button(screen, 150, 270,
        pygame.image.load("app/assets/images/orange_button.png"), 
        pygame.image.load("app/assets/images/orange_button_hover.png"), 
        "Строитель", 
        lambda: genrerate_questions.select_prof(2), 
        150, 50)
    profession_builder.set_delay(0.3)
    profession_banker = Button(screen, 150, 340,
        pygame.image.load("app/assets/images/red_button.png"), 
        pygame.image.load("app/assets/images/red_button_hover.png"), 
        "Банкир", 
        lambda: genrerate_questions.select_prof(3), 
        150, 50)
    profession_banker.set_delay(0.5)
    level_1 = Button(screen, 320, 200,
        pygame.image.load("app/assets/images/green_button.png"), 
        pygame.image.load("app/assets/images/green_button_hover.png"), 
        "Уровень 1", 
        lambda: genrerate_questions.select_level(1), 
        150, 50)
    level_1.set_delay(0.1)
    level_2 = Button(screen, 320, 270,
        pygame.image.load("app/assets/images/yellow_button.png"), 
        pygame.image.load("app/assets/images/yellow_button_hover.png"), 
        "Уровень 2", 
        lambda: genrerate_questions.select_level(2), 
        150, 50)
    level_2.set_delay(0.3)

    Running = True
    selected_level = 0
    while Running:
        screen.fill(colors.BLACK)
        if not playButtonClicked.clicked:
            play_Button.draw()
            github_button.draw()
        elif genrerate_questions.get_prof() == 0:
            profession_engineer.draw()
            profession_builder.draw()
            profession_banker.draw()
        elif genrerate_questions.get_level() == 0:
            level_1.draw()
            level_2.draw()
        elif questionNumber <= 3:
            selected_level = genrerate_questions.get_level()
            current_profession = genrerate_questions.get_prof()
            if not gaming or current_buttons is None:
                current_question = load_current_question(current_profession, selected_level)
                if current_question:
                    current_buttons = create_question_buttons(screen, current_question, current_profession, selected_level)
                    gaming = True
                else:
                    questionNumber = 4
            if gaming and current_buttons:
                screen.blit(current_buttons[4], current_buttons[5])
                screen.blit(current_buttons[6], current_buttons[7])
                for i in range(4):
                    current_buttons[i].draw()
        else:
            final_text = constants.FONT.render(
                f"Игра окончена! Правильных ответов: {correct_answers}/3", 
                True, colors.WHITE
            )
            final_rect = final_text.get_rect(
                center=(constants.SCREEN_SIZE[0] // 2, constants.SCREEN_SIZE[1] // 2)
            )
            screen.blit(final_text, final_rect)
            
            restart_text = constants.FONT.render(
                "Нажмите 'R' чтобы начать заново", 
                True, colors.WHITE
            )
            restart_rect = restart_text.get_rect(
                center=(constants.SCREEN_SIZE[0] // 2, constants.SCREEN_SIZE[1] // 2 + 50)
            )
            screen.blit(restart_text, restart_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and questionNumber > 3:
                    questionNumber = 1
                    correct_answers = 0
                    gaming = False
                    current_buttons = None
                    playButtonClicked.clicked = False
                    genrerate_questions.select_prof(0)
                    genrerate_questions.select_level(0)
            elif event.type == pygame.MOUSEBUTTONDOWN and gaming and current_buttons:
                mouse_pos = pygame.mouse.get_pos()
                for i in range(4):
                    button = current_buttons[i]
                    if button.rect.collidepoint(mouse_pos):
                        check_answer(genrerate_questions.get_prof(), selected_level, button.text, screen)
                        break
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()
