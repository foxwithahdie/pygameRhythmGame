import os
from enum import Enum

import pygame
from pygame.sprite import Sprite

import constants
import helpers

pygame.display.init()


class CircleKeySpriteType(Enum):
    """
    An enum representing the type (color) of a key sprite.
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

   
class ArrowKeySpriteType(Enum):
    """
    An enum representing the type (color) of a key sprite.
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
    

class BarKeySpriteType(Enum):
    """
    An enum representing the type (color) of a key sprite.
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


type KeySpriteType = CircleKeySpriteType | ArrowKeySpriteType | BarKeySpriteType


class KeySprite(Sprite):
    def __init__(self, key_type: KeySpriteType, x_pos: int, key: str, *groups,
                 screen_hint: pygame.Surface | None = None):
        super().__init__(*groups)
        self.key_type = key_type
        self.x_pos = x_pos
        if screen_hint is not None:
            self.image = pygame.image.load(key_type.grey_key_image).convert_alpha(screen_hint)
        else:
            self.image = pygame.image.load(key_type.grey_key_image).convert_alpha()
        self.image = pygame.transform.scale(self.image, helpers.scale_size(self.image.get_size(), 2 / 3))
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
    
    def update_x_pos(self, x_position: int) -> None:
        self.x_pos = x_position
    
    def change_keybind(self, key: str) -> None:
        self.key = pygame.key.key_code(key)
    
    def draw(self, key_type: CircleKeySpriteType, surface: pygame.Surface) -> None:
        if self.keydown:
            self.image = pygame.image.load(self.key_type.dull_key_image).convert_alpha(surface)
            self.image = pygame.transform.scale(self.image, helpers.scale_size(self.image.get_size(), 2 / 3))
            surface.blit(self.image, self.rect)
        else:
            self.image = pygame.image.load(key_type.grey_key_image).convert_alpha(surface)
            self.image = pygame.transform.scale(self.image, helpers.scale_size(self.image.get_size(), 2 / 3))
            surface.blit(self.image, self.rect)
