import pygame
import random


class Ball():
    def __init__(self):
        self.x = random.randint(100, 500)
        self.y = random.randint(100, 500)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.r = 50
        self.step_x = random.randint(-5, 5)
        self.step_y = random.randint(-5, 5)

    def move(self):
        self.x += self.step_x
        self.y += self.step_y

    def change_dir(self, x, y):
        self.step_x = x
        self.step_y = y

    def update(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)


FPS = 250
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((800, 600))
running = True
list_ball = [Ball() for i in range(10)]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    for bal in list_ball:
        bal.update()
        bal.move()
        if bal.x + bal.r >= 800:
            bal.change_dir(-bal.step_x, bal.step_y)
        elif bal.x - bal.r <= 0:
            bal.change_dir(-bal.step_x, bal.step_y)
        if bal.y + bal.r >= 600:
            bal.change_dir(bal.step_x, -bal.step_y)
        elif bal.y - bal.r <= 0:
            bal.change_dir(bal.step_x, -bal.step_y)

    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()
