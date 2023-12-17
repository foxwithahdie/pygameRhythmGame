import pygame


class GameContext:
    """
    The GameContext class is used to store the current game state.
    """

    notes_group: pygame.sprite.Group = pygame.sprite.Group()
    settings: pygame.sprite.Group = pygame.sprite.Group()
