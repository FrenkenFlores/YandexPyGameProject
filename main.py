import os
import sys
import pygame
import random
import time
from gamepkg.surfaces import (
    earth_animation,
    rocket_animation,
    ship_animation
)
from gamepkg import (
    FPS,
    WIDTH,
    HEIGHT
)


def main():
    random.seed = 42
    clock = pygame.time.Clock()
    tmp_time = time.time()
    game_over = False
    game_start = False
    # Create a regular surface.
    space_surface = pygame.Surface((WIDTH, HEIGHT))
    space_surface.fill(color=(25, 15, 35))
    ship_speed = 10
    text = pygame.font.Font("fonts/Pixeltype.ttf", 50)
    stars_surface = [pygame.image.load("graphics/star_0.png").convert_alpha()] * 10 + [
        pygame.image.load("graphics/star_1.png").convert_alpha(),
        pygame.image.load("graphics/star_2.png").convert_alpha()
    ]
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
    earth_surfaces = earth_animation()
    rocket_surfaces = rocket_animation()
    ship_surfaces = ship_animation()
    ship_surface = next(ship_surfaces)
    ship_rect = ship_surface.get_rect(
        midbottom=(WIDTH / 2, HEIGHT - 100)
    )
    earth_surface = next(earth_surfaces)
    title_text_surface = text.render('E-Defender', False, (255, 255, 255))
    start_text_surface = text.render('Press space to start', False, (200, 200, 255))
    end_text_surface = text.render('Game over', False, (255, 150, 150))
    rockets_num = 1
    rockets_speed = 5
    rockets_cords = [(random.randrange(0, WIDTH), 0) for _ in range(rockets_num)]
    update_rocket_cords = False
    pygame.mixer.Sound("sounds/Adventure.mp3").play(-1)
    button_sound = pygame.mixer.Sound("sounds/text.mp3")
    rocket_sound = pygame.mixer.Sound("sounds/rocket.mp3")
    rocket_sound.set_volume(0.2)
    while True:
        # Add exit code.
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and ship_rect.x > 0 and not game_over:
                    ship_rect.x -= ship_speed
                if event.key == pygame.K_RIGHT and ship_rect.x < WIDTH and not game_over:
                    ship_rect.x += ship_speed
                if event.key == pygame.K_UP and ship_rect.y > 0 and not game_over:
                    ship_rect.y -= ship_speed
                if event.key == pygame.K_DOWN and ship_rect.y < HEIGHT and not game_over:
                    ship_rect.y += ship_speed
                if event.key == pygame.K_SPACE and (not game_start or game_over):
                    button_sound.play()
                    game_start = True
                    game_over = False
                    rockets_num = 1
                    rockets_cords = [(random.randrange(0, WIDTH), 0) for _ in range(rockets_num)]
                    rocket_sound.play()
                    update_rocket_cords = False
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
        # Change the background effects every second.
        if time.time() - tmp_time > 1:
            # Save time.
            tmp_time = time.time()
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
        # Draw objects.
        # BLIT - Block Image Transfer - put one surface on another surface.
        screen.blit(space_surface, (0, 0))
        for (star, x, y) in rnd_star:
            screen.blit(star, (x, y))
        screen.blit(earth_surface, (
            (WIDTH - earth_surface.get_width()) / 2, (HEIGHT - earth_surface.get_height()) / 2)
        )
        screen.blit(text.render(f'Level  {rockets_num}', False, (150, 255, 255)), (
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
        ship_rect_tmp_x, ship_rect_tmp_y = (ship_rect.x, ship_rect.y)
        ship_surface = next(ship_surfaces)
        ship_rect = ship_surface.get_rect()
        ship_rect.x, ship_rect.y = ship_rect_tmp_x, ship_rect_tmp_y
        if not game_over and game_start:
            for i in range(len(rockets_cords)):
                x, y = rockets_cords[i][0], rockets_cords[i][1]
                if y == HEIGHT:
                    update_rocket_cords = True
                rocket_surface = next(rocket_surfaces)
                screen.blit(rocket_surface, (x, y))
                if (abs(ship_rect.x - x) < rocket_surface.get_width() - 20 and
                        abs(ship_rect.y - y) < rocket_surface.get_height()):
                    game_over = True
                rockets_cords[i] = (x, y + rockets_speed)
        if update_rocket_cords:
            rockets_num += 1
            rockets_cords = [(random.randrange(0, WIDTH), 0) for _ in range(rockets_num)]
            update_rocket_cords = False
            rocket_sound.play()
        screen.blit(ship_surface, ship_rect)
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
