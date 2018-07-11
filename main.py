import pygame
from input.input_manager import InputManager
from player.player import Player
from frame_counter import FrameCounter
import game_objects
from enemy.enemy import Enemy
from maze.bricks import Brick
from victory.main_door import FinishLine

BG = (255, 255, 0)
WHITE = (255, 255, 255)

# 1. Init pygame
pygame.init()

# 2. Set screen
SIZE = (800, 640)
canvas = pygame.display.set_mode(SIZE)

# 3. Clock
clock = pygame.time.Clock()

loop = True

input_manager = InputManager()

player = Player(16, 16, input_manager)
enemy = Enemy(784, 624, input_manager)
finish_line = FinishLine(400, 320)
bricks = Brick()


game_objects.add(player)
game_objects.add(enemy)
game_objects.add(finish_line)

while loop:
    # 1. Event processing
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            loop = False
        else:
            input_manager.update(event)

    game_objects.update()

    # 2. Draw
    canvas.fill(WHITE)

    game_objects.render(canvas)
    bricks.render(canvas)

    pygame.display.set_caption('Micro game')

    # 3. Flip
    pygame.display.flip()
    clock.tick(60)