from renderer.animation import Animation


class PlayerAnimator:
    def __init__(self):
        self.right_animation = Animation([])
        self.left_animation = Animation([])
        self.up_animation = Animation([])
        self.down_animation = Animation([])
        self.current_animation = self.up_animation

    def render(self, canvas, x, y):
        self.current_animation.render(canvas, x, y)

    def update(self, player_dx, player_dy):
        if player_dx < 0:
            self.current_animation = self.left_animation
        elif player_dx > 0:
            self.current_animation = self.right_animation
        elif player_dy > 0:
            self.current_animation = self.down_animation
        else:
            self.current_animation = self.up_animation
