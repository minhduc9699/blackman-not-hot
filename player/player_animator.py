from renderer.animation import Animation
from renderer.image_renderer import ImageRenderer


class PlayerAnimator:
    def __init__(self):
        self.right_animation = Animation(["image/enemy/enemy/enemy right1.png",
                                          "image/enemy/enemy/enemy right2.png",
                                          "image/enemy/enemy/enemy right3.png"],
                                         loop=True)
        self.left_animation = Animation(["image/enemy/enemy/enemy right (1).png",
                                         "image/enemy/enemy/enemy right (2).png",
                                         "image/enemy/enemy/enemy right (3).png"],
                                        loop=True)
        self.up_animation = Animation(["image/enemy/enemy/enemy up (1).png",
                                       "image/enemy/enemy/enemy up (2).png",
                                       "image/enemy/enemy/enemy up (3).png"],
                                      loop=True)
        self.down_animation = Animation(["image/enemy/enemy/enemy down1.png",
                                         "image/enemy/enemy/enemy down2.png",
                                         "image/enemy/enemy/enemy down3.png"],
                                        loop=True)
        self.stand = ImageRenderer("image/enemy/enemy/enemy right1.png")
        self.current_animation = self.stand

    def render(self, canvas, x, y):
        self.current_animation.render(canvas, x, y)

    def update(self, player_dx, player_dy):
        if player_dx < 0:
            self.current_animation = self.left_animation
        elif player_dx > 0:
            self.current_animation = self.right_animation
        elif player_dy > 0:
            self.current_animation = self.down_animation
        elif player_dy < 0:
            self.current_animation = self.up_animation
        else:
            self.current_animation = self.stand


