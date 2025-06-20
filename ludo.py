import pygame
import sys

# Initialize pygame
pygame.init()

# Screen setup
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Ludo Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Game loop
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.rect(screen, RED, (100, 100, 100, 100))
    pygame.display.flip()

pygame.quit()
sys.exit()
