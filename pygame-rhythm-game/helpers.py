import pygame


def scale_size(size: tuple[int, int], scale: float) -> tuple[int, int]:
    """Scales a tuple by a given scalar.

    Args:
        size (tuple[int, int]): The size tuple.
        scale (float): The scalar.

    Returns:
        tuple[int, int]: The tuple, scaled.
    """

    return int(size[0] * scale), int(size[1] * scale)


def transform_image(image: pygame.Surface, scale: float) -> pygame.Surface:
    """Scales an image by a given scalar.

    Args:
        image (pygame.Surface): The given image.
        scale (float): The scalar.

    Returns:
        pygame.Surface: The image, scaled by a particular width and height scalar, determined by scale size.
    """
    return pygame.transform.scale(image, scale_size(image.get_size(), scale))


def rect_distance(rect1: pygame.Rect, rect2: pygame.Rect) -> float:
    """Calculates the distance between two pygame rectangles.

    Args:
        rect1 (pygame.Rect): First rectangle.
        rect2 (pygame.Rect): Second rectangle.

    Returns:
        float: Distance between both rectangles.
    """

    return ((rect2.centerx - rect1.centerx) ** 2 + (rect2.centery - rect1.centery) ** 2) ** 0.5
