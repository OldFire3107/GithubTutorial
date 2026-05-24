"""The player-controlled basket. Moves left/right with arrow keys (or A/D)."""

import pygame

from config import (
    BASKET_COLOR,
    BASKET_HEIGHT,
    BASKET_SPEED,
    BASKET_WIDTH,
    BASKET_Y_OFFSET,
    HEIGHT,
    WIDTH,
)


class Basket:
    def __init__(self):
        self.width = BASKET_WIDTH
        self.height = BASKET_HEIGHT
        self.x = WIDTH // 2 - self.width // 2
        self.y = HEIGHT - BASKET_Y_OFFSET - self.height
        self.speed = BASKET_SPEED

    def handle_input(self, keys):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += self.speed
        # clamp to screen
        self.x = max(0, min(WIDTH - self.width, self.x))

    def draw(self, surface):
        pygame.draw.rect(
            surface,
            BASKET_COLOR,
            (self.x, self.y, self.width, self.height),
            border_radius=6,
        )

    def catches(self, item):
        """Return True if the basket's top edge overlaps the item."""
        within_x = self.x <= item.x <= self.x + self.width
        within_y = self.y <= item.y <= self.y + self.height
        return within_x and within_y
