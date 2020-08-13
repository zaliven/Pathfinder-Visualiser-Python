import pygame
import math
from spot import Spot, WHITE, GRAY
from argparser import get_cli_args
from Game import Game

WIDTH = 400
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Path Finding Algorithm Visualizer")


def main(win, width):
    args = get_cli_args()
    rows = int(args.rows)
    algorithmChoice = args.algorithm
    game = Game(pygame, win, width, rows, algorithmChoice)
    run = True

    game.draw()

    while run:
        game.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = game.get_clicked_pos(pos)
                spot = game.grid[row][col]
                if not game.start and spot != game.end:
                    game.start = spot
                    game.start.make_start()
                elif not game.end and spot != game.start:
                    game.end = spot
                    game.end.make_end()
                elif spot != game.end and spot != game.start:
                    spot.make_barrier()

            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = game.get_clicked_pos(pos)
                spot = game.grid[row][col]
                spot.reset()
                if spot == game.start:
                    game.start = None
                elif spot == game.end:
                    game.end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game.start and game.end:
                    for row in game.grid:
                        for spot in row:
                            spot.update_neighbors(game.grid)
                    game.algorithm()

                if event.key == pygame.K_c:
                    game.start = None
                    game.end = None
                    game.make_grid()
    pygame.quit()


main(WIN, WIDTH)
