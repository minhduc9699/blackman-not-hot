import pygame
from game_objects import GameObject
from frame_counter import FrameCounter
from physics.box_collider import BoxCollider
from game_objects import collide_with, add as add_game_object
from victory.player_escaped import PlayerEscaped


class Player(GameObject):
    def __init__(self, x, y, input_manager):
        GameObject.__init__(self, x, y)
        self.input_manager = input_manager
        self.counter = FrameCounter(30)
        self.box_collider = BoxCollider(32, 32)

    def update(self):
        GameObject.update(self)
        self.move()

        collide_list = collide_with(self.box_collider, Player)
        for game_object in collide_list:
            escape = PlayerEscaped(game_object.x, game_object.y)
            add_game_object(escape)

    def move(self):
        dx = 0
        dy = 0

        if self.input_manager.right_pressed:
            dx += 32
            self.input_manager.right_pressed = False
        elif self.input_manager.left_pressed:
            dx -= 32
            self.input_manager.left_pressed = False
        elif self.input_manager.down_pressed:
            dy += 32
            self.input_manager.down_pressed = False
        elif self.input_manager.up_pressed:
            dy -= 32
            self.input_manager.up_pressed = False
        self.x += dx
        self.y += dy




