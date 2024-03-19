import sys

import pygame

FPS = 60


def main():
    clock = pygame.time.Clock()
    w, h = 100, 200
    # Create a regular surface.
    test_surface = pygame.Surface((w, h))
    test_surface.fill(color=(255, 255, 255))
    while True:
        # Add exit code.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
        # Draw objects.
        # BLIT - Block Image Transfer - put one surface on another surface.
        screen.blit(test_surface, (200, 100))
        # Update the main screen.
        pygame.display.update()
        # Should not run faster than FPS frames peer second.
        clock.tick(FPS)


if __name__ == "__main__":
    pygame.init()
    width = 800
    height = 400
    # Set the display surface.
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Game')
    main()
