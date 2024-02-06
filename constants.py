import pygame
import os
import helpers
import settings

pygame.init()


WINDOW_TITLE = "Rhythm Game"

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

BACKGROUND_COLOR = pygame.Color(255, 255, 255)

ASSET_DIRECTORY = "Assets"

KEY_DOWN_Y_POS = 520
KEY_UP_Y_POS = 80

SCROLL_SPEED = settings.fps * settings.scroll_speed

KEY_SPACING = int(150 * settings.lane_offset)

CIRCLE_KEY = helpers.transform_image(pygame.image.load(
    os.path.join(ASSET_DIRECTORY, "grey_circle.png")).convert_alpha(), (2 / 3))
CIRCLE_KEY_WIDTH = CIRCLE_KEY.get_width()

BAR_KEY = helpers.transform_image(pygame.image.load(
    os.path.join(ASSET_DIRECTORY, "grey_bar.png")).convert_alpha(), (2 / 3))
BAR_KEY_WIDTH = CIRCLE_KEY.get_width()

ARROW_DOWN_KEY = helpers.transform_image(pygame.image.load(
    os.path.join(ASSET_DIRECTORY, "grey_down_arrow.png")).convert_alpha(), (2 / 3))
ARROW_DOWN_KEY_WIDTH = ARROW_DOWN_KEY.get_width()

ARROW_UP_KEY = helpers.transform_image(pygame.image.load(
    os.path.join(ASSET_DIRECTORY, "grey_up_arrow.png")).convert_alpha(), (2 / 3))
ARROW_UP_KEY_WIDTH = ARROW_UP_KEY.get_width()

ARROW_RIGHT_KEY = helpers.transform_image(pygame.image.load(
    os.path.join(ASSET_DIRECTORY, "grey_right_arrow.png")).convert_alpha(), (2 / 3))
ARROW_RIGHT_KEY_WIDTH = ARROW_RIGHT_KEY.get_width()

ARROW_LEFT_KEY = helpers.transform_image(pygame.image.load(
    os.path.join(ASSET_DIRECTORY, "grey_left_arrow.png")).convert_alpha(), (2 / 3))
ARROW_LEFT_KEY_WIDTH = ARROW_LEFT_KEY.get_width()
