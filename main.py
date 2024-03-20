import os
import sys
import pygame
import random
import time

FPS = 60
WIDTH = 800
HEIGHT = 600

def earth_animation():
    while True:
        for _, _, files in os.walk('graphics/earth'):
            for frame in files:
                yield pygame.image.load(f"graphics/earth/{frame}").convert_alpha()


def main():
    random.seed = 42
    clock = pygame.time.Clock()
    tmp_time = time.time()
    # Create a regular surface.
    space_surface = pygame.Surface((WIDTH, HEIGHT))
    space_surface.fill(color=(25, 15, 35))
    screen.blit(space_surface, (0, 0))
    stars_surface = [pygame.image.load("graphics/star_0.png").convert_alpha()] * 10 + [
        pygame.image.load("graphics/star_1.png").convert_alpha(),
        pygame.image.load("graphics/star_2.png").convert_alpha()
    ]
    stars_number = 30
    stars_density = 1
    for n in range(stars_number):
        screen.blit(
            random.choice(stars_surface),
            (
                random.randrange(0, WIDTH, stars_density),
                random.randrange(0, HEIGHT, stars_density)
            )
        )
    earth_surfaces = earth_animation()
    earth_surface = next(earth_surfaces)
    title_text = pygame.font.Font("fonts/Pixeltype.ttf", 50)
    title_text_surface = title_text.render('E-Defender', False, (255, 255, 255))
    # ship_surface = pygame.image.load("graphics/ship.png")
    # ship_rec = ship_surface.get_rect(midbottom=(33, 33))
    ships_num = 1
    ships_cords = [(random.randrange(0, WIDTH), random.randrange(0, HEIGHT)) for _ in range(ships_num)]
    while True:
        # Add exit code.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
        # Draw objects.
        if time.time() - tmp_time > 1:
            # Save time.
            tmp_time = time.time()
            screen.blit(space_surface, (0, 0))
            for n in range(stars_number):
                screen.blit(
                    random.choice(stars_surface),
                    (
                        random.randrange(0, WIDTH, stars_density),
                        random.randrange(0, HEIGHT, stars_density)
                    )
                )
            earth_surface = next(earth_surfaces)
        # BLIT - Block Image Transfer - put one surface on another surface.
        screen.blit(earth_surface, (
            (WIDTH - earth_surface.get_width()) / 2, (HEIGHT - earth_surface.get_height()) / 2)
        )
        screen.blit(title_text_surface, (
                (WIDTH - title_text_surface.get_width()) / 2,
                (HEIGHT - title_text_surface.get_height() - earth_surface.get_height() - 100) / 2
            )
        )
        for i in range(len(ships_cords)):
            ship_surface = pygame.image.load("graphics/ship.png").convert_alpha()
            pygame.transform.rotate(ship_surface, 44)
            screen.blit(ship_surface, ships_cords[i])
            ships_cords[i] = (ships_cords[i][0] + 1, ships_cords[i][1] + 1)
        # Update the main screen.
        pygame.display.update()
        # Should not run faster than FPS frames peer second.
        clock.tick(FPS)



if __name__ == "__main__":
    pygame.init()
    # Set the display surface.
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('E-Defender')
    main()
