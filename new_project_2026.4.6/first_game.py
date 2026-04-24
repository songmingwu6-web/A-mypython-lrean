import pygame
import sys
from man import Man
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("方向键控制方块")

WHITE = (255, 255, 255)
RED = (200, 50, 50)

box_x = WIDTH // 2
box_y = HEIGHT // 2
box_size = 50
speed = 1

clock = pygame.time.Clock()

# 创建小人实例
man = Man(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        man.rect.x -= 1
    if keys[pygame.K_RIGHT]:
        man.rect.x += 1
    if keys[pygame.K_UP]:
        man.rect.y -= 1
    if keys[pygame.K_DOWN]:
        man.rect.y += 5

    # 边界限制
    man.rect.x = max(0, min(WIDTH - man.rect.width, man.rect.x))
    man.rect.y = max(0, min(HEIGHT - man.rect.height, man.rect.y))

    screen.fill(WHITE)
    man.blitme()  # 画小人
    pygame.display.flip()