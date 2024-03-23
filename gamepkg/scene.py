import random

import pygame

from gamepkg import WIDTH, HEIGHT
from gamepkg.surfaces import earth_animation
from pygame.image import load


stars_surface = [load("graphics/star_0.png").convert_alpha()] * 10 + [
    load("graphics/star_1.png").convert_alpha(),
    load("graphics/star_2.png").convert_alpha()
]
earth_surfaces = earth_animation()


def get_scene():
    stars_number = 30
    stars_density = 1

    rnd_star = []
    for n in range(stars_number):
        rnd_star.append(
            (
                random.choice(stars_surface),
                random.randrange(0, WIDTH, stars_density),
                random.randrange(0, HEIGHT, stars_density)
            )
        )
    earth_surface = next(earth_surfaces)
    return rnd_star, earth_surface
