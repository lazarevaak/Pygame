import pygame
FPS = 250
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.draw.circle(screen, (255, 0, 0), (100, 100), 50)
x, y = 100, 100
rinning = True
dir=1
while rinning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rinning = False
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 50)
    if x + 50 == 800 or x - 50 == 0:
        dir *= -1
    x += dir*1
    clock.tick(FPS)
    pygame.display.flip()
    pass

pygame.quit()
