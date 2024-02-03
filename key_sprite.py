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
    def __init__(self, key_type: KeySpriteType, x_pos: int, key: str, *groups, screen_hint: Union[pygame.Surface, None] = None):
        super().__init__(*groups)
        self.key_type = key_type
        self.x_pos = x_pos
        if screen_hint is not None:
            self.image = pygame.image.load(key_type.grey_circle_image).convert_alpha(screen_hint)
        else:
            self.image = pygame.image.load(key_type.grey_circle_image).convert_alpha()
        self.image = pygame.transform.scale(self.image, helpers.scale_size(self.image.get_size(), 2 / 3))

        self.rect = self.image.get_rect(center=(self.x_pos, constants.KEY_Y_POS))
        self.key = pygame.key.key_code(key)
        self.keydown = False
        
    def press_button(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == self.key:
                self.keydown = True
                self.rect.center = (self.x_pos, constants.KEY_Y_POS)
        if event.type == pygame.KEYUP:
            self.keydown = False
            self.rect.center = (self.x_pos, constants.KEY_Y_POS)
            
    def draw(self, key_type: KeySpriteType, surface: pygame.Surface):
        if self.keydown:
            self.image = pygame.image.load(self.key_type.dull_circle_image).convert_alpha(surface)
            self.image = pygame.transform.scale(self.image, helpers.scale_size(self.image.get_size(), 2/3))
            surface.blit(self.image, self.rect)
        else:
            self.image = pygame.image.load(key_type.grey_circle_image).convert_alpha(surface)
            self.image = pygame.transform.scale(self.image, helpers.scale_size(self.image.get_size(), 2/3))
            surface.blit(self.image, self.rect)
