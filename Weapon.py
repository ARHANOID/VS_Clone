from Hitbox_Manager import Hitbox_Manager
from Projectile import Projectile

class Weapon(object):
    def __init__(self,  data):
        self.name = data[0]
        self.size = data[1]
        self.max_level = data[2]
        self.base_damage = data[3]
        self.speed = data[4]
        self.duration = data[5]
        self.cooldown = data[6]
        self.hitbox_delay = data[7]
        self.AOE = data[8]
        self.crit_multi = data[9]
        self.projectils = data[10]
        self.pierce = data[11]
        self.img = data[12]
        self.exp_img = data[13]
        self.data = data

        self.time = 0
        self.burst = 0

        self.dmg_inc = 1
        self.speed_inc = 1
        self.cooldown_inc = 1
        self.AOE_inc = 1
        self.duration_inc = 1
        self.projectils_inc = 0
        self.pierce_inc = 0
        self.lvl = 0

        self.upgrades = {"proj": self.upgrade_proj,
                      "dmg": self.upgrade_dmg,
                     "pierce": self.upgrade_pierce}


    def act(self):
        self.time += 1
        if self.burst < self.projectils:
            if self.time % int((self.cooldown/self.cooldown_inc) / ((self.projectils + self.projectils_inc) * 3)) == 0:
                self.burst += 1
                self.base_mechanic()
        else:
            if self.time % int(self.cooldown / self.cooldown_inc) == 0:
                self.burst = 0

    def create_proj(self, target, ppos):
        proj = Projectile(target, self.base_damage * self.dmg_inc, self.speed * self.speed_inc, Hitbox_Manager.add_id(),
                          ppos, (self.size * self.AOE_inc, self.size * self.AOE_inc),
                          self.pierce + self.projectils_inc, self.duration * self.duration_inc, self.img)
        return proj


    def lvlup(self):
        self.lvl += 1
        if self.lvl > self.max_level:
            print("Weapon lvlup self.lvl > self.max_level")
            return
        upgrade_name = self.data[13 + self.lvl *2]
        if upgrade_name in self.upgrades:
            self.upgrades[upgrade_name](self.data[14 + self.lvl *2])
        else:
            print("Weapon lvlup Error!!!!!!!!!!!!!!", self.lvl, upgrade_name)
            print(self.data)

    def upgrade_proj(self, n):
        self.projectils += n

    def upgrade_dmg(self, n):
        self.base_damage += n

    def upgrade_pierce(self, n):
        self.pierce += n
    def base_mechanic(self):
        pass







