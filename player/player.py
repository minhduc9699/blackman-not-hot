import pygame
from game_objects import GameObject
from frame_counter import FrameCounter
from physics.box_collider import BoxCollider
from game_objects import collide_with, add as add_game_object
# from victory.player_escaped import PlayerEscaped
from player.player_animator import PlayerAnimator
# from black_slave.prison_break import PrisonBreak


class Player(GameObject):
    def __init__(self, x, y, input_manager):
        GameObject.__init__(self, x, y)
        self.input_manager = input_manager
        self.box_collider = BoxCollider(64, 64)
        self.renderer = PlayerAnimator()
        self.frame_counter = FrameCounter(120)
        self.counter = FrameCounter(120)
        self.black_screen = False
        self.dx = 0
        self.dy = 0
        self.win = False

    def update(self):
        GameObject.update(self)
        self.update_animator()
        self.frame_counter.run()
        if self.frame_counter.expired:
            self.black_screen = True
            self.counter.run()
            if self.counter.expired:
                self.black_screen = False
                self.counter.reset()
                self.frame_counter.reset()
        if self.black_screen:
            self.move()
        else:
            self.dy = 0
            self.dx = 0

        # collide_list = collide_with(self.box_collider, BlackSlave)
        # for game_object in collide_list:
        #     game_object.deactivate()
        #     self.win = True

    # if self.win:
    #     collide_list1 = collide_with(self.box_collider, MainDoor)
    #     for game_object in collide_list1:
    #         # self.deactivate()
    #         pass
    #     print("aaaa")

    def update_animator(self):
        self.renderer.update(self.dx, self.dy)

    def move(self):
        self.dx = 0
        self.dy = 0
        if self.x == 768:
            self.input_manager.right_pressed = False
        if self.x == 32:
            self.input_manager.left_pressed = False
        if self.y == 602:
            self.input_manager.down_pressed = False
        if self.y == 32:
            self.input_manager.up_pressed = False

        if self.input_manager.right_pressed:
            self.dx += 8

        elif self.input_manager.left_pressed:
            self.dx -= 8

        elif self.input_manager.down_pressed:
            self.dy += 8

        elif self.input_manager.up_pressed:
            self.dy -= 8

        self.x += self.dx
        self.y += self.dy




