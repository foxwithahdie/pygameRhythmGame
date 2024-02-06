import os
from enum import Enum

import pygame
from pygame.sprite import Sprite

import constants
import helpers

pygame.display.init()

type KeySpriteType = CircleKeySpriteType | ArrowKeySpriteType | BarKeySpriteType


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
    def dull_key_image(self) -> str:
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

    @classmethod
    def key_size(cls) -> int:
        return constants.CIRCLE_KEY_WIDTH

   
class ArrowKeySpriteType(Enum):
    """
    An enum representing the type (color) of an arrow key sprite.
    """

    YELLOW = 1
    PURPLE = 2
    RED = 3
    BLUE = 4
    
    @property
    def grey_key_image(self) -> str:
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
    def dull_key_image(self) -> str:
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
    def key_size(cls, arrow_dir: int) -> int:
        match arrow_dir:
            case 1:
                return constants.ARROW_LEFT_KEY_WIDTH
            case 2:
                return constants.ARROW_DOWN_KEY_WIDTH
            case 3:
                return constants.ARROW_UP_KEY_WIDTH
            case 4:
                return constants.ARROW_RIGHT_KEY_WIDTH
            case _:
                raise NameError(f"Invalid key number. There are only 4 keys!")


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
    def dull_key_image(self) -> str:
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

    @classmethod
    def key_size(cls) -> int:
        return constants.BAR_KEY_WIDTH


class KeySprite(Sprite):
    """
    A sprite representing the key that the user presses.
    """
    def __init__(self, key_type: KeySpriteType, note_pos: int, key: str, *groups,
                 screen_hint: pygame.Surface | None = None):
        super().__init__(*groups)
        self.key_type = key_type
        key_spacing = constants.KEY_SPACING * (note_pos - 1)
        if isinstance(key_type, ArrowKeySpriteType):
            self.x_pos = helpers.key_padding(key_type, arrow_dir=note_pos) + (key_type.key_size(note_pos) // 2)
            self.x_pos += key_spacing
        else:
            self.x_pos = helpers.key_padding(key_type) + (key_type.key_size() // 2) + key_spacing

        if screen_hint is not None:
            self.image = helpers.transform_image(
                pygame.image.load(key_type.grey_key_image).convert_alpha(screen_hint), (2 / 3)
            )
        else:
            self.image = helpers.transform_image(
                pygame.image.load(key_type.grey_key_image).convert_alpha(), (2 / 3)
            )
        self.rect = self.image.get_rect(center=(self.x_pos, helpers.key_direction()))
        self.key = pygame.key.key_code(key)
        self.keydown = False

    def press_button(self, event: pygame.event.Event) -> None:
        if event.type == pygame.KEYDOWN:
            if event.key == self.key:
                self.keydown = True
                self.rect.center = (self.x_pos, helpers.key_direction())
        if event.type == pygame.KEYUP:
            self.keydown = False
            self.rect.center = (self.x_pos, helpers.key_direction())
    
    def change_keybind(self, key: str) -> None:
        self.key = pygame.key.key_code(key)
    
    def draw(self, key_type: CircleKeySpriteType, surface: pygame.Surface) -> None:
        if self.keydown:
            self.image = helpers.transform_image(
                pygame.image.load(self.key_type.dull_key_image).convert_alpha(surface), (2 / 3)
            )
            self.rect = self.image.get_rect(center=(self.x_pos, helpers.key_direction()))
            surface.blit(self.image, self.rect)
        else:
            self.image = helpers.transform_image(
                pygame.image.load(key_type.grey_key_image).convert_alpha(surface), (2 / 3)
            )
            self.rect = self.image.get_rect(center=(self.x_pos, helpers.key_direction()))
            surface.blit(self.image, self.rect)
