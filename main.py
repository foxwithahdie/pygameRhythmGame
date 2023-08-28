import pygame as pyg
import constants


def main():
    pyg.init()

    pyg.display.set_caption(constants.WINDOW_TITLE)

    screen = pyg.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pyg.time.Clock()
    running = True

    while running:
        delta_time = clock.tick(constants.FPS) / 1000.0
        running = game_loop(screen, delta_time)
        pyg.display.flip()


def game_loop(screen: pyg.Surface, delta_time: float) -> bool:
    """
    The main loop of the game.
    :param screen: The screen to draw on.
    :param delta_time: The time delta between the previous two frames, in seconds.
    :return: Whether the game should continue running.
    """

    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            return False

    screen.fill(constants.BACKGROUND_COLOR)

    return True


if __name__ == '__main__':
    main()
