import pygame

# CONSTANTS
DEATH = pygame.USEREVENT + 4            # called when the player dies
RESTART = pygame.USEREVENT + 2          # called when the stage restarts
WIN = pygame.USEREVENT + 3              # called when the player touches a cave (and wins)