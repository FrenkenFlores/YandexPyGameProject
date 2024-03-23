import math
import sys
import pygame
import random
import time

from gamepkg.ship import Ship
from gamepkg import (
    FPS,
    WIDTH,
    HEIGHT
)
from gamepkg.rocket import Rocket
from gamepkg.rockets_group import RocketsGroup


def main():
    from gamepkg.scene import get_scene
    clock = pygame.time.Clock()
    pygame.time.set_timer(pygame.USEREVENT, 2000)
    # Set game control vars.
    game_over = False
    game_start = False
    # Create a regular surface.
    space_surface = pygame.Surface((WIDTH, HEIGHT))
    space_surface.fill(color=(25, 15, 35))
    # Set texts.
    text = pygame.font.Font("fonts/Pixeltype.ttf", 50)
    title_text_surface = text.render('E-Defender', False, (255, 255, 255))
    start_text_surface = text.render('Press space to start', False, (200, 200, 255))
    end_text_surface = text.render('Game over', False, (255, 150, 150))
    # Set sounds.
    pygame.mixer.Sound("sounds/Adventure.mp3").play(-1)
    button_sound = pygame.mixer.Sound("sounds/text.mp3")
    rockets_group = RocketsGroup()
    ship = Ship()
    rnd_star, earth_surface = get_scene()
    tmp_time = 0
    while True:
        # Change the background effects every second.
        if time.time() - tmp_time > 1:
            rnd_star, earth_surface = get_scene()
            tmp_time = time.time()
        # Add exit code.
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT and game_start and not game_over:
                for _ in range(rockets_group.rockets_number):
                    Rocket(rockets_group)
                rockets_group.increment_rockets_number()
            if event.type == pygame.KEYDOWN:
                if not game_over:
                    ship.update(event=event)
                if event.key == pygame.K_SPACE and (not game_start or game_over):
                    button_sound.play()
                    game_start = True
                    game_over = False
                    rockets_group = RocketsGroup()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
        # BLIT - Block Image Transfer - put one surface on another surface.
        screen.blit(space_surface, (0, 0))
        for (star, x, y) in rnd_star:
            screen.blit(star, (x, y))
        screen.blit(earth_surface, (
            (WIDTH - earth_surface.get_width()) / 2, (HEIGHT - earth_surface.get_height()) / 2)
        )
        screen.blit(text.render(f'Level  {rockets_group.rockets_number}', False, (150, 255, 255)), (
                WIDTH - 150,
                50
            )
        )
        if not game_start or game_over:
            screen.blit(title_text_surface, (
                    (WIDTH - title_text_surface.get_width()) / 2,
                    (HEIGHT - title_text_surface.get_height() - earth_surface.get_height() - 100) / 2
                )
            )
            screen.blit(start_text_surface, (
                    (WIDTH - start_text_surface.get_width()) / 2,
                    (HEIGHT - start_text_surface.get_height() - earth_surface.get_height() + 300) / 2
                )
            )
        if game_over:
            screen.blit(end_text_surface, (
                    (WIDTH - end_text_surface.get_width()) / 2,
                    (HEIGHT - end_text_surface.get_height() - earth_surface.get_height() + 600) / 2
                )
            )
        if not game_over and game_start:
            rockets_group.draw(screen)
            rockets_group.update()
        if rockets_group.check_collide(ship.rect):
            game_over = True
        screen.blit(ship.image, ship.rect)
        ship.update()
        # Update the main screen.
        pygame.display.update()
        # Should not run faster than FPS frames peer second.
        clock.tick(FPS)


if __name__ == "__main__":
    pygame.init()
    # Set the display surface.
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('E-Defender')
    pygame.display.set_icon(pygame.image.load("graphics/ship/ship_1.png"))
    main()
