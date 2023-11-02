from resources import *


# Klasa pojedynczej płytki
class Tile(pygame.sprite.Sprite):
    def __init__(self, image, rect, z):
        super().__init__()
        self.image = image
        self.rect = rect
        self.z = z
        self.matched = False
        self.border_color = None
        self.border_width = 0

    # sprawdzanie, czy płytka jest zablokowana
    def is_blocked(self, tiles_group):
        right_blocked = False
        left_blocked = False

        for tile in tiles_group:
            if not tile.matched:
                if (tile.z > self.z and tile.rect.x + TILE_WIDTH / 2 == self.rect.x and tile.rect.y == self.rect.y) or \
                        (tile.z > self.z and tile.rect.x - TILE_WIDTH / 2 == self.rect.x and tile.rect.y == self.rect.y) or \
                        (tile.z > self.z and tile.rect.x == self.rect.x and tile.rect.y == self.rect.y):
                    return True

                if tile.z == self.z and tile.rect.y == self.rect.y:  # na tej samej wysokości i na tym samym poziomie Y
                    if tile.rect.x == self.rect.x + TILE_WIDTH:
                        right_blocked = True
                    if tile.rect.x + TILE_WIDTH == self.rect.x:
                        left_blocked = True

        return right_blocked and left_blocked



