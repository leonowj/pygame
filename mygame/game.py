from gameboard import GameBoard
from resources import *


# Klasa rozgrywki
class Game(GameBoard):
    def __init__(self):
        super().__init__()
        self.selected_tile = None
        self.game_over = False
        self.victory = False

    # wybieranie płytki
    def select_tile(self, pos):
        selected_tile = None
        for tile in self.tiles_group:
            if tile.rect.collidepoint(pos) and not tile.matched and not tile.is_blocked(self.tiles_group):
                if not selected_tile or tile.z > selected_tile.z:
                    selected_tile = tile
        if selected_tile:
            if self.selected_tile:
                self._check_match(selected_tile)
            else:
                self.selected_tile = selected_tile

    # dopasowywanie płytek
    def _check_match(self, tile):
        if self.selected_tile.image == tile.image and self.selected_tile != tile:
            self.selected_tile.matched = True
            tile.matched = True
            match_sound.play()
        self.selected_tile = None

        if self._board_blocked():
            self.game_over = True

        if all(tile.matched for tile in self.tiles_group):
            self.victory = True

    # sprawdzanie, czy plansza jest zablokowana
    def _board_blocked(self):
        unmatched_tiles = [tile for tile in self.tiles_group if not tile.matched]

        for tile1 in unmatched_tiles:
            for tile2 in unmatched_tiles:
                if tile1 != tile2 and tile1.image == tile2.image and not tile1.is_blocked(self.tiles_group) and not tile2.is_blocked(self.tiles_group):
                    return False

        return True
