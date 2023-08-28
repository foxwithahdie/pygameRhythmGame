import pygame
import constants


def main():
    pygame.init()

    pygame.display.set_caption(constants.WINDOW_TITLE)

    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True

    while running:
        delta_time = clock.tick(constants.FPS) / 1000.0
        running = game_loop(screen, delta_time)


def game_loop(screen: pygame.Surface, delta_time: float) -> bool:
    """
    The main loop of the game.
    :param screen: The screen to draw on.
    :param delta_time: The time delta between the previous two frames, in seconds.
    :return: Whether the game should continue running.
    """

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        
    return True


if __name__ == '__main__':
    main()
