from Paiter import Painter
import math
import pygame


class Entity(object):
    def __init__(self, idintification, pos, size, speed, img=None):
        self.id = idintification
        self.pos = [pos[0], pos[1]]
        self.speed = speed
        if type(img) is str:
            self.img = pygame.image.load(img)
        else:
            self.img = img
        self.size = size
        self.rect = pygame.Rect(self.get_pos(), self.size)

        self.time = 0
        self.rotation = False

    def get_pos(self):
        return list(self.pos)

    def get_rect(self):
        return self.rect

    def get_id(self):
        return self.id

    def get_center(self):
        center = (self.pos[0] - self.size[0] / 2, self.pos[1] - self.size[1] / 2)
        return center

    def set_pos(self, pos):
        self.pos = pos

    def rotor(self, b):
        if b is self.rotation:
            return
        self.img = pygame.transform.flip(self.img, True, False)
        self.rotation = not self.rotation

    def move(self):
        self.time += 1
        Painter.image(self.img, self.get_center())

    def seek_target(self, destination):
        checker = 0
        dx = self.pos[0] - destination[0]
        dy = self.pos[1] - destination[1]
        ddx, ddy = 0, 0

        if dx > 0:
            self.rotor(True)
        if dx < 0:
            self.rotor(False)

        if abs(dx) > abs(dy):
            if dx != 0:
                ddy = abs(dy / dx)
                ddx = (1 - ddy)
            else:
                ddy = 1
                ddx = (1 - ddy)
        else:
            if dy != 0:
                ddx = abs(dx / dy)
                ddy = (1 - ddx)
            else:
                ddx = 1
                ddy = (1 - ddx)

        if abs(dx) > self.speed:
            ddx = self.speed * ddx * math.copysign(1, dx)
            self.pos[0] = self.pos[0] - ddx
        else:
            checker += 1
            self.pos[0] = destination[0]

        if abs(dy) > self.speed:
            ddy = self.speed * ddy * math.copysign(1, dy)
            self.pos[1] = self.pos[1] - ddy
        else:
            checker += 1
            self.pos[1] = destination[1]

        if checker == 2:
            return self.explosion()

        self.rect.update(self.get_center(), self.size)
        self.move()

    def explosion(self):
        return self.death()

    def death(self):
        pass
