from game_objects import GameObject
from physics.box_collider import BoxCollider
from player.player import Player
from game_objects import collide_with, add as add_game_object
from player.player_captured import PlayerCaptured
from renderer.animation import Animation


class Enemy(GameObject):
    def __init__(self, x, y, input_manager):
        GameObject.__init__(self, x, y)
        self.box_collider = BoxCollider(32, 32)
        self.input_manager = input_manager
        self.renderer = Animation([])

    def update(self):
        GameObject.update(self)
        self.move()

        collide_list = collide_with(self.box_collider, Player)
        for game_object in collide_list:
            capture = PlayerCaptured(game_object.x, game_object.y)
            add_game_object(capture)
            game_object.deactivate()
            self.deactivate()

    def move(self):
        pass