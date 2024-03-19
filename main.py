import sys
import pygame
import random
import time

FPS = 60
WIDTH = 800
HEIGHT = 600


def main():
    random.seed = 1
    clock = pygame.time.Clock()
    tmp_time = time.time()
    # Create a regular surface.
    space_surface = pygame.Surface((WIDTH, HEIGHT))
    space_surface.fill(color=(15, 15, 15))
    screen.blit(space_surface, (0, 0))
    earth_surface = pygame.image.load("graphics/earth.png")
    stars_surface = [pygame.image.load("graphics/star_0.png")] * 10 + [
        pygame.image.load("graphics/star_1.png"),
        pygame.image.load("graphics/star_2.png")
    ]
    stars_number = 30
    stars_density = 1
    while True:
        # Add exit code.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
        # Draw objects.
        if time.time() - tmp_time > 3:
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
        # BLIT - Block Image Transfer - put one surface on another surface.
        screen.blit(earth_surface, (
            (WIDTH - earth_surface.get_width()) / 2, (HEIGHT - earth_surface.get_height()) / 2)
        )
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
