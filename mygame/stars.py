import random
from resources import *


# Klasa animacji
class Stars:
    def __init__(self):
        self.stars = []
        self.image = IMAGES['STAR']
        self.width = self.image.get_rect().width
        self.height = self.image.get_rect().height

    # dodawanie nowych gwiazd
    def add_stars(self):
        pos_x = screen.get_rect().center[0] - self.width / 2
        pos_y = screen.get_rect().center[1] - self.height / 2
        direction_x = random.randint(-4, 6)
        direction_y = random.randint(-4, 6)
        lifetime = random.randint(4, 6)
        star_rect = pygame.Rect(int(pos_x), int(pos_y), self.width, self.height)
        self.stars.append([star_rect, direction_x, direction_y, lifetime])

    # usuwanie gwiazd
    def _delete_stars(self):
        self.stars = [star for star in self.stars if star[3] > 0]

    # rysowanie gwiazd
    def draw(self, surface):
        if self.stars:
            self._delete_stars()
            for star in self.stars:
                star[0].x += star[1]
                star[0].y += star[2]
                star[3] -= 0.01
                surface.blit(self.image, star[0])



