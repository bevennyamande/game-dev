#! /root/werkzeug/projects/game-dev/venv/bin/python3

import pygame

pygame.init()

screen_height = 192   # width of the screen
screen_width = 320    # height of the screen

# Create the window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Immortal Engines Platformer')


# Load Assets
bg_image = pygame.image.load('assets/Background/BG1.png').convert_alpha()
bg_image2 = pygame.image.load('assets/Background/BG3.png').convert_alpha()

def draw_background():
    screen.blit(bg_image, (0,0))

def draw_background2():
    screen.blit(bg_image2, (0,0))

# Game Loop
run = True
while run:

    draw_background()
    draw_background2()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
    pygame.display.update()

