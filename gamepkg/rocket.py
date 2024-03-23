import random
from gamepkg import WIDTH, HEIGHT
from gamepkg.surfaces import rocket_animation
import pygame
from pygame.sprite import Sprite


class Rocket(Sprite):
    def __init__(self, group):
        super(Rocket, self).__init__()
        self.add(group)
        self.rocket_surfaces = rocket_animation()
        self.image = next(self.rocket_surfaces)
        self.rect = self.image.get_rect(topleft=(random.randrange(0, WIDTH), 0))
        self.rocket_speed = random.randrange(1, 6)
        try:
            pygame.mixer.Sound("sounds/text.mp3").play().set_volume(0.2)
        except AttributeError as e:
            pass

    def update(self, *args, **kwargs):
        self.image = next(self.rocket_surfaces)
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.rect.y = self.rect.y + self.rocket_speed
        if self.rect.y > HEIGHT:
            self.kill()

    def collide(self, ship_rect):
        if bool(
            abs(ship_rect.x - self.rect.x) < self.image.get_width() - 20 and
            abs(ship_rect.y - self.rect.y) < self.image.get_height()
        ):
            return True
        else:
            return False