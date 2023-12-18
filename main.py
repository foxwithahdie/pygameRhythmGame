import pygame
import constants
import helpers
from game_context import GameContext
from key_sprite import KeySprite, KeySpriteType
from note_sprite import NoteSprite, NoteSpriteType


def main():
    pygame.init()

    pygame.display.set_caption(constants.WINDOW_TITLE)

    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True

    context = GameContext()

    NoteSprite(NoteSpriteType.BLUE, constants.SCREEN_WIDTH // 2, context.notes_group, surface_hint=screen)
    
    global player_keys
    player_keys = []
    
    global player_key_x_pos
    player_key_x_pos = []
    
    key_1: KeySprite = KeySprite(KeySpriteType.YELLOW, helpers.key_padding(screen) + constants.KEY_SPACING,
                                 "d", context.notes_group, screen_hint=screen)
    key_2: KeySprite = KeySprite(KeySpriteType.RED, helpers.key_padding(screen) + (constants.KEY_SPACING * 2),
                                 "f", context.notes_group, screen_hint=screen)
    key_3: KeySprite = KeySprite(KeySpriteType.PURPLE, helpers.key_padding(screen) + (constants.KEY_SPACING * 3),
                                 "j", context.notes_group, screen_hint=screen)
    key_4: KeySprite = KeySprite(KeySpriteType.BLUE, helpers.key_padding(screen) + (constants.KEY_SPACING * 4),
                                 "k", context.notes_group, screen_hint=screen)
    
    player_keys.append(key_1); player_keys.append(key_2)
    player_keys.append(key_3); player_keys.append(key_4)
    player_key_x_pos.append(key_1.x_pos); player_key_x_pos.append(key_2.x_pos)
    player_key_x_pos.append(key_3.x_pos); player_key_x_pos.append(key_4.x_pos)

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
        if event.type == pygame.QUIT:
            return False
        for key in player_keys:
            key.press_button(event)
    screen.fill(constants.BACKGROUND_COLOR)
    context.notes_group.update(delta_time)

    
    for key in player_keys:
        key.draw(key.key_type, screen)
    context.notes_group.draw(screen)
    return True


if __name__ == '__main__':
    main()
