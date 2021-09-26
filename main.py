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


VELOCITY = 10
SNAKE_WIDTH = 15
APPLE_SIZE = 20
TOP_WIDTH = 40
small_font = pygame.font.SysFont('forte', 25)
medium_font = pygame.font.SysFont('showcard gothic', 30, True)
large_font = pygame.font.SysFont('chiller', 60, True, True)
clock = pygame.time.Clock()

canvas = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('SNAKE GAME')


#images for items
snake_img = pygame.image.load('snake2.png')
apple_img = pygame.image.load('apple2.png')
tail_img = pygame.image.load('tail22.png')
apple_img_rect = apple_img.get_rect()

#music for background,crash and eat
pygame.mixer.music.load('gamesound23.mp3')

pygame.mixer.music.play(1)



