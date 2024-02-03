import pygame
from typing import Union, Any
from pygame.sprite import Sprite
import helpers


class Slider(Sprite):
    def __init__(self, x_pos: int, y_pos: int, value: Any, scale: int, step: int, *groups,
                 screen_hint: Union[pygame.Surface, None] = None):
        super().__init__()
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.changing_value = value
        self.scale = scale
        self.step = step

    def increment(self, event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN:
            ...

    def draw(self, surface: pygame.Surface) -> None:
        ...
    