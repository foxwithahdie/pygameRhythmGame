from enum import Enum
import os
from typing import NoReturn, Optional

import pygame

import helpers
import constants
import settings

pygame.display.init()


class CircleKeySpriteType(Enum):
    """
    An enum representing the type (color) of a circle key sprite.
    """

    YELLOW = 1
    PURPLE = 2
    RED = 3
    BLUE = 4

    @property
    def grey_key_image(self) -> str:
        return os.path.join(constants.ASSET_DIRECTORY, "grey_circle.png")

    @property
    def dull_key_image(self) -> str | NoReturn:
        """Returns the file name of the dull key.

        Raises:
            ValueError: Raises if it is not a defined instance of the circle key sprite type.

        Returns:
            str | NoReturn: Will return the file name of the key type, otherwise will raise an error.
        """
        directory = constants.ASSET_DIRECTORY

        match self:
            case CircleKeySpriteType.YELLOW:
                file_name = "yellow_circle_dull.png"
            case CircleKeySpriteType.PURPLE:
                file_name = "purple_circle_dull.png"
            case CircleKeySpriteType.RED:
                file_name = "red_circle_dull.png"
            case CircleKeySpriteType.BLUE:
                file_name = "blue_circle_dull.png"
            case _:
                raise ValueError(f"Invalid key type: {self}")

        return os.path.join(directory, file_name)

    @property
    def key_size(self) -> int:
        directory = constants.ASSET_DIRECTORY
        circle_key: pygame.Surface = helpers.transform_image(pygame.image.load(
            os.path.join(directory, "grey_circle.png")).convert_alpha(), (2 / 3))
        return circle_key.get_width()

   
class ArrowKeySpriteType(Enum):
    """
    An enum representing the type (color) of an arrow key sprite.
    """

    YELLOW = 1
    PURPLE = 2
    RED = 3
    BLUE = 4
    
    @property
    def grey_key_image(self) -> str | NoReturn:
        """Returns the grey version of the certain arrow key.
        Raises:
            ValueError: Raises if it is not a defined instance of the arrow key sprite type.

        Returns:
            str | NoReturn: Returns the grey key image file name, raises an error otherwise.
        """
        directory = constants.ASSET_DIRECTORY
        
        match self:
            case ArrowKeySpriteType.YELLOW:
                file_name = 'grey_left_arrow.png'
            case ArrowKeySpriteType.PURPLE:
                file_name = 'grey_down_arrow.png'
            case ArrowKeySpriteType.RED:
                file_name = 'grey_up_arrow.png'
            case ArrowKeySpriteType.BLUE:
                file_name = 'grey_right_arrow.png'
            case _:
                raise ValueError(f"Invalid key type: {self}")
            
        return os.path.join(directory, file_name)

    @property
    def dull_key_image(self) -> str | NoReturn:
        """Returns the file name of the dull key image of a certain arrow key.

        Raises:
            ValueError: Raises if it is not a defined instance of the arrow key sprite type.

        Returns:
            str | NoReturn: Returns the file name, otherwise raises an error.
        """
        directory = constants.ASSET_DIRECTORY

        match self:
            case ArrowKeySpriteType.YELLOW:
                file_name = "yellow_left_arrow_dull.png"
            case ArrowKeySpriteType.PURPLE:
                file_name = "purple_down_arrow_dull.png"
            case ArrowKeySpriteType.RED:
                file_name = "red_up_arrow_dull.png"
            case ArrowKeySpriteType.BLUE:
                file_name = "blue_right_arrow_dull.png"
            case _:
                raise ValueError(f"Invalid key type: {self}")

        return os.path.join(directory, file_name)
    
    @classmethod
    def key_size(cls, arrow_dir: Optional[int] = None) -> int | NoReturn:
        """Gives the width of the key of a specific arrow direction.
            Creates an instance of the key surface and returns the width.

        Args:
            arrow_dir (Optional[int], optional): The direction of the arrow key. Defaults to None. 1 -> Left, 2 -> Down, 3 -> Up, 4 -> Right.
                
        Raises:
            ValueError: Raises if it is not a defined direction of the arrow key sprite type.

        Returns:
            int | NoReturn: Returns the width of the key, otherwise raises an error.
        """
        directory = constants.ASSET_DIRECTORY

        match arrow_dir:
            case 1:
                arrow_left_key: pygame.Surface = helpers.transform_image(pygame.image.load(
                    os.path.join(directory, "grey_left_arrow.png")).convert_alpha(), (2 / 3))
                return arrow_left_key.get_width()
            case 2:
                arrow_down_key: pygame.Surface = helpers.transform_image(pygame.image.load(
                    os.path.join(directory, "grey_down_arrow.png")).convert_alpha(), (2 / 3))
                return arrow_down_key.get_width()
            case 3:
                arrow_up_key: pygame.Surface = helpers.transform_image(pygame.image.load(
                    os.path.join(directory, "grey_up_arrow.png")).convert_alpha(), (2 / 3))
                return arrow_up_key.get_width()
            case 4:
                arrow_right_key: pygame.Surface = helpers.transform_image(pygame.image.load(
                    os.path.join(directory, "grey_right_arrow.png")).convert_alpha(), (2 / 3))
                return arrow_right_key.get_width()
            case _:
                raise ValueError(f"Invalid key number {arrow_dir}. There are only 4 types of keys!")


class BarKeySpriteType(Enum):
    """
    An enum representing the type (color) of a bar key sprite.
    """

    YELLOW = 1
    PURPLE = 2
    RED = 3
    BLUE = 4

    @property
    def grey_key_image(self) -> str:
        return os.path.join(constants.ASSET_DIRECTORY, "grey_bar.png")

    @property
    def dull_key_image(self) -> str | NoReturn:
        """Returns the file name of the dull bar key image.

        Raises:
            ValueError: Raises if it is not a defined instance of the bar key sprite type.

        Returns:
            str | NoReturn: The file name of the specific bar key instance, otherwise raises an error.
        """
        directory = constants.ASSET_DIRECTORY

        match self:
            case BarKeySpriteType.YELLOW:
                file_name = "yellow_bar_dull.png"
            case BarKeySpriteType.PURPLE:
                file_name = "purple_bar_dull.png"
            case BarKeySpriteType.RED:
                file_name = "red_bar_dull.png"
            case BarKeySpriteType.BLUE:
                file_name = "blue_bar_dull.png"
            case _:
                raise ValueError(f"Invalid key type: {self}")

        return os.path.join(directory, file_name)

    @property
    def key_size(self) -> int:
        directory = constants.ASSET_DIRECTORY
        bar_key: pygame.Surface = helpers.transform_image(pygame.image.load(
            os.path.join(directory, "grey_bar.png")).convert_alpha(), (2 / 3))
        return bar_key.get_width()
    
    
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
        """_summary_

        Returns:
            int: _description_
        """
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
        """
        The size of the note for the specific note type.
        :return: The integer size of the note type.
        """
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
    def note_size(self) -> int:
        """_summary_

        Returns:
            int: _description_
        """
        directory = constants.ASSET_DIRECTORY
        bar_note: pygame.Surface = helpers.transform_image(pygame.image.load(
            os.path.join(directory, "grey_bar.png")).convert_alpha(), (2 / 3))
        return bar_note.get_width()


def key_padding(key_type: CircleKeySpriteType | ArrowKeySpriteType | BarKeySpriteType,
                arrow_dir: Optional[int] = None) -> int:
    """
    Calculates the padding around the keys.
    :param key_type: Type of key
    :param arrow_dir: If the type of key is an arrow, find the specific arrow direction.
    :return: Pixel width of padding.
    """

    screen_width: int = constants.SCREEN_WIDTH
    key_spacing: int = constants.KEY_SPACING
    if isinstance(key_type, ArrowKeySpriteType):
        key_rect_right: int = key_type.key_size(arrow_dir=arrow_dir) + key_spacing * 3
    else:
        key_rect_right = key_type.key_size + key_spacing * 3

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
    """
    Returns the starting Y position of a note
    depending on if it is downscroll or upscroll.

    Returns:
        int: Y p
    """
    return -60 if settings.downscroll else constants.SCREEN_HEIGHT + 60
