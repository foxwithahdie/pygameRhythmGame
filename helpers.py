import pygame
import os
import constants
import settings
from key_sprite import KeySprite


def scale_size(size: tuple[int, int], scale: float) -> tuple[int, int]:
    """
    Scales a size by a given scale.
    :param size: The size to scale.
    :param scale: The scale to apply.
    :return: The scaled size.
    """

    return int(size[0] * scale), int(size[1] * scale)


def rect_distance(rect1: pygame.Rect, rect2: pygame.Rect) -> float:
    """
    Calculates the distance between two rectangles.
    :param rect1:
    :param rect2:
    :return: Distance between the two rectangles.
    """

    return ((rect2.centerx - rect1.centerx) ** 2 + (rect2.centery - rect1.centery) ** 2) ** 0.5


def key_padding() -> int:
    """
    Calculates the padding around the keys.
    :return: Pixel width of padding.
    """
    
    screen_width: int = constants.SCREEN_WIDTH
    key_spacing: int = constants.KEY_SPACING
    
    key_rect_right: int = (constants.CIRCLE_KEY_WIDTH) + key_spacing * 3
    
    return (screen_width - key_rect_right) // 2


def key_direction() -> int:
    """
    Returns the y position for the keys depending on the 
    scroll direction set in settings.

    Returns:
        int: Y position.
    """
    return constants.KEY_DOWN_Y_POS if settings.downscroll else constants.KEY_UP_Y_POS

def note_start_pos() -> int:
    return -60 if settings.downscroll else constants.SCREEN_HEIGHT + 60