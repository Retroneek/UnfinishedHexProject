import pygame
import sys

# Initialize pygame
pygame.init()

# Create a screen
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Retroneek's Hex Project")
# Game Assets
playerYOU = pygame.image.load('Assets/player.png')
playerX = 400
playerY = 400
gameframes = 60
gameAngle = 0
playerX_change = 0

def player():
    screen.blit(playerYOU, (playerX, playerY))

# Game Loop
while True:
    screen.fill((0, 0, 0))
    clock = pygame.time.Clock()
    clock.tick(gameframes)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1
            if event.key == pygame.K_RIGHT:
                playerX_change = +1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    playerX += playerX_change
    player()
    pygame.display.update()


## Q: how do I draw the player
## A: 
