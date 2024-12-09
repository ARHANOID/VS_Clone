import pygame
from Entity import Entity
from Hitbox_Manager import Hitbox_Manager
from Temp_effect import Temp_effect


class Projectile(Entity):
    def __init__(self, dest, hp, speed, id, pos, size, pierce, duration, img, sound, temp):
        self.sound_text = sound
        self.temp = temp
        super().__init__(id, pos, size, speed, img)

        self.hp = hp
        self.dmg = hp
        self.destination = dest
        self.pierce = pierce
        self.duration = duration
        self.sound = None
        self.temp_effect = None

        Hitbox_Manager.add_proj(self)

        self.set_img()

    def set_destination(self, d):
        self.destination = d

    def set_speed(self, s):
        self.speed = s

    def get_speed(self):
        return self.speed

    def del_img(self):
        self.img = None
        self.sound = None
        self.temp_effect = None

    def set_img(self):
        if type(self.text_img) is str:
            self.img = pygame.image.load(self.text_img)
        else:
            self.img = self.text_img
        if self.temp is not None:
            self.temp_effect = pygame.image.load(self.temp)
        self.sound = pygame.mixer.Sound(self.sound_text)

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
            if self.temp_effect is None:
                return None
            if self.rotation:
                self.rotation = not self.rotation
                self.temp_effect = pygame.transform.flip(self.temp_effect, True, False)
            Temp_effect(20, self.id, self.pos, self.size, 0, self.temp_effect)

    def explosion(self):
        self.death()
        pass
