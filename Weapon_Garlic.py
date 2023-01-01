from Weapon import Weapon
from Hitbox_Manager import Hitbox_Manager
import random


class Weapon_Garlic(Weapon):

    def __init__(self, id, data):
        super().__init__(id, data)

        self.offset = 0
        self.proj_arrey = []

    def act(self):
        self.time += 1
        if len(self.proj_arrey) == 0:
            self.base_mechanic()
            return

        for proj in self.proj_arrey:
            if Hitbox_Manager.do_proj_exist(proj):
                player = Hitbox_Manager.get_player(0)
                ppos = player.get_pos()
                proj.set_pos(ppos)
            else:
                self.proj_arrey.remove(proj)

    def reboot(self):
        for proj in self.proj_arrey:
            proj.deth()
        self.proj_arrey = []

    def base_mechanic(self):
        r = random.randint(20, 50)
        self.aming(self.offset + r)

    def aming(self, offset):
        player = Hitbox_Manager.get_player(0)
        ppos = player.get_pos()
        target = (-100000, -100000)
        proj = self.create_proj(target, ppos)
        self.proj_arrey.append(proj)
