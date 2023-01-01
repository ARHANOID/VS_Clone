from Weapon import Weapon
from Hitbox_Manager import Hitbox_Manager
import Config
import random


class Weapon_Knife(Weapon):

    def __init__(self, id, data):
        super().__init__(id, data)

        self.offset = 0

    def act(self):
        self.time += 1
        if self.time % int((self.cooldown / self.cooldown_inc)) == 0:
            self.base_mechanic()

    def base_mechanic(self):
        for i in range(self.projectils):
            r = random.randint(20, 50)
            self.aming(self.offset + i * r)

    def aming(self, offset):
        x, y = Config.W_w / 2, Config.W_h / 2
        player = Hitbox_Manager.get_player(0)
        direction = player.get_direction()
        ppos = player.get_pos()
        if direction == 0:
            x, y = player.get_pos()[0], 0
        elif direction == 1:
            x, y = Config.W_w, player.get_pos()[1]
        elif direction == 2:
            x, y = player.get_pos()[0], Config.W_h
        elif direction == 3:
            x, y = 0, player.get_pos()[1]
        elif direction == 4:  # need to calculate
            x, y = Config.W_w, 0
        elif direction == 5:
            x, y = Config.W_w, Config.W_h
        elif direction == 6:
            x, y = 0, Config.W_h
        elif direction == 7:
            x, y = 0, 0

        x, y = x + int(offset / 1), y + int(offset / 1)
        ppos = (ppos[0] + int(offset / 1), ppos[1] + int(offset / 1))
        proj = self.create_proj((x, y), ppos)
