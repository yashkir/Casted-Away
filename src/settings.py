import pygame
from src.paths import *

CAPTION = "Castaway"
FPS = 60
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT) = (800, 600)

# Layers
NUM_OF_LAYERS = 7

# COLORS
BLACK = pygame.color.THECOLORS["black"]
WHITE = pygame.color.THECOLORS["white"]
GRAY = pygame.color.THECOLORS["gray"]
BROWN = pygame.color.THECOLORS["brown"]

# ACTORS
ADULT_ACTOR_SIZE = 32, 32

# Sprite sheets
SPRITES_SHEET_SPRITE_SIZE = (48, 48)


def flip_y(pos):
    """Convert pymunk physics to pygame coordinates

    In pymunk positive y is up
    """
    # if type(pos) is tuple or type(pos) is list:
    try:
        return pos[0], SCREEN_HEIGHT - pos[1]
    except TypeError:
        # else:
        y = pos
        return SCREEN_HEIGHT - y