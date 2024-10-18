from typing import NoReturn
from enum import Enum

from sprite_types import *
import constants


class Lane(Enum):
    """
    An enum for representing a particular lane. Condenses the spacing for each lane depending on the key type.
    """
    YELLOW_LANE = 1
    PURPLE_LANE = 2
    RED_LANE = 3
    BLUE_LANE = 4
    
    @property
    def circle_x_position(self) -> int:
        match self:
            case Lane.YELLOW_LANE:
                return key_padding(CircleKeySpriteType.YELLOW) + (CircleKeySpriteType.YELLOW.key_size // 2) + constants.KEY_SPACING * 0
            case Lane.PURPLE_LANE:
                return key_padding(CircleKeySpriteType.PURPLE) + (CircleKeySpriteType.PURPLE.key_size // 2) + constants.KEY_SPACING * 1
            case Lane.RED_LANE:
                return key_padding(CircleKeySpriteType.RED) + (CircleKeySpriteType.RED.key_size // 2) + constants.KEY_SPACING * 2
            case Lane.BLUE_LANE:
                return key_padding(CircleKeySpriteType.BLUE) + (CircleKeySpriteType.BLUE.key_size // 2) + constants.KEY_SPACING * 3
            case _:
                raise ValueError("Invalid lane color!")
            
    @property
    def arrow_x_position(self) -> int:
        match self:
            case Lane.YELLOW_LANE:
                return key_padding(ArrowKeySpriteType.YELLOW) + (ArrowKeySpriteType.YELLOW.key_size(1) // 2) + constants.KEY_SPACING * 0
            case Lane.PURPLE_LANE:
                return key_padding(ArrowKeySpriteType.PURPLE) + (ArrowKeySpriteType.PURPLE.key_size(2) // 2) + constants.KEY_SPACING * 1
            case Lane.RED_LANE:
                return key_padding(ArrowKeySpriteType.RED) + (ArrowKeySpriteType.RED.key_size(3) // 2) + constants.KEY_SPACING * 2
            case Lane.BLUE_LANE:
                return key_padding(ArrowKeySpriteType.BLUE) + (ArrowKeySpriteType.BLUE.key_size(4) // 2) + constants.KEY_SPACING * 3
            case _:
                raise ValueError("Invalid lane color!")
    
    @property
    def bar_x_position(self) -> int:
        match self:
            case Lane.YELLOW_LANE:
                return key_padding(BarKeySpriteType.YELLOW) + (BarKeySpriteType.YELLOW.key_size // 2) + constants.KEY_SPACING * 0
            case Lane.PURPLE_LANE:
                return key_padding(BarKeySpriteType.PURPLE) + (BarKeySpriteType.PURPLE.key_size // 2) + constants.KEY_SPACING * 1
            case Lane.RED_LANE:
                return key_padding(BarKeySpriteType.RED) + (BarKeySpriteType.RED.key_size // 2) + constants.KEY_SPACING * 2
            case Lane.BLUE_LANE:
                return key_padding(BarKeySpriteType.BLUE) + (BarKeySpriteType.BLUE.key_size // 2) + constants.KEY_SPACING * 3
            case _:
                raise ValueError("Invalid lane color!")


class NoteConfig:
    """
    A class holding static values and methods for configuring what notes types are on screen,
    and parsing those into their note types.
    """
    key_config: list[str] = ["y-circle", "r-circle", "b-circle", "p-circle"]
    note_config: list[str] = ["y-circle", "r-circle", "b-circle", "p-circle"]
    
    @staticmethod
    def parse_note_config(conf: str) -> CircleSpriteType | ArrowSpriteType | BarSpriteType | NoReturn:
        conf_split: list[str] = conf.split("-")
        if conf_split[-1] == "circle":
            match conf_split[0]:
                case "y":
                    return CircleSpriteType.YELLOW
                case "b":
                    return CircleSpriteType.BLUE
                case "r":
                    return CircleSpriteType.RED
                case "p":
                    return CircleSpriteType.PURPLE
                case _:
                    raise ValueError("Invalid note color!")
        elif conf_split[-1] == "bar":
            match conf_split[0]:
                case "y":
                    return BarSpriteType.YELLOW
                case "b":
                    return BarSpriteType.BLUE
                case "r":
                    return BarSpriteType.RED
                case "p":
                    return BarSpriteType.PURPLE
                case _:
                    raise ValueError("Invalid note color!")
        elif conf_split[-1] == "arrow":
            match conf_split[0]:
                case "y":
                    return ArrowSpriteType.YELLOW
                case "b":
                    return ArrowSpriteType.BLUE
                case "r":
                    return ArrowSpriteType.RED
                case "p":
                    return ArrowSpriteType.PURPLE
                case _:
                    raise ValueError("Invalid note color!")
        else:
            raise ValueError("Invalid note type!")
        
    @staticmethod
    def parse_key_config(conf: str) -> CircleKeySpriteType | ArrowKeySpriteType | BarKeySpriteType | NoReturn:
        conf_split: list[str] = conf.split("-")
        if conf_split[-1] == "circle":
            match conf_split[0]:
                case "y":
                    return CircleKeySpriteType.YELLOW
                case "b":
                    return CircleKeySpriteType.BLUE
                case "r":
                    return CircleKeySpriteType.RED
                case "p":
                    return CircleKeySpriteType.PURPLE
                case _:
                    raise ValueError("Invalid note color!")
        elif conf_split[-1] == "bar":
            match conf_split[0]:
                case "y":
                    return BarKeySpriteType.YELLOW
                case "b":
                    return BarKeySpriteType.BLUE
                case "r":
                    return BarKeySpriteType.RED
                case "p":
                    return BarKeySpriteType.PURPLE
                case _:
                    raise ValueError("Invalid note color!")
        elif conf_split[-1] == "arrow":
            match conf_split[0]:
                case "y":
                    return ArrowKeySpriteType.YELLOW
                case "b":
                    return ArrowKeySpriteType.BLUE
                case "r":
                    return ArrowKeySpriteType.RED
                case "p":
                    return ArrowKeySpriteType.PURPLE
                case _:
                    raise ValueError("Invalid note color!")
        else:
            raise ValueError("Invalid note type!")
