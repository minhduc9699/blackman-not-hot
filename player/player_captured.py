from game_objects import GameObject
# from renderer.animation import Animation


class PlayerCaptured(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self, x, y)
        # self.renderer = Animation([])