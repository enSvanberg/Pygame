import pygame
import math

pygame.init()

# start
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player = pygame.Rect((300, 250, 50, 50))
running = True

speed = 1

while running:

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255, 0, 0), player)

    key = pygame.key.get_pressed()
    
    move_x = 0
    move_y = 0
    
    if key[pygame.K_a]:
        move_x = -1
    if key[pygame.K_d]:
        move_x = 1
    if key[pygame.K_w]:
        move_y = -1
    if key[pygame.K_s]:
        move_y = 1
    
    player.move_ip(move_x * speed, move_y * speed)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
