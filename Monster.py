import math
from Entity import Entity
from Hitbox_Manager import Hitbox_Manager

class Monster(Entity):

    def __init__(self, id, pos, size, img=None, img_revert=None):
        super().__init__(id, pos, size, img)
        self.upgrade_counter = 0
        self.speed = 1
        self.hp = 5
        self.xp = self.hp
        self.dmg = 1
        self.img_revert = img_revert
        Hitbox_Manager.add_mob(self)
        self.destination = [0,0]

    def take_dmg(self, dmg):
        self.hp += -dmg
        if self.hp < 1:
            return self.death()
        return False
    def get_dmg(self):
        return self.dmg

    def death(self):
        # print("moster death", self.id)
        Hitbox_Manager.take_xp_player(self.xp)
        Hitbox_Manager.remove_mob(self.id)
        return True

    def act(self):

        self.destination = Hitbox_Manager.get_player(0).get_pos()

        checker = 0
        dx = self.pos[0] - self.destination[0]
        dy = self.pos[1] - self.destination[1]
        ddx, ddy = 0, 0

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
            self.pos[0] = self.destination[0]

        if abs(dy) > self.speed:
            ddy = self.speed * ddy * math.copysign(1, dy)
            self.pos[1] = self.pos[1] - ddy
        else:
            checker += 1
            self.pos[1] = self.destination[1]

        if checker == 2:
            return self.explosion()

        # self.rect.move_ip(-ddx, -ddy)
        self.rect.update( self.get_center(), self.size)
        # self.rect.center = self.pos
        self.move()

        return False

    def explosion(self):
        return self.death()