import pygame

import config.constants
import game_context
import config.settings
from game_types.key_sprite import KeySprite
from game_types.map_conversion import MapConverter, Map

import os

global player_keys


def main() -> None:
    """
    Main entry point of the program.
    """
    global player_keys
    pygame.init()
    pygame.mixer.init()

    pygame.display.set_caption(config.constants.WINDOW_TITLE)

    screen = pygame.display.set_mode((config.constants.SCREEN_WIDTH, config.constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    context = game_context.GameContext()

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
        
        delta_time = clock.tick(config.settings.fps) / 1000.0
        
        running = game_loop(screen, delta_time, critical_crystal)
        pygame.display.flip()


def game_loop(screen: pygame.Surface, delta_time: float, song_map: Map) -> bool:
    """The main loop of the game separated into a function.

    WIP.
    
    Args:
        screen (pygame.Surface): Where all the game parts are drawn.
        delta_time (float): The time it takes for a frame to draw.
        song_map (Map): The map that is being played. Test parameter.

    Returns:
        bool: Whether to continue running the game or not.
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

    screen.fill(config.constants.BACKGROUND_COLOR)

    if game_context.game_active:
        for key in player_keys:
            key.draw(screen)
            
        song_map.group.draw(screen)
        song_map.group.update(delta_time)


    return True


if __name__ == '__main__':
    main()
