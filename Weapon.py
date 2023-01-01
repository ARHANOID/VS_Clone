from Hitbox_Manager import Hitbox_Manager
from Projectile import Projectile
from Paiter import Painter
import pygame


class Weapon(object):
    def __init__(self, id, data):
        self.id = id
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
        self.temp = data[15]
        self.sound = data[16]
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

        image = pygame.image.load(data[14])
        size = image.get_size()
        self.icon = pygame.transform.scale(image, (int(size[0] / 2), int(size[1] / 2)))
        if type(self.temp) is float:
            self.temp = None
        else:
            self.temp = pygame.image.load(self.temp)

        self.upgrades = {"proj": self.upgrade_proj,
                         "dmg": self.upgrade_dmg,
                         "pierce": self.upgrade_pierce,
                         "speed": self.upgrade_speed,
                         "duration": self.upgrade_duration}

    def start(self):
        offset = (70 * self.id, 0)
        Painter.image(self.icon, offset)
        Painter.draw_text(str(self.lvl), 70 * self.id + 50, 20, 20)
        self.act()

    def act(self):
        self.time += 1
        if self.burst < self.projectils:
            if self.time % int(
                    (self.cooldown / self.cooldown_inc) / ((self.projectils + self.projectils_inc) * 3)) == 0:
                self.burst += 1
                self.base_mechanic()
        else:
            if self.time % int(self.cooldown / self.cooldown_inc) == 0:
                self.burst = 0

    def create_proj(self, target, ppos):
        proj = Projectile(target, self.base_damage * self.dmg_inc, self.speed * self.speed_inc, Hitbox_Manager.add_id(),
                          ppos, (self.size * self.AOE_inc, self.size * self.AOE_inc),
                          self.pierce + self.projectils_inc, self.duration * self.duration_inc, self.img, self.sound,
                          self.temp)
        return proj

    def lvlup(self):
        self.lvl += 1
        if self.lvl > self.max_level:
            print("Weapon lvlup self.lvl > self.max_level")
            return
        upgrade_name = self.data[13 + self.lvl * 2]
        if upgrade_name in self.upgrades:
            self.upgrades[upgrade_name](self.data[14 + self.lvl * 2])
        else:
            print("Weapon lvlup Error!!!!!!!!!!!!!!", self.lvl, upgrade_name)
            print(self.data)

    def upgrade_proj(self, n):
        self.projectils += n

    def upgrade_dmg(self, n):
        self.base_damage += n

    def upgrade_pierce(self, n):
        self.pierce += n

    def upgrade_speed(self, n):
        self.speed += n

    def upgrade_duration(self, n):
        self.duration += n

    def base_mechanic(self):
        pass
