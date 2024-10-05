import pygame
import settings

WINDOW_TITLE: str = "Rhythm Game"

TOTAL_COLUMNS: int = 4

SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600

BACKGROUND_COLOR: pygame.Color = pygame.Color(255, 255, 255)

ASSET_DIRECTORY: str = "Assets"

MAP_DIRECTORY: str = "Maps"

SOUND_DIRECTORY: str = "Sounds"


KEY_DOWN_Y_POS: int = 520
KEY_UP_Y_POS: int = 80

SCROLL_SPEED: float = settings.fps * settings.scroll_speed

KEY_SPACING: int = int(150 * settings.lane_offset)
