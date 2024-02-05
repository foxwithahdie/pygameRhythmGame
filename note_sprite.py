import os
from enum import Enum

import pygame
from pygame.sprite import Sprite

import constants
import helpers
import settings


class CircleSpriteType(Enum):
    """
    An enum representing the type (color) of a note sprite.
    """

    YELLOW = 1
    PURPLE = 2
    RED = 3
    BLUE = 4

    @property
    def note_image(self) -> str:
        """
        The image of the circle for this note type.
        :return: The file path of the image.
        """

        match self:
            case CircleSpriteType.YELLOW:
                file_name = "yellow_circle.png"
            case CircleSpriteType.PURPLE:
                file_name = "purple_circle.png"
            case CircleSpriteType.RED:
                file_name = "red_circle.png"
            case CircleSpriteType.BLUE:
                file_name = "blue_circle.png"
            case _:
                raise ValueError(f"Invalid note type: {self}")

        return os.path.join(constants.ASSET_DIRECTORY, file_name)


class ArrowSpriteType(Enum):
    """
    An enum representing the type (color) of a note sprite.
    """

    YELLOW = 1
    PURPLE = 2
    RED = 3
    BLUE = 4

    @property
    def note_image(self) -> str:
        """
        The image of the circle for this note type.
        :return: The file path of the image.
        """

        match self:
            case ArrowSpriteType.YELLOW:
                file_name = "yellow_left_arrow.png"
            case ArrowSpriteType.PURPLE:
                file_name = "purple_down_arrow.png"
            case ArrowSpriteType.RED:
                file_name = "red_up_arrow.png"
            case ArrowSpriteType.BLUE:
                file_name = "blue_right_arrow.png"
            case _:
                raise ValueError(f"Invalid note type: {self}")

        return os.path.join(constants.ASSET_DIRECTORY, file_name)


class BarSpriteType(Enum):
    """
    An enum representing the type (color) of a note sprite.
    """

    YELLOW = 1
    PURPLE = 2
    RED = 3
    BLUE = 4

    @property
    def note_image(self) -> str:
        """
        The image of the circle for this note type.
        :return: The file path of the image.
        """

        match self:
            case BarSpriteType.YELLOW:
                file_name = "yellow_bar.png"
            case BarSpriteType.PURPLE:
                file_name = "purple_bar.png"
            case BarSpriteType.RED:
                file_name = "red_bar.png"
            case BarSpriteType.BLUE:
                file_name = "blue_bar.png"
            case _:
                raise ValueError(f"Invalid note type: {self}")

        return os.path.join(constants.ASSET_DIRECTORY, file_name)
    

type NoteType = CircleSpriteType | ArrowSpriteType | BarSpriteType

class NoteSprite(Sprite):
    """
    A sprite representing a falling note.
    """
    
    def __init__(self, note_type: NoteType, x_pos: int, *groups,
                 surface_hint: pygame.Surface | None = None):
        super().__init__(*groups)
        if surface_hint is not None:
            self.image = pygame.image.load(note_type.note_image).convert_alpha(surface_hint)
        else:
            self.image = pygame.image.load(note_type.note_image).convert_alpha()
        self.image = pygame.transform.scale(self.image, helpers.scale_size(self.image.get_size(), 2/3))
        self.rect = self.image.get_rect(center=(x_pos, helpers.note_start_pos()))

    def update(self, delta_time: float) -> None:
        if settings.downscroll:
            self.rect.centery += int(delta_time * constants.SCROLL_SPEED)
        else:
            self.rect.centery -= int(delta_time * constants.SCROLL_SPEED)
