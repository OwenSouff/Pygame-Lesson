import pygame
import os
import math
import random
pygame.font.init()
pygame.mixer.init()

WIDTH = 900
HEIGHT = 500
WINDOW =pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Fight")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

BORDER = pygame.Rect(WIDTH//2-5,0,10,HEIGHT)

BULLET_HIT_SOUND= pygame.mixer.Sound(os.path.join('Assets', 'explosion.wav'))
BULLET_FIRE_SOUND =pygame.mixer.Sound(os.path.join('Assets', 'Laser.wav'))

HEALTH_FONT = pygame.font.SysFont('arial', 40)
WINNER_FONT = pygame.font.SysFont('arial', 100)


FPS = 60
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 3
SPACESHIP_WIDTH = 80
SPACESHIP_HEIGHT = 60

METEOR_WIDTH, METEOR_HEIGHT = 50, 50

METEOR_VEL = 2
METEOR_1_DIR = random.randint(0, 359)
METEOR_2_DIR = random.randint(0, 359)
METEOR_3_DIR = random.randint(0, 359)
METEOR_1_X_VEL = math.cos(METEOR_1_DIR) * METEOR_VEL
METEOR_1_Y_VEL = math.sin(METEOR_1_DIR) * METEOR_VEL
METEOR_2_X_VEL = math.cos(METEOR_2_DIR) * METEOR_VEL
METEOR_2_Y_VEL = math.sin(METEOR_2_DIR) * METEOR_VEL
METEOR_3_X_VEL = math.cos(METEOR_3_DIR) * METEOR_VEL
METEOR_3_Y_VEL = math.sin(METEOR_3_DIR) * METEOR_VEL

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

METEOR_IMAGE = pygame.image.load(os.path.join('Assets', 'meteor.png'))
METEOR_1 = pygame.transform.rotate(pygame.transform.scale(
    METEOR_IMAGE, (METEOR_WIDTH, METEOR_HEIGHT)), 90)
METEOR_2 = pygame.transform.rotate(pygame.transform.scale(
    METEOR_IMAGE, (METEOR_WIDTH, METEOR_HEIGHT)), 90)
METEOR_3 = pygame.transform.rotate(pygame.transform.scale(
    METEOR_IMAGE, (METEOR_WIDTH, METEOR_HEIGHT)), 90)

SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))



def yellow_control(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > -15:
        yellow.x-=VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width - 15 < BORDER.x:
        yellow.x+=VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > -10:
        yellow.y-=VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height - 10 < HEIGHT:
        yellow.y+=VEL

def red_control(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL + 15 > BORDER.x + BORDER.width:
        red.x-=VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL +red.width - 15 < WIDTH:
        red.x+=VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > -10:
        red.y-=VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height - 10 < HEIGHT:
        red.y+=VEL

def drawWindow(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health, meteor_1, meteor_2, meteor_3):
    WINDOW.blit(SPACE, (0,0))
    #WINDOW.fill(WHITE)
    pygame.draw.rect(WINDOW, BLACK, BORDER)

    red_health_text = HEALTH_FONT.render("Health: "+str(red_health), True, WHITE)
    yellow_health_text = HEALTH_FONT.render("Health: "+str(yellow_health), True, WHITE)
    WINDOW.blit(red_health_text, (WIDTH-red_health_text.get_width(), -10, 10))
    WINDOW.blit(yellow_health_text,(10, 10))

    WINDOW.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WINDOW.blit(RED_SPACESHIP, (red.x, red.y))
    WINDOW.blit(METEOR_1, (meteor_1.x, meteor_1.y))
    WINDOW.blit(METEOR_2, (meteor_2.x, meteor_2.y))
    WINDOW.blit(METEOR_3, (meteor_3.x, meteor_3.y))

    for bullet in red_bullets:
        pygame.draw.rect(WINDOW, RED, bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(WINDOW, YELLOW, bullet)

    pygame.display.update()

def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    clock = pygame.time.Clock()
    run =True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        #yellow.x+=1
        keys_pressed = pygame.key.get_pressed()
        red_control(keys_pressed, red)
        yellow_control(keys_pressed, yellow)
        drawWindow(red, yellow)
    pygame.quit()

if __name__ == '__main__':
    main()

