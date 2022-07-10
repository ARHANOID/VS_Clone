import math
from Entity import Entity
from Hitbox_Manager import Hitbox_Manager

class Projectile(Entity):
    def __init__(self, dest, hp, speed, id, pos, size, pierce, duration, img=None):
        super().__init__(id, pos, size, img)

        self.speed = speed
        self.hp = hp
        self.dmg = hp
        self.destination = dest
        self.pierce = pierce
        self.duration = duration
        Hitbox_Manager.add_proj(self)

    def set_destination(self, d):
        self.destination = d
    def set_speed(self, s):
        self.speed = s
    def get_speed(self):
        return self.speed
    def collide(self, mob):
        result = mob.take_dmg(self.dmg)
        self.pierce += -1
        if self.pierce < 0:
            self.death()
        return result

    def death(self):
        Hitbox_Manager.remove_proj(self.id)

    def act(self):
        if self.time > self.duration:
            return self.explosion()

        checker = 0
        dx = self.pos[0] - self.destination[0]
        dy = self.pos[1] - self.destination[1]
        ddx, ddy = 0, 0

        if abs(dx) > abs(dy):
            if dx != 0:
                ddy = abs(dy / dx)
                ddx = (1 - ddy)
            else:
                ddy = 1
                ddx = (1 - ddy)
        else:
            if dy != 0:
                ddx = abs(dx / dy)
                ddy = (1 - ddx)
            else:
                ddx = 1
                ddy = (1 - ddx)

        if abs(dx) > self.speed:
            ddx = self.speed * ddx * math.copysign(1, dx)
            self.pos[0] = self.pos[0] - ddx
        else:
            checker += 1
            self.pos[0] = self.destination[0]

        if abs(dy) > self.speed:
            ddy = self.speed * ddy * math.copysign(1, dy)
            self.pos[1] = self.pos[1] - ddy
        else:
            checker += 1
            self.pos[1] = self.destination[1]

        if checker == 2:
            return self.explosion()

        # self.rect.move_ip(-ddx, -ddy)
        self.rect.update(self.get_center(), self.size)
        # self.rect.center = self.pos
        self.move()

        return None

    def explosion(self):
        self.death()
        pass