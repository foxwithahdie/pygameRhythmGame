import pygame


class GameContext:
    """
    The GameContext class is used to store the current game state.
    """

    notes_group: pygame.sprite.Group = pygame.sprite.Group()
    key_group: pygame.sprite.Group = pygame.sprite.Group()
    settings: pygame.sprite.Group = pygame.sprite.Group()
    song_selection: pygame.sprite.Group = pygame.sprite.Group()
    main_menu: pygame.sprite.Group = pygame.sprite.Group()
    