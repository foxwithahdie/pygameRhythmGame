# imports-start-hotreload
import pygame

import constants as constants
import game_context as game_context
import helpers as helpers
import settings as settings
from key_sprite import KeySprite, CircleKeySpriteType, ArrowKeySpriteType, BarKeySpriteType
from note_sprite import NoteSprite, CircleSpriteType, ArrowSpriteType, BarSpriteType

# imports-end-hotreload

# globals-start-hotreload
global player_keys


# globals-end-hotreload


def main() -> None:
    global player_keys
    pygame.init()

    pygame.display.set_caption(constants.WINDOW_TITLE)

    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    context = game_context.GameContext()

    player_keys = []

    player_keys.extend([KeySprite(CircleKeySpriteType.YELLOW, 1, "d",
                                  context.key_group, screen_hint=screen),
                        KeySprite(CircleKeySpriteType.RED, 2, "f",
                                  context.key_group, screen_hint=screen),
                        KeySprite(CircleKeySpriteType.PURPLE, 3, "j",
                                  context.key_group, screen_hint=screen),
                        KeySprite(CircleKeySpriteType.BLUE, 4, "k",
                                  context.key_group, screen_hint=screen)
                        ])

    NoteSprite(CircleSpriteType.BLUE,
               helpers.key_padding(
                   CircleKeySpriteType.BLUE) + (CircleKeySpriteType.BLUE.key_size // 2) + constants.KEY_SPACING * 3,
               context.notes_group, surface_hint=screen)

    while running:
        # init-start-hotreload
        delta_time = clock.tick(settings.fps) / 1000.0
        running = game_loop(screen, delta_time, context)
        pygame.display.flip()
        # init-end-hotreload


# loop-start-hotreload
def game_loop(screen: pygame.Surface, delta_time: float, context: game_context.GameContext) -> bool:
    """
    The main loop of the game.
    :param screen: The screen to draw on.
    :param delta_time: The time delta between the previous two frames, in seconds.
    :param context: The current game context.
    :return: Whether the game should continue running.
    """
    global player_keys

    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                return False
        if game_context.game_active:
            for key in player_keys:
                key.press_button(event, delta_time)

    screen.fill(constants.BACKGROUND_COLOR)

    if game_context.game_active:
        for key in player_keys:
            key.draw(key.key_type, screen)
        context.notes_group.draw(screen)
        context.notes_group.update(delta_time)

    return True


# loop-end-hotreload


if __name__ == '__main__':
    main()
