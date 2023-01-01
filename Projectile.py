import pygame
from Entity import Entity
from Hitbox_Manager import Hitbox_Manager
from Temp_effect import Temp_effect


class Projectile(Entity):
    def __init__(self, dest, hp, speed, id, pos, size, pierce, duration, img, sound, temp):
        super().__init__(id, pos, size, speed, img)

        self.hp = hp
        self.dmg = hp
        self.destination = dest
        self.pierce = pierce
        self.duration = duration
        self.sound = pygame.mixer.Sound(sound)
        self.temp = temp
        Hitbox_Manager.add_proj(self)

    def set_destination(self, d):
        self.destination = d

    def set_speed(self, s):
        self.speed = s

    def get_speed(self):
        return self.speed

    def collide(self, mob):
        self.sound.play()
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

        self.seek_target(self.destination)
        if self.time % 4 == 0:
            if self.temp is None:
                return None
            if self.rotation:
                self.rotation = not self.rotation
                self.temp = pygame.transform.flip(self.temp, True, False)
            Temp_effect(20, self.id, self.pos, self.size, 0, self.temp)

    def explosion(self):
        self.death()
        pass
