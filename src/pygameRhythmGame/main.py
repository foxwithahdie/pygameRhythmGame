# imports-start-hotreload

import pygame

import constants
import game_context
import settings
from key_sprite import KeySprite
from note_sprite import NoteSprite, NoteData
from map_conversion import MapConverter, Map

import os

# imports-end-hotreload

# globals-start-hotreload

global player_keys

# globals-end-hotreload


def main() -> None:
    global player_keys
    pygame.init()
    pygame.mixer.init()

    pygame.display.set_caption(constants.WINDOW_TITLE)

    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT), pygame.RESIZABLE)
    clock = pygame.time.Clock()
    running = True
    context = game_context.GameContext()
    
    # NoteSprite(NoteData.from_dict({"column": 1, "time": 5, "type": True}), context.test_group)

    player_keys = [
            KeySprite(1, "d", context.key_group, screen_hint=screen),
            KeySprite(2, "f", context.key_group, screen_hint=screen),
            KeySprite(3, "j", context.key_group, screen_hint=screen),
            KeySprite(4, "k", context.key_group, screen_hint=screen)
    ]

    critical_crystal: Map = MapConverter.map_conversion(
        os.path.join("seiryu__critical_crystal_Seiryu__SanadaYukimura",
                     "seiryu__critical_crystal_Seiryu__SanadaYukimura__[Normal].osu"
                     )
    )
    critical_crystal.change_song("critical_crystal.mp3")
    critical_crystal.song.play()
    while running:
        # init-start-hotreload
        
        delta_time = clock.tick(settings.fps) / 1000.0
        
        running = game_loop(screen, delta_time, critical_crystal)
        pygame.display.flip()
        
        # init-end-hotreload


# loop-start-hotreload

def game_loop(screen: pygame.Surface, delta_time: float, song_map: Map) -> bool:
    """
    The main loop of the game.
    :param screen: The screen to draw on.
    :param delta_time: The time delta between the previous two frames, in seconds.
    :param song_map: The map currently being played. Test parameter.
    :return: Whether the game should continue running.
    """
    global player_keys
    
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                return False
        if game_context.game_active:
            player_keys[0].press_button(event, song_map.group, delta_time)
            player_keys[1].press_button(event, song_map.group, delta_time)
            player_keys[2].press_button(event, song_map.group, delta_time)
            player_keys[3].press_button(event, song_map.group, delta_time)

    screen.fill(constants.BACKGROUND_COLOR)

    if game_context.game_active:
        for key in player_keys:
            key.draw(screen)
            
        song_map.group.draw(screen)
        song_map.group.update(delta_time)


    return True

# loop-end-hotreload


if __name__ == '__main__':
    main()
