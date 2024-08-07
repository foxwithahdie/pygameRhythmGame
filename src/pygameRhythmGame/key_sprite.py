import os
from enum import Enum
from typing import NoReturn, Optional

import pygame
from game_context import GameContext
import pygame.sprite as sprite

import constants as constants
import helpers as helpers

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


class KeySprite(sprite.Sprite):
    """
    A sprite representing the key that the user presses.
    """
    def __init__(self, key_type: CircleKeySpriteType | ArrowKeySpriteType | BarKeySpriteType, note_pos: int, key: str,
                 *groups, screen_hint: Optional[pygame.Surface] = None):
        super().__init__(*groups)
        self.key_type = key_type
        self.note_pos = note_pos
        key_spacing = constants.KEY_SPACING * (note_pos - 1)
        if isinstance(key_type, ArrowKeySpriteType):
            self.x_pos = helpers.key_padding(key_type, arrow_dir=note_pos) + (key_type.key_size(note_pos) // 2)
            self.x_pos += key_spacing
        else:
            self.x_pos = helpers.key_padding(key_type) + (key_type.key_size // 2) + key_spacing

        if screen_hint is not None:
            self.image = helpers.transform_image(
                pygame.image.load(key_type.grey_key_image).convert_alpha(screen_hint), (2 / 3)
            )
        else:
            self.image = helpers.transform_image(
                pygame.image.load(key_type.grey_key_image).convert_alpha(), (2 / 3)
            )
        self.rect: pygame.Rect = self.image.get_rect(center=(self.x_pos, helpers.key_direction()))
        self.key: int = pygame.key.key_code(key)
        self.event = pygame.event.custom_type()
        self.keydown: bool = False
        self.note_intersected: bool = False
        self.start_time: float = 0.0

    def press_button(self, event: pygame.event.Event, delta_time: float) -> None:
        
        note_intersection = sprite.spritecollideany(self, GameContext.notes_group)
        
        if note_intersection and not self.note_intersected:
            self.note_intersected = True
            self.start_time = delta_time
            print(f'at note_intersection: {self.start_time}')
            if isinstance(self.key_type, ArrowKeySpriteType):
                pygame.time.set_timer(self.event, 
                    (self.key_type.key_size(arrow_dir=self.note_pos)) // int(delta_time * constants.SCROLL_SPEED)
                )
            else:
                pygame.time.set_timer(self.event, 
                    (self.key_type.key_size) // int(delta_time * constants.SCROLL_SPEED)
                )     
        
        if event.type == pygame.KEYDOWN:
            if event.key == self.key:
                self.keydown = True
                self.rect.center = (self.x_pos, helpers.key_direction())
        if event.type == pygame.KEYUP:
            self.keydown = False
            self.rect.center = (self.x_pos, helpers.key_direction())
        if event.type == self.event:
            if not self.keydown:
                print(f'{self.start_time * 1000 =}')
                print(f'{delta_time * 1000 =}')
                elapsed_time = ((delta_time * 1000) - (self.start_time * 1000))
                print(elapsed_time)
                
                sprite.spritecollide(self, GameContext.notes_group, True)
                self.note_intersected = False
                pygame.time.set_timer(self.event, 0)
                    
        if self.note_intersected and not note_intersection:
            # miss
            self.note_intersected = False

    def change_keybind(self, key: str) -> None:
        self.key = pygame.key.key_code(key)
    
    def draw(self, key_type: CircleKeySpriteType | ArrowKeySpriteType | BarKeySpriteType, surface: pygame.Surface) -> None:
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
