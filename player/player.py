import pygame
from game_objects import GameObject
from frame_counter import FrameCounter
class Player(GameObject):
    # 1. Create constructor (properties)
    def __init__(self, x, y, input_manager):
        GameObject.__init__(self, x, y)
        self.input_manager = input_manager
        self.counter = FrameCounter(30)


    # 2. Describe action / method / behavior
    def update(self):
        GameObject.update(self)
        self.move()

    def move(self):
        self.dx = 0
        self.dy = 0

        if self.input_manager.right_pressed:
            self.dx += 3
        if self.input_manager.left_pressed:
            self.dx -= 3
        if self.input_manager.down_pressed:
            self.dy += 3
        if self.input_manager.up_pressed:
            self.dy -= 3

        self.x += self.dx
        self.y += self.dy