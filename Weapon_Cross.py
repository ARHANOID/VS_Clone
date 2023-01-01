from Weapon import Weapon
from Hitbox_Manager import Hitbox_Manager
import random


class Weapon_Cross(Weapon):

    def __init__(self, id, data):
        super().__init__(id, data)

        self.offset = 0
        self.proj_arrey = []
        self.secondary_proj_arrey = []
        self.start_pos = (0, 0)

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
                        target = self.straight_line(pos, 10, 1)
                        proj.set_destination(target)
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

    def base_mechanic(self):
        r = random.randint(20, 50)
        self.aming(self.offset + r)

    def straight_line(self, pos, lenth, direction=-1):
        player = Hitbox_Manager.get_player(0)
        ppos = player.get_pos()
        dx = (ppos[0] - pos[0]) * lenth
        dy = (ppos[1] - pos[1]) * lenth

        x = ppos[0] + dx * direction
        y = ppos[1] + dy * direction

        return (x, y)

    def aming(self, offset):

        player = Hitbox_Manager.get_player(0)
        ppos = player.get_pos()
        pos = Hitbox_Manager.get_nearest_mob(ppos)
        target = self.straight_line(pos, 4)

        ppos = (ppos[0] + int(offset / 1), ppos[1] + int(offset / 1))
        proj = self.create_proj(target, ppos)
        self.proj_arrey.append(proj)
