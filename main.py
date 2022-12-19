#импорт библиотек
import pygame
from pygame.draw import *
from random import randint
from box import Box
from ball import Ball


pygame.init()

# установка констант
SIZE = (600, 400)
RED = (200,0,0)
FPS = 60
ph=["images/фон1.jpg","images/фон2.jpg","images/фон3.jpg","images/фон4.jpg","images/фон5.jpg","images/фон6.jpg"]
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Баскетбольчик')

def load_ph(i):
    ph_surf = pygame.image.load(ph[i])
    ph_surf = pygame.transform.scale(ph_surf, (600, 400))
    ph_rect = ph_surf.get_rect(center=(300, 200))
    return ph_surf, ph_rect

# шрифт счетчика
f = pygame.font.SysFont("arial", 50)

# экран
def print_scene(i):
    '''
    '''
    screen.blit(*load_ph(i))
    rect(screen, RED,(0,80,60,20))
    rect(screen, RED,(0,200,60,20))
    rect(screen, RED,(540,80,60,20))
    rect(screen, RED,(540,200,60,20))
    polygon(screen,RED,[(60,80),(150,150),(150,170),(60,100)])
    polygon(screen,RED,[(540,80),(450,150),(450,170),(540,100)])
    polygon(screen,RED,[(60,200),(150,270),(150,290),(60,220)])
    polygon(screen,RED,[(540,200),(450,270),(450,290),(540,220)])


clock = pygame.time.Clock()
box = Box((-100, -100), (150, 150), screen)
ball = Ball((-100, -100), (50, 50), screen)

print_scene(0)

# основной цикл
counter = 0
score = 0
speed = 1
CP = 0
while True:
    if counter == 0:
        pos = randint(0, 3)
    elif counter == (220 // speed) * speed - speed:
        if pos == Box.POSITIONS.index(box.position):
            score += 1
            if speed < 5 and score % 5 == 4:
                speed += 1
        else:
            score = 0
            speed = 1
    counter = counter + speed if counter + speed < 220 else 0
    ball.move(Ball.POSITIONS[pos][counter // 20])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                CP %= 2
            if event.key == pygame.K_RIGHT:
                CP = CP // 2 * 2 + 1
            if event.key == pygame.K_LEFT:
                CP = CP // 2 * 2
            if event.key == pygame.K_DOWN:
                CP = 2 + CP % 2
            box.move(Box.POSITIONS[CP])
            print(CP)

                
    print_scene((score // 5) % len(ph))
    ball.print()
    box.print()
    text = f.render(f"{score}", 0, (0, 0, 0))
    text_pos = text.get_rect(center=(SIZE[0]//2, SIZE[1]//2))
    screen.blit(text, text_pos)
    pygame.display.update()
    clock.tick(FPS)