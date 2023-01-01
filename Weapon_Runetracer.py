from Weapon import Weapon
from Hitbox_Manager import Hitbox_Manager
import Config
import random


class Weapon_Runetracer(Weapon):

    def __init__(self, id, data):
        super().__init__(id, data)

        self.offset = 0
        self.proj_arrey = []

    def act(self):
        self.time += 1
        if self.burst < self.projectils:
            if self.time % int(
                    (self.cooldown / self.cooldown_inc) / ((self.projectils + self.projectils_inc) * 3)) == 0:
                self.burst += 1
                self.base_mechanic()
        else:
            if self.time % (self.cooldown / self.cooldown_inc) == 0:
                self.burst = 0

        for proj in self.proj_arrey:
            pos = proj.get_pos()
            if Hitbox_Manager.do_proj_exist(proj):
                if self.colide_with_border(pos):
                    target = self.spawn_mob()
                    proj.set_destination(target)
            else:
                self.proj_arrey.remove(proj)

    def colide_with_border(self, x_y):
        x, y = x_y
        if x < 0:
            return True
        if x >= Config.W_w:
            return True
        if y < 0:
            return True
        if y >= Config.W_h:
            return True
        return False

    def spawn_mob(self):
        offset = 500
        n = Config.W_w * 2 + Config.W_h * 2
        r = random.randint(0, n)
        if r < Config.W_w:
            x, y = r, 0 - offset
        elif r < (Config.W_w + Config.W_h):
            x, y = Config.W_w + offset, r - Config.W_w
        elif r < (Config.W_h * 2 + Config.W_w):
            x, y = r - Config.W_w + Config.W_h, Config.W_h + offset
        else:
            x, y = 0 - offset, r - Config.W_w * 2 + Config.W_h

        return (x, y)

    def base_mechanic(self):
        r = random.randint(20, 50)
        self.aming(self.offset + r)

    def aming(self, offset):
        player = Hitbox_Manager.get_player(0)
        ppos = player.get_pos()

        target = self.spawn_mob()

        # x , y = x + int(offset/1), y + int(offset/1)
        proj = self.create_proj(target, ppos)
        self.proj_arrey.append(proj)
