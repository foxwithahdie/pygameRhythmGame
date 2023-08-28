import os
from enum import Enum
from typing import Union

import pygame
from pygame.sprite import Sprite

import constants
import helpers

pygame.display.init()


class KeySpriteType(Enum):
    """
    An enum representing the type (color) of a key sprite.
    """

    YELLOW = 1
    PURPLE = 2
    RED = 3
    BLUE = 4

    @property
    def grey_circle_image(self) -> str:
        return os.path.join(constants.ASSET_DIRECTORY, "grey_circle.png")

    @property
    def dull_circle_image(self) -> str:
        directory = constants.ASSET_DIRECTORY

        match self:
            case KeySpriteType.YELLOW:
                file_name = "yellow_circle_dull.png"
            case KeySpriteType.PURPLE:
                file_name = "purple_circle_dull.png"
            case KeySpriteType.RED:
                file_name = "red_circle_dull.png"
            case KeySpriteType.BLUE:
                file_name = "blue_circle_dull.png"
            case _:
                raise ValueError(f"Invalid key type: {self}")

        return os.path.join(directory, file_name)


class KeySprite(Sprite):
    def __init__(self, key_type: KeySpriteType, x_pos: int, *groups, screen_hint: Union[pygame.Surface, None] = None):
        super().__init__(*groups)
        self.key_type = key_type
        self.image = pygame.image.load(key_type.grey_circle_image).convert_alpha(screen_hint)
        self.image = pygame.transform.scale(self.image, helpers.scale_size(self.image.get_size(), 2 / 3))

        self.rect = self.image.get_rect()
        self.rect.x = x_pos - self.rect.width / 2
        self.rect.y = constants.KEY_Y_POS
        self.keydown = False
    def press_button(self, event: pygame.event.get(), screen_hint: Union[pygame.Surface, None] = None):
        if event.type == pygame.KEYDOWN:
            self.keydown = True
            self.image = pygame.image.load(self.key_type.dull_circle_image).convert_alpha(screen_hint)
            self.image = pygame.transform.scale(self.image, helpers.scale_size(self.image.get_size(), 2 / 3))
            self.rect = self.image.get_rect()
            self.rect.x = self.rect.x
            self.rect.y = self.rect.y
        if event.type == pygame.KEYUP:
            self.keydown = False
            self.rect = self.image.get_rect()
            self.rect.x = self.rect.x
            self.rect.y = self.rect.y