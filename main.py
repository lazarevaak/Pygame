import pygame

class Ball():
    def __init__(self, pas):
        self.x = pas[0]
        self.y = pas[1]
        self.color = (255, 0, 0)
        self.r = 50
        self.step_x = 0
        self.step_y = 0

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
first_ball = Ball((100, 100))
first_ball.change_dir(1,1)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    first_ball.update()
    first_ball.move()
    if first_ball.x + first_ball.r == 800:
        first_ball.change_dir(-first_ball.step_x,first_ball.step_y)
    elif first_ball.x - first_ball.r == 0:
        first_ball.change_dir(-first_ball.step_x,first_ball.step_y)
    if first_ball.y + first_ball.r == 600:
        first_ball.change_dir(first_ball.step_x,-first_ball.step_y)
    elif first_ball.y - first_ball.r == 0:
        first_ball.change_dir(first_ball.step_x,-first_ball.step_y)




    clock.tick(FPS)
    pygame.display.flip()


pygame.quit()
