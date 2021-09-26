#includes pause
import pygame
import sys
import random

pygame.init()
FPS = 30
#colours

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# creating windows

WINDOW_WIDTH = 700
WINDOW_HEIGHT = 700
# background image
ad = pygame.image.load("background2.jpg")
bd = pygame.image.load("back3.jpg")
bc = pygame.image.load("snakes.jpg")

ad = pygame.transform.scale(ad,(WINDOW_WIDTH,WINDOW_HEIGHT))
bd= pygame.transform.scale(bd,(WINDOW_WIDTH,WINDOW_HEIGHT))
bc = pygame.transform.scale(bc,(WINDOW_WIDTH,WINDOW_HEIGHT))



