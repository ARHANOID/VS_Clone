from Paiter import Painter
import pygame, sys, math


class Button():
    def __init__(self, color, x, y, img, text):
        self.color = color
        self.x = x
        self.y = y
        self.text = text
        self.img = img
        self.rect = pygame.Rect((self.x, self.y), self.img.get_size())
        self.draw()

    def draw(self):
        Painter.image(self.img, (self.x, self.y))

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 30)
            text = font.render(self.text, 1, (255, 255, 255))
            pos = (self.x + (self.img.get_size()[0] / 2 - text.get_width() / 2),
                   self.y + (self.img.get_size()[1] / 2 - text.get_height() / 2))

            Painter.draw_raw_text(text, pos)

    def is_mouseover(self):
        pos = pygame.mouse.get_pos()
        return self.rect.collidepoint(pos)
