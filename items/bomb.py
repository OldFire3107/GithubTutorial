"""A bomb. Catching one subtracts 5 points."""

import pygame
from .base import FallingItem


class Bomb(FallingItem):
    radius = 14
    color = (40, 40, 40)
    fall_speed = 6

    def __init__(self, x, y):
        super().__init__(x, y)
        # extra per-bomb state could go here (e.g. a flicker counter)
        self.flash = 0

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
        # red fuse spark
        pygame.draw.circle(surface, (240, 80, 40), (self.x, self.y - self.radius - 3), 3)

    def on_caught(self, game):
        game.score -= 5
        super().on_caught(game)