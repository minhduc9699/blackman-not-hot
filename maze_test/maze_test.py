import pygame
pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

gameDisplay = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Maze")

gameExit = False

lead_x = 20
lead_y = 20

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

gameDisplay.fill(white)
pygame.draw.rect(gameDisplay, black, [lead_x, lead_y, 20, 20])
pygame.display.update()

