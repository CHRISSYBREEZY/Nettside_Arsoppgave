import pygame
import config
from game_state import GameState

from game import Game

pygame.init()

screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))

pygame.display.set_caption("Kubenmon")

clock = pygame.time.Clock()

game = Game(screen)
game.set_up()

# Denne skal hontere menyer
while game.game_state == GameState.RUNNING:
    clock.tick(50)
    game.update()
    pygame.display.flip()