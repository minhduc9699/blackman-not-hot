from game_objects import GameObject
from renderer.image_renderer import ImageRenderer
from physics.box_collider import BoxCollider
from player.player import Player
from game_objects import collide_with, add as add_game_object
from black_slave.black_slave import BlackSlave


class MainDoor(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self, x, y)
        self.renderer = ImageRenderer("image/enemy/enemy/enemy right1.png")
        self.box_collider = BoxCollider(32, 32)

    def update(self):
        GameObject.update(self)
        collide_list = collide_with(self.box_collider, Player)
        for game_object in collide_list:
            if game_object.win == True:
                game_object.deactivate()