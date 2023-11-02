from text import Text, Button
from stars import *
from game import Game


# Konkretyzacja obiektów
game = Game()
star = Stars()
mahjong_text = Text("Welcome to Mahjong!", YELLOW, *screen.get_rect().center, 100, 'Cooper Black')
victory_text = Text("VICTORY!", BROWN, *screen.get_rect().center, 120, 'Cooper Black')
game_over_text = Text("GAME OVER", BROWN, *screen.get_rect().center, 120, 'Cooper Black')
new_game = Button("NEW GAME", INDIGO, WHITE, 300, 80, screen.get_rect().centerx - 200, screen.get_rect().centery + 130, 40, 'Cooper Black')
exit_game = Button("EXIT GAME", INDIGO, WHITE, 300, 80, screen.get_rect().centerx + 200, screen.get_rect().centery + 130, 40, 'Cooper Black')

window_open = True
active_game = False

while window_open:
    # Pętla zdarzeń
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                window_open = False
        elif not active_game:
            # Menu
            screen.fill(BACKGROUND)
            mahjong_text.draw(screen)
            new_game.draw(screen)
            exit_game.draw(screen)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_game.rect.collidepoint(pygame.mouse.get_pos()):
                    window_open = False
                elif new_game.rect.collidepoint(pygame.mouse.get_pos()):
                    active_game = True
                    first_click = True
                    screen.fill(BACKGROUND)
                    game.create_board()
                    game.draw(screen)
        # Rozgrywka
        if active_game:
            if event.type == pygame.MOUSEBUTTONDOWN and not first_click:
                pos = pygame.mouse.get_pos()
                game.select_tile(pos)
                screen.fill(BACKGROUND)
                game.draw(screen)

            # Wygrana
            if game.victory:
                screen.fill(BACKGROUND)
                if event.type == ANIMATION_EVENT:
                    star.add_stars()
                star.draw(screen)
                victory_text.draw(screen)
                if not victory_music_played:
                    victory_music.play()
                    victory_music_played = True
                new_game.draw(screen)
                exit_game.draw(screen)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if exit_game.rect.collidepoint(pygame.mouse.get_pos()):
                        window_open = False
                    elif new_game.rect.collidepoint(pygame.mouse.get_pos()):
                        active_game = True
                        screen.fill(BACKGROUND)
                        game = Game()
                        game.create_board()
                        game.draw(screen)
                        game.victory = False
                        victory_music_played = False

            # Przegrana
            if game.game_over and not game.victory:
                screen.fill(BACKGROUND)
                game_over_text.draw(screen)
                if not game_over_music_played:
                    game_over_music.play()
                    game_over_music_played = True
                new_game.draw(screen)
                exit_game.draw(screen)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if exit_game.rect.collidepoint(pygame.mouse.get_pos()):
                        window_open = False
                    elif new_game.rect.collidepoint(pygame.mouse.get_pos()):
                        active_game = True
                        screen.fill(BACKGROUND)
                        game = Game()
                        game.create_board()
                        game.draw(screen)
                        game.game_over = False
                        game_over_music_played = False
        # Ramka dla zaznaczonej płytki
        if game.selected_tile:
            adjusted_x = game.selected_tile.rect.x - game.selected_tile.z*5
            adjusted_y = game.selected_tile.rect.y - game.selected_tile.z*5
            border_rect = pygame.Rect(adjusted_x, adjusted_y, TILE_WIDTH, TILE_HEIGHT)
            pygame.draw.rect(screen, RED, border_rect, 3)

        first_click = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
