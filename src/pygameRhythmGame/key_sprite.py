import time
from typing import Optional

import pygame
from game_context import GameContext
from note_config import NoteConfig
import pygame.sprite as sprite
from sprite_types import *

import constants
import helpers


class KeySprite(sprite.Sprite):
    """
    A sprite representing the key that the user presses.
    """
    def __init__(self, note_pos: int, key: str, *groups, screen_hint: Optional[pygame.Surface] = None):
        super().__init__(*groups)
        self.key_type = NoteConfig.parse_key_config(NoteConfig.key_config[note_pos - 1])
        self.note_pos = note_pos
        key_spacing = constants.KEY_SPACING * (note_pos - 1)
        if isinstance(self.key_type, ArrowKeySpriteType):
            self.x_pos = key_padding(self.key_type, arrow_dir=note_pos) + (self.key_type.key_size(note_pos) // 2)
            self.x_pos += key_spacing
        else:
            self.x_pos = key_padding(self.key_type) + (self.key_type.key_size // 2) + key_spacing

        if screen_hint is not None:
            self.image = helpers.transform_image(
                pygame.image.load(self.key_type.grey_key_image).convert_alpha(screen_hint), (2 / 3)
            )
        else:
            self.image = helpers.transform_image(
                pygame.image.load(self.key_type.grey_key_image).convert_alpha(), (2 / 3)
            )
        self.rect: pygame.Rect = self.image.get_rect(center=(self.x_pos,  key_direction()))
        self.key: int = pygame.key.key_code(key)
        self.event = pygame.event.custom_type()
        self.keydown: bool = False
        self.note_intersected: bool = False
        self.start_time: float = 0.0

    def press_button(self, event: pygame.event.Event, group: pygame.sprite.Group, delta_time: float) -> None:
        
        note_intersection = sprite.spritecollide(self, group, False)  # type: ignore
        
        if note_intersection and not self.note_intersected:
            self.note_intersected = True
            self.start_time = time.time()
            #print(f'at note_intersection: {self.start_time}') # debug
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
                self.rect.center = (self.x_pos, key_direction())
        if event.type == pygame.KEYUP:
            self.keydown = False
            self.rect.center = (self.x_pos, key_direction())
        if event.type == self.event:
            if not self.keydown:
                #print(f'{self.start_time * 1000 =}ms') # debug
                #print(f'{delta_time * 1000 =}ms') # debug
                elapsed_time = ((time.time()) - (self.start_time))
                #print(f"{elapsed_time = }") # debug
                
                sprite.spritecollide(self, group, True) # type: ignore
                self.note_intersected = False
                pygame.time.set_timer(self.event, 0)
                    
        if self.note_intersected and not note_intersection:
            # miss
            self.note_intersected = False

    def change_keybind(self, key: str) -> None:
        self.key = pygame.key.key_code(key)
    
    def draw(self, surface: pygame.Surface) -> None:
        """Draws the key onto the surface.

        Args:
            key_type (CircleKeySpriteType | ArrowKeySpriteType | BarKeySpriteType): The type of key that would be drawn, so you can draw the different images based on if it is pressed.
            surface (pygame.Surface): Where to draw the key.
        """
        key_type = type(self.key_type)
        match self.key_type:
            case key_type.YELLOW: key_type = key_type.YELLOW
            case key_type.BLUE: key_type = key_type.BLUE
            case key_type.RED: key_type = key_type.RED
            case key_type.PURPLE: key_type = key_type.PURPLE
            case _:
                raise ValueError("Invalid key type!")
            
        if self.keydown:
            self.image = helpers.transform_image(
                pygame.image.load(self.key_type.dull_key_image).convert_alpha(surface), (2 / 3)
            )
            self.rect = self.image.get_rect(center=(self.x_pos, key_direction()))
            surface.blit(self.image, self.rect)
        else:
            self.image = helpers.transform_image(
                pygame.image.load(key_type.grey_key_image).convert_alpha(surface), (2 / 3)
            )
            self.rect = self.image.get_rect(center=(self.x_pos, key_direction()))
            surface.blit(self.image, self.rect)
