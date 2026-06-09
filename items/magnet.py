# items/magnet.py
"""Magnet powerup. While active, falling items drift toward the basket."""

import pygame
from .base import FallingItem


class Magnet(FallingItem):
    radius = 13
    color = (220, 60, 60)
    base_fall_speed = 4

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
        pygame.draw.circle(surface, (40, 40, 40), (self.x, self.y), self.radius // 2)

    def on_collect(self, game):
        game.magnet_until = pygame.time.get_ticks() + 5000
        super().on_collect(game)
