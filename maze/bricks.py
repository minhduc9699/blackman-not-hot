import pygame
bricks = []


def add(brick):
    bricks.append(brick)


def update():
    for brick in bricks:
        if brick.need:
            brick.update()


def render(canvas):
    for brick in bricks:
        if brick.need:
            brick.render(canvas)


class Brick:
    def __init__(self, width=32, height=32, x=16, y=16):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.need = True

    def render(self, canvas):
        self.x = 16
        BLACK = (0, 0, 0)
        rect = (self.x - self.width/2, self.y - self.height/2, self.width, self.height)
        pygame.draw.rect(canvas, BLACK, rect, 1)




