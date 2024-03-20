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
    game_over = False
    game_start = False
    # Create a regular surface.
    space_surface = pygame.Surface((WIDTH, HEIGHT))
    space_surface.fill(color=(25, 15, 35))
    ship_surface = pygame.image.load("graphics/ship.png").convert_alpha()
    ship_rect = ship_surface.get_rect(
        midbottom=(WIDTH / 2, HEIGHT - 100)
    )
    ship_speed = 10
    rocket_surface = pygame.image.load("graphics/rocket.png").convert_alpha()
    rocket_surface = pygame.transform.rotate(rocket_surface, 180)
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
    earth_surface = next(earth_surfaces)
    title_text = pygame.font.Font("fonts/Pixeltype.ttf", 50)
    title_text_surface = title_text.render('E-Defender', False, (255, 255, 255))
    start_text = pygame.font.Font("fonts/Pixeltype.ttf", 50)
    start_text_surface = start_text.render('Press space to start', False, (200, 200, 255))
    end_text = pygame.font.Font("fonts/Pixeltype.ttf", 50)
    end_text_surface = end_text.render('Game over', False, (255, 150, 150))
    level_text = pygame.font.Font("fonts/Pixeltype.ttf", 50)
    rockets_num = 1
    rockets_speed = 5
    rockets_cords = [(random.randrange(0, WIDTH), 0) for _ in range(rockets_num)]
    update_rocket_cords = False
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
                    game_start = True
                    game_over = False
                    rockets_num = 1
                    rockets_cords = [(random.randrange(0, WIDTH), 0) for _ in range(rockets_num)]
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
        for i in rnd_star:
            screen.blit(i[0], (i[1], i[2]))
        screen.blit(earth_surface, (
            (WIDTH - earth_surface.get_width()) / 2, (HEIGHT - earth_surface.get_height()) / 2)
        )
        screen.blit(level_text.render(f'Level  {rockets_num}', False, (150, 255, 255)), (
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
            for i in range(len(rockets_cords)):
                x, y = rockets_cords[i][0], rockets_cords[i][1]
                if y == HEIGHT:
                    update_rocket_cords = True
                screen.blit(rocket_surface, (x, y))
                if (abs(ship_rect.x - x) < rocket_surface.get_width() - 20 and
                        abs(ship_rect.y - y) < rocket_surface.get_height()):
                    game_over = True
                rockets_cords[i] = (x, y + rockets_speed)
        if update_rocket_cords:
            rockets_num += 1
            rockets_cords = [(random.randrange(0, WIDTH), 0) for _ in range(rockets_num)]
            update_rocket_cords = False
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
