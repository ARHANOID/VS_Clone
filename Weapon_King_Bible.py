from Weapon import Weapon
from Hitbox_Manager import Hitbox_Manager
from Config import Config
import random, math

class Weapon_King_Bible(Weapon):

    def __init__(self, data):
        super().__init__(data)

        self.offset = -30
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
            if Hitbox_Manager.do_proj_exist(proj):
                pass
            else:
                self.proj_arrey.remove(proj)

        for i in range(len(self.proj_arrey)):
            proj = self.proj_arrey[i]
            player = Hitbox_Manager.get_player(0)
            ppos = player.get_pos()
            pos = self.circulator(ppos, i+1)
            proj.set_pos(pos)


    def circulator(self, pos, i):
        # print("elf.duration * self.duration_inc",self.duration * self.duration_inc)
        # print("self.cooldown / self.cooldown_inc", int(self.cooldown / self.cooldown_inc))
        # print(" self.projectils + self.projectils_inc",  self.projectils + self.projectils_inc)
        # print("i", i)
        # print("half1",
        #       (self.duration * self.duration_inc) / (self.cooldown / self.cooldown_inc) * (
        #         self.projectils + self.projectils_inc))
        # print("half2",
        #       (i / (self.duration * self.duration_inc) / (int(self.cooldown / self.cooldown_inc) * (
        #               self.projectils + self.projectils_inc))
        max_proj_angle = 360 * (i / (((self.duration * self.duration_inc) / int(self.cooldown / self.cooldown_inc)) * (
                self.projectils + self.projectils_inc)))
        # print("max_proj_angle", max_proj_angle)
        angle = (((360 + self.time * self.speed * self.speed_inc)
                 - max_proj_angle)
                 % 360)
        originX, originY = pos[0] - self.offset, pos[1] - self.offset
        angle = angle*(math.pi/180)
        radius = Config.W_h / 9
        x = originX + math.cos(angle) * radius
        y = originY + math.sin(angle) * radius
        result = []
        result.append(x)
        result.append(y)
        return result

    def base_mechanic(self):
        r = random.randint(20, 50)
        self.aming(self.offset + r)

    def aming(self, offset):
        player = Hitbox_Manager.get_player(0)
        ppos = player.get_pos()
        target = (-100000, -100000)
        proj = self.create_proj(target, ppos)
        self.proj_arrey.append(proj)






















