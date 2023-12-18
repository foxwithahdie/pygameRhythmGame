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

def key_padding(screen: pygame.Surface) -> int:
    """
    Calculates the padding around the keys.
    :param screen: Surface for image optimization.
    :return: Pixel width of padding.
    """
    screen_width: int = constants.SCREEN_WIDTH
    key_spacing = constants.KEY_SPACING
    image = pygame.image.load(os.path.join(constants.ASSET_DIRECTORY, "grey_circle.png")).convert_alpha(screen)
    image = pygame.transform.scale(image, scale_size(image.get_size(), (2 / 3)))
    key_rect_left: int = key_spacing - image.get_width()//2
    key_rect_right: int = (key_spacing * 4) + image.get_width()//2
    key_rect_width: int = key_rect_right - key_rect_left
    
    # print("key_rect_left: ", key_rect_left)
    # print("key_rect_right: ", key_rect_right)
    
    return (screen_width - key_rect_width) // (key_spacing // 15)
