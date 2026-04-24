import pygame
import sys
from jh_name import JH
pygame.init()

WIDTH, HEIGHT = 800,600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("方向键控制方块")

WHITE = (255,255,255)
RED = (255,0,0)

box_x = WIDTH //2
box_y = HEIGHT //2
box_size = 50
speed = 1

clock = pygame.time.Clock()

#创建火箭实例
jh = JH(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        jh.rect.x -= 1
    if keys[pygame.K_RIGHT]:
        jh.rect.x += 1
    if keys[pygame.K_UP]:
        jh.rect.y -= 1
    if keys[pygame.K_DOWN]:
        jh.rect.y += 1

                #边界限制
    jh.rect.x = max(0, min(jh.rect.x, WIDTH - jh.rect.width))
    jh.rect.y = max(0, min(jh.rect.y, HEIGHT - jh.rect.height))

   

    screen.fill(WHITE)
    jh.blitme()
    pygame.display.flip()