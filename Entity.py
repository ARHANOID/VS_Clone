from Paiter import Painter
import pygame

class Entity(object):
    def __init__(self, idintification, pos, size, img=None):
        self.id = idintification
        self.pos = [pos[0], pos[1]]
        self.size = size
        self.rect = pygame.Rect(self.get_pos(), self.size)
        self.img = pygame.image.load(img)

        self.time = 0

        # size = self.img.get_size()
        # rect = self.img.get_rect()
        # print(idintification, size)
        # print(idintification, rect)

    def get_pos(self):
        return list(self.pos)
    def get_rect(self):
        return self.rect
    def get_id(self):
        return self.id
    def get_center(self):
        center = (self.pos[0] - self.size[0]/2, self.pos[1] - self.size[1]/2)
        return center

    def set_pos(self, pos):
        self.pos = pos

    def move(self):
        self.time += 1
        Painter.image(self.img, self.get_center())





