from typing import Any

import pygame
from pygame.sprite import Sprite


class Slider(Sprite):
    """
    A sprite for a slider. WIP.
    
    Inheritance Use:
        Sprite.draw(screen: pygame.Surface) -> None:
            Not implemented yet.
            
        Sprite.update(delta_time: float) -> None:
            Not implemented yet.
    """
    def __init__(self, x_pos: int, y_pos: int, value: Any, scale: int, step: int, *groups,
                 screen_hint: pygame.Surface | None = None):
        super().__init__(*groups)
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.delta = value
        self.scale = scale
        self.step = step

    def increment(self, event) -> None:
        raise NotImplementedError("Not implemented yet..")
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     ...

    def draw(self, surface: pygame.Surface) -> None:
        raise NotImplementedError("Not implemented yet..")
        # ...
        
    def update(self, delta_time: float) -> None:
        raise NotImplementedError("Not implemented yet..")
    