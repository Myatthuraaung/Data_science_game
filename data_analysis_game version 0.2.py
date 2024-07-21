import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Data Analysis Game")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Set up fonts
font = pygame.font.Font(None, 36)

# Game variables
current_level = 1
max_level = 10
hints_remaining = 3
answer = ""
question_displayed = False

# Data for problems
level_data = {
    1: {
        "question": "Calculate the mean of the following numbers: [1, 2, 3, 4, 5]",
        "answer": "3"
    }
}

# Game clock
clock = pygame.time.Clock()

# Function to draw text
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Function to draw the game interface
def draw_interface():
    screen.fill(BLACK)
    draw_text(f"Level: {current_level}", font, WHITE, screen, 10, 10)
    draw_text(f"Hints Remaining: {hints_remaining}", font, WHITE, screen, 10, 50)
    draw_text(f"Answer: {answer}", font, WHITE, screen, 10, 90)
    pygame.display.flip()

# Function to display the question
def display_question():
    global question_displayed
    if not question_displayed:
        draw_text(level_data[current_level]["question"], font, WHITE, screen, 10, 150)
        question_displayed = True
        pygame.display.flip()

# Function to check the player's answer
def check_answer():
    global answer
    return answer == level_data[current_level]["answer"]

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h and hints_remaining > 0:
                # Provide a hint (stub for now)
                hints_remaining -= 1
                print("Hint provided")
            elif event.key == pygame.K_RETURN:
                # Check the answer
                if check_answer():
                    current_level += 1
                    hints_remaining = 3
                    answer = ""
                    question_displayed = False
                    if current_level > max_level:
                        draw_text("Congratulations! You completed all levels.", font, GREEN, screen, 200, 300)
                        pygame.display.flip()
                        pygame.time.wait(5000)
                        running = False
                else:
                    answer = ""
            elif event.key == pygame.K_BACKSPACE:
                answer = answer[:-1]
            else:
                answer += event.unicode

    # Draw the game interface
    draw_interface()

    # Display the question
    if current_level <= max_level:
        display_question()

    # Cap the frame rate
    clock.tick(30)
