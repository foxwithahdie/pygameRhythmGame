import pygame
import constants
import helpers
from game_context import GameContext
from key_sprite import KeySprite, KeySpriteType
from note_sprite import NoteSprite, NoteSpriteType

# player_keys: list[KeySprite], player_key_x_pos: list[int]
global player_keys, player_key_x_pos


def main() -> None:
    pygame.init()

    pygame.display.set_caption(constants.WINDOW_TITLE)

    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    context = GameContext()

    global player_keys, player_key_x_pos

    NoteSprite(NoteSpriteType.BLUE, constants.SCREEN_WIDTH // 2, context.notes_group, surface_hint=screen)
    
    player_keys = []
    
    player_key_x_pos = []
    
    key_1: KeySprite = KeySprite(KeySpriteType.YELLOW, (helpers.key_padding() + constants.CIRCLE_KEY_WIDTH // 2),
                                 "d", context.key_group, screen_hint=screen)
    key_2: KeySprite = KeySprite(KeySpriteType.RED, 
                                 (helpers.key_padding() + constants.CIRCLE_KEY_WIDTH // 2 + constants.KEY_SPACING),
                                 "f", context.key_group, screen_hint=screen)
    key_3: KeySprite = KeySprite(KeySpriteType.PURPLE, 
                                 (helpers.key_padding() + constants.CIRCLE_KEY_WIDTH // 2 + constants.KEY_SPACING * 2),
                                 "j", context.key_group, screen_hint=screen)
    key_4: KeySprite = KeySprite(KeySpriteType.BLUE, 
                                 (helpers.key_padding() + constants.CIRCLE_KEY_WIDTH // 2 + constants.KEY_SPACING * 3),
                                 "k", context.key_group, screen_hint=screen)
    
    player_keys.append(key_1)
    player_keys.append(key_2)
    player_keys.append(key_3)
    player_keys.append(key_4)
    
    while running:
        delta_time = clock.tick(constants.FPS) / 1000.0
        running = game_loop(screen, delta_time, context)
        pygame.display.flip()


def game_loop(screen: pygame.Surface, delta_time: float, context: GameContext) -> bool:
    """
    The main loop of the game.
    :param screen: The screen to draw on.
    :param delta_time: The time delta between the previous two frames, in seconds.
    :param context: The current game context.
    :return: Whether the game should continue running.
    """

    for event in pygame.event.get():   
        match event.type:
            case pygame.QUIT:
                return False
        for key in player_keys:
            key.press_button(event)
            
    screen.fill(constants.BACKGROUND_COLOR)
    context.notes_group.draw(screen)
    
    for key in player_keys:
        key.draw(key.key_type, screen)

    context.notes_group.update(delta_time)
    
    return True


if __name__ == '__main__':
    main()
