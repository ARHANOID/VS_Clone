from Weapon import Weapon
from Hitbox_Manager import Hitbox_Manager
import random

class Weapon_Magic_Wand(Weapon):

    def __init__(self, data):
        super().__init__(data)

        self.offset = 0

    def base_mechanic(self):
        r = random.randint(20, 50)
        self.aming(self.offset +  r)

    def aming(self, offset):
        player = Hitbox_Manager.get_player(0)
        ppos = player.get_pos()
        pos = Hitbox_Manager.get_nearest_mob(ppos)

        dx = (ppos[0] - pos[0]) * 5
        dy = (ppos[1] - pos[1]) * 5

        x = ppos[0] - dx
        y = ppos[1] - dy

        # ppos = (ppos[0] + int(offset/1), ppos[1] + int(offset/1))
        x, y = x + int(offset / 1), y + int(offset / 1)
        ppos = (ppos[0] + int(offset / 1), ppos[1] + int(offset / 1))

        proj = self.create_proj((x,y), ppos)






















