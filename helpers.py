import pygame


def scale_size(size: tuple[int, int], scale: float) -> tuple[int, int]:
    """
    Scales a size by a given scale.
    :param size: The size to scale.
    :param scale: The scale to apply.
    :return: The scaled size.
    """

    return int(size[0] * scale), int(size[1] * scale)


def rect_distance(rect1: pygame.rect.Rect, rect2: pygame.rect.Rect):
    """
    Calculates the distance between two rectangles.
    :param rect1:
    :param rect2:
    :return:
    """

    return ((rect2.centerx - rect1.centerx) ** 2 + (rect2.centery - rect1.centery) ** 2) ** 0.5

def key_spacing(common_multiplier):
    """
    Spaces the notes out from eachother so the player can have key spacing.
    :param common_multiplier
    """
    
    return ...