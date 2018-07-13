from game_objects import GameObject
from physics.box_collider import BoxCollider
from frame_counter import FrameCounter
from player.player import Player
from game_objects import collide_with, add as add_game_object
from player.player_captured import PlayerCaptured
from renderer.animation import Animation
from enemy.enemy_animator import EnemyAnimator
from renderer.image_renderer import ImageRenderer


class Enemy(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self, x, y)
        self.box_collider = BoxCollider(64, 64)
        self.renderer = EnemyAnimator()
        self.direct = True
        self.frame_counter = FrameCounter(120)
        self.black_screen = False
        self.counter = FrameCounter(120)
        self.dy = 0
        self.dx = 0

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
        if not self.black_screen:
            self.move()
        else:
            self.dy = 0

        collide_list = collide_with(self.box_collider, Player)
        for game_object in collide_list:
            game_object.deactivate()

    def move(self):
        self.dy = 0
        if self.direct:
            if self.y > 16:
                self.dy -= 8
            elif self.y == 16:
                self.direct = False
        else:
            if self.y < 624:
                self.dy += 8
            elif self.y == 624:
                self.direct = True

        self.y += self.dy
        self.x += self.dx

    def update_animator(self):
            self.renderer.update(self.dx, self.dy)
