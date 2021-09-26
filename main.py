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
def start_game():
    canvas.fill(BLACK)
    canvas.blit(bc,(0,0))
    start_font1 = large_font.render("Welcome To Snake Game", True,BLUE,RED)
    start_font2 = medium_font.render("PlAY GAME", True, RED, YELLOW)
    start_font3 = medium_font.render("RULES", True, RED, YELLOW)
    start_font4 = medium_font.render("Quit", True, RED, YELLOW)
    start_font5 = medium_font.render("Creator", True, RED, YELLOW)
    start_font1_rect = start_font1.get_rect()
    start_font2_rect = start_font2.get_rect()
    start_font3_rect = start_font3.get_rect()
    start_font4_rect = start_font4.get_rect()
    start_font5_rect = start_font5.get_rect()

    start_font1_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2 - 200)
    start_font2_rect.center = (WINDOW_WIDTH/2 + 100, WINDOW_HEIGHT/2 + 50)
    start_font3_rect.center = (WINDOW_WIDTH/2 + 100, WINDOW_HEIGHT / 2 + 100)
    start_font5_rect.center = (WINDOW_WIDTH/2 + 100, WINDOW_HEIGHT / 2 + 150)
    start_font4_rect.center = (WINDOW_WIDTH/2 + 100, WINDOW_HEIGHT/2 + 200)

    canvas.blit(start_font1, start_font1_rect)
    canvas.blit(start_font2, start_font2_rect)
    canvas.blit(start_font3, start_font3_rect)
    canvas.blit(start_font4, start_font4_rect)
    canvas.blit(start_font5, start_font5_rect)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    gameloop()
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x > start_font3_rect.left and x < start_font3_rect.right:
                    if y > start_font3_rect.top and y < start_font3_rect.bottom:
                        start_inst(start_font1, start_font1_rect)
                if x > start_font2_rect.left and x < start_font2_rect.right:
                    if y > start_font2_rect.top and y < start_font2_rect.bottom:
                        gameloop()
                if x > start_font5_rect.left and x < start_font5_rect.right:
                    if y > start_font5_rect.top and y < start_font5_rect.bottom:
                        creator()
                if x > start_font4_rect.left and x < start_font4_rect.right:
                    if y > start_font4_rect.top and y < start_font4_rect.bottom:
                        pygame.quit()
                        sys.exit()



        pygame.display.update()

 def creator():
            canvas.fill(BLACK)
            my_img = pygame.image.load('image2.jpg')
            my_img_rect = my_img.get_rect()
            my_img_rect.center = (WINDOW_WIDTH / 2, my_img_rect.height / 2 + 20)
            canvas.blit(my_img, my_img_rect)

            start_inst1 = large_font.render("Aaditya Narayan Thakur", False, GREEN)
            start_inst1_rect = start_inst1.get_rect()
            start_inst1_rect.center = (WINDOW_WIDTH / 2, 420)
            canvas.blit(start_inst1, start_inst1_rect)

            start_inst2 = small_font.render("Hello Guys,It's myself Aaditya Narayan Thakur.", True, RED)
            start_inst3 = small_font.render("My student id is 210262.", True, BLUE)
            start_inst4 = small_font.render("This is a very simple game, developed using by python", True, GREEN)
            start_inst5 = small_font.render("Thanks for playing ", True, YELLOW)

            canvas.blit(start_inst2, (10, 500))
            canvas.blit(start_inst3, (10, 530))
            canvas.blit(start_inst4, (10, 560))
            canvas.blit(start_inst5, (10, 590))


            start_inst5 = medium_font.render("<<BACK", True, RED, YELLOW)
            start_inst5_rect = start_inst5.get_rect()
            start_inst5_rect.center = (
            WINDOW_WIDTH - start_inst5_rect.width / 2, WINDOW_HEIGHT - start_inst5_rect.height / 2)
            canvas.blit(start_inst5, start_inst5_rect)
            pygame.display.update()

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = event.pos
                        if x > start_inst5_rect.left and x < start_inst5_rect.right:
                            if y > start_inst5_rect.top and y < start_inst5_rect.bottom:
                                start_game()
                pygame.display.update()

def start_inst(start_font1, start_font1_rect):
      canvas.fill(BLACK)
      canvas.blit(bd, (0, 0))
      canvas.blit(start_font1, start_font1_rect)
      start_inst1 = small_font.render("--> Do not cross the edges, else you will be dead", True, YELLOW)
      start_inst2 = small_font.render("--> Keep eating the red apples", True, RED)
      start_inst3 = small_font.render("--> Do not cross over yourself", True, GREEN)
      start_inst4 = small_font.render("--> Provide your Feedback......", True, BLUE)
      start_inst5 = medium_font.render("<<BACK", True, RED, YELLOW)
      start_inst5_rect = start_inst5.get_rect()
      start_inst5_rect.center = (WINDOW_WIDTH - 100, WINDOW_HEIGHT - 100)

      canvas.blit(start_inst1, (WINDOW_WIDTH / 8, WINDOW_HEIGHT / 2))
      canvas.blit(start_inst2, (WINDOW_WIDTH / 8, WINDOW_HEIGHT / 2 + 30))
      canvas.blit(start_inst3, (WINDOW_WIDTH / 8, WINDOW_HEIGHT / 2 + 60))
      canvas.blit(start_inst4, (WINDOW_WIDTH / 8, WINDOW_HEIGHT / 2 + 90))
      canvas.blit(start_inst5, start_inst5_rect)
      pygame.display.update()
      while True:
          for event in pygame.event.get():
              if event.type == pygame.QUIT:
                  pygame.quit()
                  sys.exit()
              if event.type == pygame.MOUSEBUTTONDOWN:
                 x, y = event.pos
                 if x > start_inst5_rect.left and x < start_inst5_rect.right:
                    if y > start_inst5_rect.top and y < start_inst5_rect.bottom:
                        start_game()
          pygame.display.update()

def gameover():
              # canvas.fill(BLACK)

              font_gameover1 = large_font.render('GAME OVER', True, GREEN)
              font_gameover2 = medium_font.render("Play Again", True, RED, YELLOW)
              font_gameover3 = medium_font.render("Quit", True, RED, YELLOW)

              font_gameover1_rect = font_gameover1.get_rect()
              font_gameover2_rect = font_gameover2.get_rect()
              font_gameover3_rect = font_gameover3.get_rect()

              font_gameover1_rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 - 100)
              font_gameover2_rect.center = (WINDOW_WIDTH / 2 + 150, WINDOW_HEIGHT / 2 + 20)
              font_gameover3_rect.center = (WINDOW_WIDTH / 2 + 150, WINDOW_HEIGHT / 2 + 70)

              canvas.blit(font_gameover1, font_gameover1_rect)
              canvas.blit(font_gameover2, font_gameover2_rect)
              canvas.blit(font_gameover3, font_gameover3_rect)
              pygame.display.update()

              while True:
                  for event in pygame.event.get():
                      if event.type == pygame.QUIT:
                          pygame.quit()
                          sys.exit()
                      if event.type == pygame.MOUSEBUTTONDOWN:
                          x, y = event.pos
                          if x > font_gameover2_rect.left and x < font_gameover2_rect.right:
                              if y > font_gameover2_rect.top and y < font_gameover2_rect.bottom:
                                  gameloop()
                          if x > font_gameover3_rect.left and x < font_gameover3_rect.right:
                              if y > font_gameover3_rect.top and y < font_gameover3_rect.bottom:
                                  pygame.quit()
                                  sys.exit()

                  pygame.display.update()


def snake(snakelist, direction):

    if direction == 'right':
        head = pygame.transform.rotate(snake_img, 270)
        tail = pygame.transform.rotate(tail_img, 270)
    if direction == 'left':
        head = pygame.transform.rotate(snake_img, 90)
        tail = pygame.transform.rotate(tail_img, 90)
    if direction == 'up':
        head = pygame.transform.rotate(snake_img, 0)
        tail = pygame.transform.rotate(tail_img, 0)
    if direction == 'down':
        head = pygame.transform.rotate(snake_img, 180)
        tail = pygame.transform.rotate(tail_img, 180)

    canvas.blit(head, snakelist[-1])
    canvas.blit(tail, snakelist[0])

    for XnY in snakelist[1:-1]:
        pygame.draw.rect(canvas, BLUE, (XnY[0], XnY[1], SNAKE_WIDTH, SNAKE_WIDTH))








