import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((600, 600))
screen.fill((255, 255, 255))
pygame.draw.line(screen, (255, 0, 0), (200, 0), (200, 600), 1)
pygame.draw.line(screen, (255, 0, 0), (400, 0), (400, 600), 1)
pygame.draw.line(screen, (255, 0, 0), (0, 200), (600, 200), 1)
pygame.draw.line(screen, (255, 0, 0), (0, 400), (600, 400), 1)
pygame.display.update()

step = 1
pole = [0, 0, 0, 0, 0, 0, 0, 0, 0]


def do_step(pole_index, step, left_top_corner, right_down_corner):
    if pole[pole_index] != 0:
        return step
    pole[pole_index] = step + 1
    if step == 1:
        pygame.draw.line(screen, (0, 0, 255), left_top_corner, right_down_corner)
        pygame.draw.line(screen, (0, 0, 255),
                         (right_down_corner[0], left_top_corner[1]),
                         (left_top_corner[0], right_down_corner[1]))
    else:
        pygame.draw.circle(screen, (0, 0, 255), (left_top_corner[0] + 100, left_top_corner[1] + 100), 100, 3)
    return 1 - step


def calculate_pole_index(pos):
    return pos[0] // 200 + pos[1] // 200 * 3


def calculate_left_top_corner(pos):
    return pos[0] - pos[0] % 200, pos[1] - pos[1] % 200 


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            left_top_corner = calculate_left_top_corner(event.pos)
            do_step(calculate_pole_index(event.pos), step,)

            pygame.display.update()
        # elif event.type == pygame.MOUSEBUTTONUP:
