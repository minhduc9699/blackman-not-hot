import pygame
from input.input_manager import InputManager
from player.player import Player
from frame_counter import FrameCounter
import game_objects
from enemy.enemy import Enemy
# from maze.bricks import Brick
from black_screen import BlackScreen
from black_slave.black_slave import BlackSlave
from victory.main_door import MainDoor

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

player = Player(64, 320, input_manager)
enemy = Enemy(400, 608)
enemy1 = Enemy(640, 400)

black_slave = BlackSlave(768, 240)
black_screen = BlackScreen(0, 0)
main_door = MainDoor(16, 320)

game_objects.add(enemy)
game_objects.add(black_slave)
game_objects.add(main_door)
game_objects.add(enemy1)
game_objects.add(black_screen)
game_objects.add(player)

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

    pygame.display.set_caption('Micro game')

    # 3. Flip
    pygame.display.flip()
    clock.tick(60)