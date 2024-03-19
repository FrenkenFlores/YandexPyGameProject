import sys
import pygame
import random
import time

FPS = 60
WIDTH = 800
HEIGHT = 600


def update_background():
    space_surface = pygame.Surface((WIDTH, HEIGHT))
    space_surface.fill(color=(0, 0, 0))
    stars_surface = [pygame.image.load("graphics/star_0.png").convert()] * 10 + [
        pygame.image.load("graphics/star_1.png").convert(),
        pygame.image.load("graphics/star_2.png").convert()
    ]
    stars_number = 30
    stars_density = 1
    screen.blit(space_surface, (0, 0))
    for n in range(stars_number):
        screen.blit(
            random.choice(stars_surface),
            (
                random.randrange(0, WIDTH, stars_density),
                random.randrange(0, HEIGHT, stars_density)
            )
        )


def main():
    random.seed = 1
    clock = pygame.time.Clock()
    tmp_time = time.time()
    # Create a regular surface.
    update_background()
    earth_surface = pygame.image.load("graphics/earth.png").convert()
    title_text = pygame.font.Font("fonts/Pixeltype.ttf", 50)
    title_text_surface = title_text.render('E-Defender', False, (255, 255, 255))

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
            update_background()
        # BLIT - Block Image Transfer - put one surface on another surface.
        screen.blit(earth_surface, (
            (WIDTH - earth_surface.get_width()) / 2, (HEIGHT - earth_surface.get_height()) / 2)
        )
        screen.blit(title_text_surface, (
                (WIDTH - title_text_surface.get_width()) / 2,
                (HEIGHT - title_text_surface.get_height() - earth_surface.get_height() - 100) / 2
            )
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
