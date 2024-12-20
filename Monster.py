from Paiter import Painter
from Entity import Entity
from Temp_effect import Temp_effect
from Hitbox_Manager import Hitbox_Manager
import pygame


class Monster(Entity):

    def __init__(self, id, pos, data):
        self.img_revert = None
        self.text_r_img = data[6]
        super().__init__(id, pos, (data[1], data[1]), data[2], data[5])
        self.upgrade_counter = 0
        self.hp = data[3]
        self.xp = self.hp
        self.dmg = data[4]
        # self.img_revert = pygame.image.load(self.text_r_img)
        self.destination = [0, 0]
        self.death_timer = 15

        Hitbox_Manager.add_mob(self)

    def take_dmg(self, dmg):
        self.hp += -dmg
        if self.hp < 1:
            return self.explosion()
        return False

    def get_dmg(self):
        return self.dmg

    def del_img(self):
        self.img = None
        self.img_revert = None

    def set_img(self):
        if type(self.text_img) is str:
            self.img = pygame.image.load(self.text_img)
        else:
            self.img = self.text_img
        self.img_revert = pygame.image.load(self.text_r_img)

    def death(self):
        Hitbox_Manager.take_xp_player(self.xp)
        Hitbox_Manager.remove_mob(self.id)
        if self.rotation:
            self.rotation = not self.rotation
            self.img_revert = pygame.transform.flip(self.img_revert, True, False)
        Temp_effect(200, self.id, self.pos, self.size, 0, self.img_revert)
        return True

    def explosion(self):
        return self.death()

    def act(self):
        self.destination = Hitbox_Manager.get_player(0).get_pos()
        self.seek_target(self.destination)
        return False
