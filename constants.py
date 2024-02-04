import pygame
import os
import helpers
import settings

pygame.init()


WINDOW_TITLE = "Rhythm Game"

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

FPS = 60

BACKGROUND_COLOR = pygame.Color(255, 255, 255)

ASSET_DIRECTORY = "assets"

SCROLL_SPEED = 50

KEY_DOWN_Y_POS = 520
KEY_UP_Y_POS = 80

CIRCLE_KEY = pygame.image.load(os.path.join(ASSET_DIRECTORY, "grey_circle.png")).convert_alpha()
CIRCLE_KEY = pygame.transform.scale(CIRCLE_KEY, helpers.scale_size(CIRCLE_KEY.get_size(), (2 / 3)))
CIRCLE_KEY_WIDTH = CIRCLE_KEY.get_width()

KEY_SPACING = int(150 * settings.lane_offset)
