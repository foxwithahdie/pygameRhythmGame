import pygame

import constants
import game_context
import helpers
import settings
from key_sprite import KeySprite, CircleKeySpriteType, ArrowKeySpriteType, BarKeySpriteType
from note_sprite import NoteSprite, CircleSpriteType, ArrowSpriteType, BarSpriteType


def main(app) -> None:
    pygame.init()

    pygame.display.set_caption(constants.WINDOW_TITLE)

    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    context = game_context.GameContext()

    app.player_keys = []
    
    key_1: KeySprite = KeySprite(CircleKeySpriteType.YELLOW, 1, "d",
                                 context.key_group, screen_hint=screen)
    key_2: KeySprite = KeySprite(CircleKeySpriteType.RED, 2, "f",
                                 context.key_group, screen_hint=screen)
    key_3: KeySprite = KeySprite(CircleKeySpriteType.PURPLE, 3, "j",
                                 context.key_group, screen_hint=screen)
    key_4: KeySprite = KeySprite(CircleKeySpriteType.BLUE, 4, "k",
                                 context.key_group, screen_hint=screen)

    app.player_keys.extend([key_1, key_2, key_3, key_4])

    NoteSprite(CircleSpriteType.BLUE,
               helpers.key_padding(
                   CircleKeySpriteType.BLUE) + (CircleKeySpriteType.BLUE.key_size // 2) + constants.KEY_SPACING * 3,
               context.notes_group, surface_hint=screen)

    while running:
        delta_time = clock.tick(settings.fps) / 1000.0
        running = game_loop(app, screen, delta_time, context)
        pygame.display.flip()


def game_loop(app: game_context.AppScope, screen: pygame.Surface, delta_time: float, context: game_context.GameContext) -> bool:
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
        if game_context.game_active:
            for key in app.player_keys:
                key.press_button(event, delta_time)
            
    screen.fill(constants.BACKGROUND_COLOR)
    
    if game_context.game_active:
        for key in app.player_keys:
            key.draw(key.key_type, screen)
        context.notes_group.draw(screen)
        context.notes_group.update(delta_time)

    return True


if __name__ == '__main__':
    app = game_context.AppScope()
    main(app)
