from resources import *
import random
from tile import Tile


# Klasa planszy
class GameBoard:
    def __init__(self):
        self.tiles_group = pygame.sprite.Group()

    # tworzenie planszy
    def create_board(self):
        tile_images = [IMAGES[name] for name in IMAGES if "TILE" in name]
        tile_images *= 6
        random.shuffle(tile_images)

        tile_images_count = len(tile_images)
        tile_index = 0
        z_cor = 0
        board_offset_x = (WINDOW_WIDTH - BOARD_WIDTH) // 2.137
        board_offset_y = (WINDOW_HEIGHT - BOARD_HEIGHT) // 2

        for layer in range(7, 2, -2):
            z_cor += 1
            for col in range(layer):
                for row in range(layer - 1):
                    tile_image = tile_images[tile_index % tile_images_count]
                    tile_rect = tile_image.get_rect()
                    tile_rect.x = board_offset_x + (col * TILE_WIDTH) + ((z_cor-1) * TILE_WIDTH)
                    tile_rect.y = board_offset_y + (row * TILE_HEIGHT) + ((z_cor-1) * TILE_HEIGHT)

                    tile = Tile(tile_image, tile_rect, z_cor)   # kompozycja
                    self.tiles_group.add(tile)
                    tile_index += 1
        # top layer
        z_cor += 1
        for row in range(2):
            for col in range(2):
                tile_image = tile_images[tile_index % tile_images_count]
                tile_rect = tile_image.get_rect()
                tile_rect.x = board_offset_x + (col * TILE_WIDTH) + ((z_cor - 1) * TILE_WIDTH) - TILE_WIDTH / 2
                tile_rect.y = board_offset_y + (row * TILE_HEIGHT) + ((z_cor - 2) * TILE_HEIGHT)

                tile = Tile(tile_image, tile_rect, z_cor)
                self.tiles_group.add(tile)
                tile_index += 1

    # rysowanie planszy
    def draw(self, surface):
        for tile in self.tiles_group:
            if tile.matched:
                continue
            adjusted_x = tile.rect.x - tile.z*5
            adjusted_y = tile.rect.y - tile.z*5
            surface.blit(tile.image, (adjusted_x, adjusted_y))




