from Weapon import Weapon
from Hitbox_Manager import Hitbox_Manager
from Config import Config

class Weapon_Whip(Weapon):

    def __init__(self, data):
        super().__init__(data)

    def base_mechanic(self):
        self.aming()

    def aming(self):
        x,y = Config.W_w/2, Config.W_h/2
        player = Hitbox_Manager.get_player(0)
        ppos = player.get_pos()
        direction = player.get_direction()
        px, py = player.get_pos()
        if direction == 0:
            x, y =px, py - self.AOE
        elif direction == 1:
            x, y = px + self.AOE, py
        elif direction == 2:
            x, y = px, py + self.AOE
        elif direction == 3:
            x, y = px - self.AOE, py
        elif direction == 4: #need to calculate
            x, y = px + int(self.AOE * 0.6), py - int(self.AOE * 0.6)
        elif direction == 5:
            x, y = px + int(self.AOE * 0.6), py + int(self.AOE * 0.6)
        elif direction == 6:
            x, y = px - int(self.AOE * 0.6), py + int(self.AOE * 0.6)
        elif direction == 7:
            x, y = px - int(self.AOE * 0.6), py - int(self.AOE * 0.6)

        proj = self.create_proj((x, y), ppos)






















