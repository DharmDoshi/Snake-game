import pygame
import random
import time
import math
pygame.init()
clock = pygame.time.Clock()

green_color = (0, 255, 0)
red_color = (255, 0, 0)
white_color = (255, 255, 255)

# Display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake")

# Snake
snake_block = 15
snake_speed = 15
snake_list = []

# Score
score = 0
font = pygame.font.SysFont("arial", 27 )
text_x = 10
text_y = 10

# Game over
gameover_font = pygame.font.SysFont("arial", 70)

def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, green_color, [x[0], x[1], snake_block, snake_block])

def show_score(x, y):
    score_value = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_value, (x, y))

def gameover_txt():
    food_x = 2000
    snake_x = 2000
    text_x = 2000
    over_txt = gameover_font.render("GAME OVER", True, (255, 255, 255))
    score_value = font.render("Your score is " + str(score), True, (255, 255, 255))
    screen.blit(score_value, (330, 230))
    screen.blit(over_txt, (230, 150))

def collision(food_x, food_y, snake_x, snake_y):
    distance = math.sqrt((food_x - snake_x)**2 + (food_y - snake_y)**2)
    if distance < 20:
        return True
    else:
        return False

# Snake coordinates
snake_x = screen_width / 2
snake_y = screen_height / 2
x_dx = 0
y_dy = 0
snake_list = []
length_snake = 1

# Food
food_x = round(random.randrange(50, screen_width - snake_block) / 10.0) * 10.0
food_y = round(random.randrange(50, screen_height - snake_block) / 10.0) * 10.0

# Main loop
game_running = True
game_over = False

while not game_over:
    while game_running == False:
        gameover_txt()
        food_y = 2000
        snake_y = 2000
        text_x = 2000
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = True
                game_over = True

    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

        # Snake movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_dx = -snake_block
                y_dy = 0
            if event.key == pygame.K_RIGHT:
                x_dx = snake_block
                y_dy = 0
            if event.key == pygame.K_UP:
                x_dx = 0
                y_dy = -snake_block
            if event.key == pygame.K_DOWN:
                x_dx = 0
                y_dy = snake_block

    # Boundary condition
    if snake_x < 0:
        snake_x = 800

    if snake_x > screen_width:
        snake_x = 0

    if snake_y < 0:
        snake_y = 600

    if snake_y > screen_height:
        snake_y = 0

    # Movement of snake
    snake_x += x_dx
    snake_y += y_dy

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, red_color, [food_x, food_y, snake_block, snake_block])

    snake_head = []
    snake_head.append(snake_x)
    snake_head.append(snake_y)
    snake_list.append(snake_head)

    # Ways to end game
    if len(snake_list) > length_snake:
        del snake_list[0]

    for x in snake_list[:-1]:
        if x == snake_head:
            food_x = 2000
            text_x = 2000
            snake_x = 2000
            game_running = False

    # If snake eats food length should increase
    in_collision = collision(food_x, food_y, snake_x, snake_y)
    if in_collision:
        food_x = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
        food_y = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
        length_snake += 1
        score += 1

    clock.tick(snake_speed)
    snake(snake_block, snake_list)
    show_score(text_x, text_y)
    pygame.display.update()
