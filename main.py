import pygame
from fighter import Fighter

pygame.init()

# create game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('DebikFight')

#set framerate
clock = pygame.time.Clock()
FPS = 60

#define colours
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

#load bacground(BG) image
bg_image = pygame.image.load('assets/images/background/test_map.jpg').convert_alpha()

#BG drawing func
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))

#func for drawing fighter health bars
def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, WHITE, (x - 2, y - 2, 404, 34))
    pygame.draw.rect(screen, RED, (x, y, 400, 30))
    pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))

#create two instances of fighters
fighter_1 = Fighter(200, 310)
fighter_2 = Fighter(700, 310)

#game loop
run = True
while run:

    clock.tick(FPS)

    #draw BG
    draw_bg()

    #show player stats
    draw_health_bar(fighter_1.health, 20, 20)
    draw_health_bar(fighter_2.health, 580, 20)

    #move fighters
    fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2)

    #draw fighters
    fighter_1.draw(screen)
    fighter_2.draw(screen)

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    #update display
    pygame.display.update()

#exit pygame
pygame.quit()