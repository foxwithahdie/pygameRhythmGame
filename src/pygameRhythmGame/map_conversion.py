import math
from typing import Optional, Any
from zipfile import ZipFile
import os
import shutil

import constants
from note_sprite import Lane

# column 1 - x - math.floor(x * total_amount_of_columns / 512)

# column 2 - y - does not affect

# column 3 - time when object is supposed to be hit

# column 4 - type of note - if 1 or 5, regular note, else hold note

# column 5 - hit sound - skip

# column 6 - end of hold note if it is a hold note

class Map:
    ...

class MapConverter:
    
    @staticmethod
    def column(x_value: int) -> int:
        return math.floor(x_value * constants.TOTAL_COLUMNS / 512)
    
    @staticmethod
    def map_conversion(map_file: str) -> Map:
        hit_objects_str: list[str] = MapConverter.extract_hit_objects_string(map_file)
        hit_objects_dict_list: list[dict[str, Any]] = MapConverter.extract_hit_objects(hit_objects_str)
        
        return Map()
        
    @staticmethod
    def extract_osz_file(map_file: str) -> str:
        """Extracts the osz file into a folder, deletes all of the extraneous sound files and moves the song file to the sounds folder.

        Args:
            map_file (str): The filename of the osz file.

        Returns:
            str: The folder name.
        """
        folder_file_name: str = map_file[:map_file.rfind(".")]
        song_file: str = ""
        with ZipFile(os.path.join("Maps", map_file), "r") as osz_file:
            os.mkdir(os.path.join("Maps", folder_file_name))
            osz_file.extractall(os.path.join("Maps", folder_file_name))
        
        song_folder_files: list[str] = [ file for file in os.listdir(os.path.join("Maps", folder_file_name)) 
                                        if os.path.isfile(os.path.join(os.path.join("Maps", folder_file_name), file)) ]
        
        for file in song_folder_files:
            if file.endswith("mp3"):
                song_file = file
            
            if file.endswith("wav") or file.endswith("jpg"):
                os.remove(os.path.join("Maps", folder_file_name, file))
        
        shutil.move(os.path.join("Maps", folder_file_name, song_file), "Sounds")
        
        return folder_file_name
    
    @staticmethod
    def extract_hit_objects_string(map_file: str) -> list[str]:
        hit_objects: list[str] = []
        with open(os.path.join("Maps", map_file), "r") as file:
            flag = False
            for line in file.readlines():
                if flag:
                    hit_objects.append(line[:-1])
                if "[HitObjects]" in line:
                    flag = True
        return hit_objects
    
    @staticmethod
    def extract_hit_objects(hit_objects_strings: list[str]) -> list[dict[str, Any]]:
        hit_objects_list: list[dict[str, Any]] = []
        for hit_object in hit_objects_strings:
            hit_object_values: list[str] = hit_object[:hit_object.find(":")].split(",")
            hit_object_dict: dict[str, Any] = {
                specifier: value for specifier, value in zip(
                    ["column", "y", "time", "type", "hit_sound", "hold_note_time"],
                    hit_object_values
                ) if specifier != "y" or specifier != "hit_sound"
            }
            hit_object_dict["type"] = True if hit_object_dict["type"] == 128 else False
            hit_object_dict["column"] = MapConverter.column(hit_object_dict["column"])
            hit_objects_list.append(hit_object_dict)
            
        return hit_objects_list
            

class NoteData:
    def __init__(self, column: int, time: int, type: Optional[bool] = None, hold_note_time: Optional[int] = None):
        """_summary_

        Args:
            column (int): _description_
            time (int): _description_
            type (Optional[bool], optional): _description_. Defaults to None.
            hold (Optional[bool], optional): _description_. Defaults to None.
        """
        ...    