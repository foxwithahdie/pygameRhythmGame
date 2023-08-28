import pygame
import constants
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

    NoteSprite(NoteSpriteType.BLUE, constants.SCREEN_WIDTH / 2, context.notes_group, surface_hint=screen)

    KeySprite(KeySpriteType.YELLOW, constants.SCREEN_WIDTH / 5, context.notes_group, screen_hint=screen)
    KeySprite(KeySpriteType.RED, constants.SCREEN_WIDTH / 5 * 2, context.notes_group, screen_hint=screen)
    KeySprite(KeySpriteType.PURPLE, constants.SCREEN_WIDTH / 5 * 3, context.notes_group, screen_hint=screen)
    KeySprite(KeySpriteType.BLUE, constants.SCREEN_WIDTH / 5 * 4, context.notes_group, screen_hint=screen)

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

    context.notes_group.update(delta_time)

    screen.fill(constants.BACKGROUND_COLOR)
    context.notes_group.draw(screen)

    return True


if __name__ == '__main__':
    main()
