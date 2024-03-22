import os
import pygame


def earth_animation():
    while True:
        for _, _, files in os.walk('graphics/earth'):
            for frame in files:
                yield pygame.image.load(f"graphics/earth/{frame}").convert_alpha()


def rocket_animation():
    while True:
        for _, _, files in os.walk('graphics/rocket'):
            for frame in files:
                rocket_surface = pygame.image.load(f"graphics/rocket/{frame}").convert_alpha()
                yield pygame.transform.rotate(rocket_surface, 180)


def ship_animation():
    while True:
        for _, _, files in os.walk('graphics/ship'):
            for frame in files:
                yield pygame.image.load(f"graphics/ship/{frame}").convert_alpha()
