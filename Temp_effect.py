from Entity import Entity
from Hitbox_Manager import Hitbox_Manager
import pygame


class Temp_effect(Entity):
    def __init__(self, life_time, id, pos, size, speed, img):
        super().__init__(id, pos, size, speed, img)

        self.life_time = life_time
        self.collapse = True
        Hitbox_Manager.add_temp_effect(self)
        self.size = self.img.get_size()

    def act(self):
        if self.life_time < 1:
            Hitbox_Manager.remove_temp_effect(self)
            return
        self.life_time += -1
        if self.collapse:
            self.size = (self.size[0] / 1.05, self.size[1] / 1.05)
            self.img = pygame.transform.scale(self.img, self.size)

        self.move()

        return None
