from typing import Any

import pygame
import pygame.sprite as sprite

from note_config import NoteConfig, Lane
from sprite_types import *


class NoteData:
    def __init__(self, column: int, time: int, type: bool, hold_note_time: Optional[int] = None):
        """_summary_

        Args:
            column (int): _description_
            time (int): _description_
            type (Optional[bool], optional): _description_. Defaults to None.
            hold (Optional[bool], optional): _description_. Defaults to None.
        """
        column += 1
        match column:
            case 1:
                self.lane = Lane.YELLOW_LANE
            case 2:
                self.lane = Lane.PURPLE_LANE
            case 3:
                self.lane = Lane.RED_LANE
            case 4:
                self.lane = Lane.BLUE_LANE
            case _:
                raise ValueError("Invalid column. Check math in map_conversion.py")
            
        self.time = time
        self.type = type
        if hold_note_time is not None:
            self.hold_note_time = hold_note_time
        
    @classmethod
    def from_dict(cls, dict: dict[str, Any]):
        return NoteData(dict["column"], dict["time"], dict["type"], hold_note_time=dict.get("hold_note_time"))


class NoteSprite(sprite.Sprite):
    """
    A sprite representing a falling note.
    """
        
    def __init__(self, note_data: NoteData, *groups, surface_hint: Optional[pygame.Surface] = None):
        super().__init__(*groups)
        self.note_data = note_data
        self.note_type = NoteConfig.parse_note_config(NoteConfig.note_config[self.note_data.lane.value - 1])
        if surface_hint is not None:
            self.image = pygame.image.load(self.note_type.note_image).convert_alpha(surface_hint)
        else:
            self.image = pygame.image.load(self.note_type.note_image).convert_alpha()
        self.image = pygame.transform.scale(self.image, helpers.scale_size(self.image.get_size(), 2 / 3))
        start_pos = note_start_pos() + (-1 if settings.downscroll else 1) * (constants.SCROLL_SPEED * self.note_data.time / 1000.0)
        # print(start_pos)
        if isinstance(self.note_type, CircleSpriteType):
            self.x_pos = self.note_data.lane.circle_x_position
        elif isinstance(self.note_type, ArrowSpriteType):
            self.x_pos = self.note_data.lane.arrow_x_position
        elif isinstance(self.note_type, BarSpriteType):
            self.x_pos = self.note_data.lane.bar_x_position
        else:
            raise ValueError("Note type not an existing type!")
        self.rect = self.image.get_rect(center=(self.x_pos, start_pos))

    def update(self, delta_time: float) -> None:
        buffer = 100
        if settings.downscroll:
            self.rect.centery += int(delta_time * constants.SCROLL_SPEED)
        else:
            self.rect.centery -= int(delta_time * constants.SCROLL_SPEED)
        
        passes_bottom: bool = self.rect.centery - self.note_type.note_size - buffer >= constants.SCREEN_WIDTH
        passes_top: bool = self.rect.centery + self.note_type.note_size + buffer <= 0
        
        if (passes_bottom and settings.downscroll) or (passes_top and not settings.downscroll):
            #print(f"{self.rect.centery = }, {self.note_type.note_size = }, {self.rect.centery + self.note_type.note_size = }")
            #print(f"{passes_bottom and settings.downscroll = }, {passes_top and not settings.downscroll = }")
            sprite.Sprite.kill(self)
