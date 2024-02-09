import os
from enum import Enum
from typing import NoReturn, Optional

import pygame
import pygame.sprite as sprite

import constants
import helpers
import settings


class CircleSpriteType(Enum):
    """
    An enum representing the type (color) of a circle note sprite.
    """

    YELLOW = 1
    PURPLE = 2
    RED = 3
    BLUE = 4

    @property
    def note_image(self) -> str | NoReturn:
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

    @property
    def note_size(self) -> int:
        directory = constants.ASSET_DIRECTORY
        circle_note: pygame.Surface = helpers.transform_image(pygame.image.load(
            os.path.join(directory, "grey_circle.png")).convert_alpha(), (2 / 3))
        return circle_note.get_width()


class ArrowSpriteType(Enum):
    """
    An enum representing the type (color) of an arrow note sprite.
    """

    YELLOW = 1
    PURPLE = 2
    RED = 3
    BLUE = 4

    @property
    def note_image(self) -> str | NoReturn:
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

    @property
    def note_size(self) -> int | NoReturn:
        directory = constants.ASSET_DIRECTORY

        match self:
            case ArrowSpriteType.YELLOW:
                arrow_left_note: pygame.Surface = helpers.transform_image(pygame.image.load(
                    os.path.join(directory, "yellow_left_arrow.png")).convert_alpha(), (2 / 3))
                return arrow_left_note.get_width()
            case ArrowSpriteType.PURPLE:
                arrow_down_note: pygame.Surface = helpers.transform_image(pygame.image.load(
                    os.path.join(directory, "purple_down_arrow.png")).convert_alpha(), (2 / 3))
                return arrow_down_note.get_width()
            case ArrowSpriteType.RED:
                arrow_up_note: pygame.Surface = helpers.transform_image(pygame.image.load(
                    os.path.join(directory, "red_up_arrow.png")).convert_alpha(), (2 / 3))
                return arrow_up_note.get_width()
            case ArrowSpriteType.BLUE:
                arrow_right_note: pygame.Surface = helpers.transform_image(pygame.image.load(
                    os.path.join(directory, "blue_right_arrow.png")).convert_alpha(), (2 / 3))
                return arrow_right_note.get_width()
            case _:
                raise ValueError(f"Invalid note type: {self}")


class BarSpriteType(Enum):
    """
    An enum representing the type (color) of a bar note sprite.
    """

    YELLOW = 1
    PURPLE = 2
    RED = 3
    BLUE = 4

    @property
    def note_image(self) -> str | NoReturn:
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

    @property
    def key_size(self) -> int:
        directory = constants.ASSET_DIRECTORY
        bar_note: pygame.Surface = helpers.transform_image(pygame.image.load(
            os.path.join(directory, "grey_bar.png")).convert_alpha(), (2 / 3))
        return bar_note.get_width()


class NoteSprite(sprite.Sprite):
    """
    A sprite representing a falling note.
    """

    def __init__(self, note_type: CircleSpriteType | ArrowSpriteType | BarSpriteType,
                 x_pos: int, *groups, surface_hint: Optional[pygame.Surface] = None):
        super().__init__(*groups)
        if surface_hint is not None:
            self.image = pygame.image.load(note_type.note_image).convert_alpha(surface_hint)
        else:
            self.image = pygame.image.load(note_type.note_image).convert_alpha()
        self.image = pygame.transform.scale(self.image, helpers.scale_size(self.image.get_size(), 2 / 3))
        self.rect = self.image.get_rect(center=(x_pos, helpers.note_start_pos()))
        self.note_type = note_type

    def update(self, delta_time: float) -> None:
        buffer = 100
        if settings.downscroll:
            self.rect.centery += int(delta_time * constants.SCROLL_SPEED)
        else:
            self.rect.centery -= int(delta_time * constants.SCROLL_SPEED)
        if self.rect.centery - self.note_type.note_size - buffer >= constants.SCREEN_WIDTH\
           or self.rect.centery + self.note_type.note_size + buffer <= 0:
            sprite.Sprite.kill(self)
