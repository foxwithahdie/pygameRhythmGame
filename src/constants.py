import pygame
import os
import settings

WINDOW_TITLE: str = "Rhythm Game"

SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600

BACKGROUND_COLOR: pygame.Color = pygame.Color(255, 255, 255)

ASSET_DIRECTORY: str = os.path.join("..", "Assets")

KEY_DOWN_Y_POS: int = 520
KEY_UP_Y_POS: int = 80

SCROLL_SPEED: float = settings.fps * settings.scroll_speed

KEY_SPACING: int = int(150 * settings.lane_offset)
