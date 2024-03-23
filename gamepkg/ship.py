from pygame.sprite import Sprite
from gamepkg.surfaces import ship_animation
from gamepkg import WIDTH, HEIGHT
from pygame import (
    K_LEFT,
    K_UP,
    K_RIGHT,
    K_DOWN
)


class Ship(Sprite):
    def __init__(self):
        super(Ship, self).__init__()
        self.ship_surfaces = ship_animation()
        self.image = next(self.ship_surfaces)
        self.rect = self.image.get_rect(topleft=((WIDTH - self.image.get_width()) / 2, HEIGHT - 100))
        self.speed = 10

    def update(self, *args, **kwargs):
        if 'event' in kwargs:
            event = kwargs['event']
            if event.key == K_LEFT and self.rect.x > 0:
                self.rect.x -= self.speed
            if event.key == K_RIGHT and self.rect.x < WIDTH:
                self.rect.x += self.speed
            if event.key == K_UP and self.rect.y > 0:
                self.rect.y -= self.speed
            if event.key == K_DOWN and self.rect.y < HEIGHT:
                self.rect.y += self.speed
        self.image = next(self.ship_surfaces)
        self.rect = self.image.get_rect(topleft=(
            self.rect.x, self.rect.y
        ))
