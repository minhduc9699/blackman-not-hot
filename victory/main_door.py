from game_objects import GameObject
from renderer.image_renderer import ImageRenderer
from physics.box_collider import BoxCollider


class FinishLine(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self, x, y)
        self.renderer = ImageRenderer()
        self.box_collider = BoxCollider(32, 32)