import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

rinning = True
while rinning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rinning = False
    pass

pygame.quit()
