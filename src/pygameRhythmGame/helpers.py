import pygame


def scale_size(size: tuple[int, int], scale: float) -> tuple[int, int]:
    """
    Scales a size by a given scale.
    :param size: The size to scale.
    :param scale: The scale to apply.
    :return: The scaled size.
    """

    return int(size[0] * scale), int(size[1] * scale)


def transform_image(image: pygame.Surface, scale: float) -> pygame.Surface:
    """
    Scales an image by a given scale.
    :param image: Image.
    :param scale: Scale.
    :return: The scaled image.
    """
    return pygame.transform.scale(image, scale_size(image.get_size(), scale))


def rect_distance(rect1: pygame.Rect, rect2: pygame.Rect) -> float:
    """
    Calculates the distance between two rectangles.
    :param rect1:
    :param rect2:
    :return: Distance between the two rectangles.
    """

    return ((rect2.centerx - rect1.centerx) ** 2 + (rect2.centery - rect1.centery) ** 2) ** 0.5
