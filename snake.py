import pygame
import random

pygame.init()
width = 600
snake = []
height = 600
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)
pygame.display.set_caption('Snake')
screen = pygame.display.set_mode((width, height), 0, 32)
clock = pygame.time.Clock()


class Snake:
    xVelocity = 1
    yVelocity = 0
    dir = 'E'

    @staticmethod
    def move():
        x = snake[len(snake) - 1].x + Snake.xVelocity
        y = snake[len(snake) - 1].y + Snake.yVelocity
        if x == 0:
            x = 600
        elif x == 600:
            x = 0
        elif y == 600:
            y = 0
        elif y == 0:
            y = 600
        s = Snake(x, y)
        snake.pop(0)
        snake.append(s)

    @staticmethod
    def draw():
        for i in range(len(snake)):
            if i == len(snake) - 1:
                pygame.draw.rect(screen, red, pygame.Rect(snake[i].x, snake[i].y, 10, 10))
            else:
                pygame.draw.rect(screen, white, pygame.Rect(snake[i].x, snake[i].y, 10, 10))

    @staticmethod
    def grow():
        x = snake[len(snake) - 1].x + Snake.xVelocity
        y = snake[len(snake) - 1].y + Snake.yVelocity
        s = Snake(x, y)
        snake.append(s)

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Fruit:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(screen, white, pygame.Rect(self.x, self.y, 10, 10))


def main():
    timer = 0
    s = Snake(width / 2, height / 2)
    x = random.randint(0, 600)
    y = random.randint(0, 600)
    fruit = Fruit(x, y)
    snake.append(s)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and Snake.dir != 'S':
                    Snake.xVelocity = 0
                    Snake.yVelocity = -1
                    Snake.dir = 'N'
                elif event.key == pygame.K_a and Snake.dir != 'E':
                    Snake.xVelocity = -1
                    Snake.yVelocity = 0
                    Snake.dir = 'W'
                elif event.key == pygame.K_s and Snake.dir != 'N':
                    Snake.xVelocity = 0
                    Snake.yVelocity = 1
                    Snake.dir = 'S'
                elif event.key == pygame.K_d and Snake.dir != 'W':
                    Snake.xVelocity = 1
                    Snake.yVelocity = 0
                    Snake.dir = 'E'
        screen.fill(black)
        fruit.draw()
        Snake.draw()
        Snake.move()
        timer += 1
        if timer == 500 or collision(fruit):
            x = random.randint(0, 600)
            y = random.randint(0, 600)
            fruit = Fruit(x, y)
            timer = 0
            Snake.grow()
        clock.tick(160)
        pygame.display.update()


def collision(fruit):
    head = snake[len(snake) - 1]
    if head.y + 10 >= fruit.y and head.y <= fruit.y + 10:
        if head.x >= fruit.x and head.x <= fruit.x + 10:
            return True
    if head.y >= fruit.y and head.y <= fruit.y + 10:
        if head.x >= fruit.x and head.x <= fruit.x + 10:
            return True
    if head.x + 10 >= fruit.x and head.x <= fruit.x + 10:
        if head.y >= fruit.y and head.y <= fruit.y + 10:
            return True
    if head.x >= fruit.x and head.x <= fruit.x + 10:
        if head.y >= fruit.y and head.y <= fruit.y + 10:
            return True
    return False


if __name__ == '__main__':
    main()


