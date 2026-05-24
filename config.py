"""
Game-wide constants. Tweak these if you want to experiment with how the game feels.

Nothing in this file does anything by itself — it's just numbers and colors that
other files import.
"""

# --- window ---
WIDTH = 600
HEIGHT = 700
FPS = 60
TITLE = "Catch the Falling Items"

# --- colors (R, G, B) ---
BG_COLOR = (20, 24, 40)
TEXT_COLOR = (240, 240, 240)
BASKET_COLOR = (180, 140, 60)

# --- basket ---
BASKET_WIDTH = 90
BASKET_HEIGHT = 18
BASKET_SPEED = 7
BASKET_Y_OFFSET = 40  # distance from bottom of screen

# --- spawning ---
SPAWN_INTERVAL_MS = 700   # how often a new item appears
MAX_MISSES = 5            # game over after this many missed items
