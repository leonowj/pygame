from resources import *


class Text:
    def __init__(self, text, text_color, pc_x, pc_y, font_size, font_family):
        self.text = str(text)
        self.text_color = text_color
        self.pc_x = pc_x
        self.pc_y = pc_y
        self.font_size = font_size
        self.font_family = font_family

        self.font = pygame.font.SysFont(self.font_family, self.font_size)
        self.image = self.font.render(self.text, True, self.text_color)
        self.rect = self.image.get_rect()
        self.rect.center = pc_x, pc_y

    # wyświetlanie tekstu
    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Button:
    def __init__(self, text, text_color, background_color, width, height, pc_x, pc_y, font_size, font_family):
        self.text = Text(text, text_color, pc_x, pc_y, font_size, font_family)
        self.background_color = background_color
        self.width = width
        self.height = height

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.text.rect.center

    # rysowanie przycisku
    def draw(self, surface):
        surface.fill(self.background_color, self.rect)
        self.text.draw(surface)

