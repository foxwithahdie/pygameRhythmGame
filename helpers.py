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
    :return:
    """

    return ((rect2.centerx - rect1.centerx) ** 2 + (rect2.centery - rect1.centery) ** 2) ** 0.5

def key_padding() -> int:
    screen_width: int = constants.SCREEN_WIDTH
    image = pygame.image.load(os.path.join(constants.ASSET_DIRECTORY, "grey_circle.png")).convert_alpha()
    key_rect_left: int = 137 - image.get_size()[0]//2
    key_rect_right: int = (137 * 4) + image.get_size()[0]//2
    key_rect_width: int = key_rect_right - key_rect_left
    
    return (screen_width - key_rect_width) // 2

def main_space_x_range() -> tuple[int, int]:
    return key_padding(), constants.SCREEN_WIDTH - key_padding()
