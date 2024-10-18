import math
from typing import Optional, Any
from zipfile import ZipFile
import os
import shutil

import constants
from note_sprite import NoteData, NoteSprite
import pygame.mixer

class Map:
    """
    A class representing a map. It contains all of the notes in order of when they will be created, and a song tied to the map.
    """
    def __init__(self, hit_objects_list: list[NoteData], song: Optional[str] = None):
        if song is not None:
            self.song: pygame.mixer.Sound = pygame.mixer.Sound(os.path.join("Sounds", song))
        hit_objects_sprites: list[NoteSprite] = [NoteSprite(note_data) for note_data in hit_objects_list]
        self.group = pygame.sprite.Group(*hit_objects_sprites)
    
    def change_song(self, song: str) -> None:
        """Changes the song that the map plays.

        Args:
            song (str): The song file name.
        """
        self.song = pygame.mixer.Sound(os.path.join("Sounds", song))

class MapConverter:
    
    @staticmethod
    def column(x_value: int) -> int:
        """Returns the column (1, 2, etc) of the note depending on the x value in the map file.

        Args:
            x_value (int): The x value in the map file.

        Returns:
            int: The column corresponding to the x value.
        """
        return math.floor(x_value * constants.TOTAL_COLUMNS / 512)
    
    @staticmethod
    def map_conversion(map_file: str) -> Map:
        """Converts a map file into a Map object.

        Args:
            map_file (str): The file name of the map.

        Returns:
            Map: The map object with all of the notes created for it in place.
        """
        hit_objects_str: list[str] = MapConverter.extract_hit_objects_string(map_file)
        hit_objects_list: list[NoteData] = list(map(NoteData.from_dict, MapConverter.extract_hit_objects(hit_objects_str)))
        
        return Map(hit_objects_list)
        
    @staticmethod
    def extract_osz_file(map_file: str) -> str:
        """Extracts the osz file into a folder, deletes all the extraneous sound files and moves the song file to the sounds folder.

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
        """Extracts the list of the comma-separated strings in the map file of the note information.
        Args:
            map_file (str): The map file name.

        Returns:
            list[str]: The list of the comma-separated strings with all of the note information.
        """
        hit_objects: list[str] = []
        with open(os.path.join("Maps", map_file), "r", encoding="utf8") as file:
            flag = False
            for line in file.readlines():
                if flag:
                    hit_objects.append(line[:-1])
                if "[HitObjects]" in line:
                    flag = True
        return hit_objects
    
    @staticmethod
    def extract_hit_objects(hit_objects_strings: list[str]) -> list[dict[str, Any]]:
        """Converts all of the comma-separated note information into a list of dictionaries containing the note information.

        Args:
            hit_objects_strings (list[str]): The comma-separated note information in a list.

        Returns:
            list[dict[str, Any]]: A list of dictionaries of the note information, split up by column, time, type and if it is a hold note, hold note time.
        """
        hit_objects_list: list[dict[str, Any]] = []
        for hit_object in hit_objects_strings:
            hit_object_values: list[str] = hit_object[:hit_object.find(":")].split(",")
            hit_object_dict: dict[str, Any] = {
                specifier: int(value) for specifier, value in zip(
                    ["column", "y", "time", "type", "hit_sound", "hold_note_time"],
                    hit_object_values
                ) if specifier != "y" or specifier != "hit_sound"
            }
            hit_object_dict["type"] = True if hit_object_dict["type"] == 128 else False
            hit_object_dict["column"] = MapConverter.column(hit_object_dict["column"])
            hit_objects_list.append(hit_object_dict)
            
        return hit_objects_list
 