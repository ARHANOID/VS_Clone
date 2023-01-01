from Weapon import Weapon
from Hitbox_Manager import Hitbox_Manager
import Config
import random


class Weapon_Axe(Weapon):

    def __init__(self, id, data):
        super().__init__(id, data)

        self.offset = 0
        self.proj_arrey = []
        self.secondary_proj_arrey = []

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

        if self.time % 10 == 0:
            for proj in self.proj_arrey:
                if Hitbox_Manager.do_proj_exist(proj):
                    speed = proj.get_speed() - 1
                    proj.set_speed(speed)
                    if speed < 1:
                        pos = proj.get_pos()
                        proj.set_speed(self.speed)
                        proj.set_destination((pos[0], Config.W_h))
                        self.secondary_proj_arrey.append(proj)
                        self.proj_arrey.remove(proj)
                else:
                    self.proj_arrey.remove(proj)

            for proj in self.secondary_proj_arrey:
                if Hitbox_Manager.do_proj_exist(proj):
                    speed = proj.get_speed() + 1
                    proj.set_speed(speed)
                    if speed < self.speed - 1:
                        self.secondary_proj_arrey.remove(proj)
                else:
                    self.secondary_proj_arrey.remove(proj)

    def base_mechanic(self):
        r = random.randint(20, 50)
        self.aming(self.offset + r)

    def aming(self, offset):
        player = Hitbox_Manager.get_player(0)
        ppos = player.get_pos()

        r = random.randint(-500, 500)
        x, y = ppos[0] + r, ppos[1] - 300

        x, y = x + int(offset / 1), y + int(offset / 1)
        proj = self.create_proj((x, y), ppos)
        self.proj_arrey.append(proj)
