from pygame.sprite import Group


class RocketsGroup(Group):
    def __init__(self):
        super(RocketsGroup, self).__init__()
        self.rockets_number = 1

    def increment_rockets_number(self):
        self.rockets_number += 1

    def check_collide(self, ship_rect):
        for i in self.sprites():
            if i.collide(ship_rect):
                return True
