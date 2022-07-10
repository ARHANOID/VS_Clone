import pygame
from Entity import Entity
from Hitbox_Manager import Hitbox_Manager
from Paiter import Painter
from Config import Config
from Weapon_Knife import Weapon_Knife
from Weapon_Whip import Weapon_Whip
from Weapon_Magic_Wand import Weapon_Magic_Wand
from Weapon_Axe import Weapon_Axe
from Weapon_Runetracer import Weapon_Runetracer
from Weapon_King_Bible import Weapon_King_Bible
from Weapon_Garlic import Weapon_Garlic
from Weapon_Cross import Weapon_Cross
from Weapon_Cross import Weapon_Cross
from Weapon_Cross import Weapon_Cross

s_Weapons = {"Whip": Weapon_Whip,
             "Knife": Weapon_Knife,
             "Magic Wand": Weapon_Magic_Wand,
             "Axe": Weapon_Axe,
             "Cross": Weapon_Cross,
             "Runetracer": Weapon_Runetracer,
             "King Bible": Weapon_King_Bible,
             "Garlic": Weapon_Garlic,
             "Fire Wand": None,
             "Santa Water": None}

# s_direct = ((1,0,4),(0,1,4),(1,2,5),(2,1,5),(2,3,6),(3,2,6),(3,4,7),(4,3,7))
s_direct = ((0,1,4),(1,2,5),(2,3,6),(3,0,7))

xp_boost = 2

class Player(Entity):
    def __init__(self, id, pos, size, lvl, img = None):
        super().__init__(id, pos, size, img)
        self.upgrade_counter = 0
        self.speed = 5
        self.hp = 100
        self.xp = 0
        self.new_direction = 0
        self.weapons = {}
        self.actual_direction = 0
        self.lvlup_ready = lvl

        self.lvl = 0
        # if lvl > 0:
        #     for i in range(lvl):
        #         self.lvlup()

        self.xp_for_next_lvl = (self.xp + self.lvl * 100 + 100)/xp_boost

        Hitbox_Manager.add_player(self)

    def get_lvlup_ready(self):
        return self.lvlup_ready
    def collide(self, mob):
        self.take_dmg(mob.get_dmg())

    def take_dmg(self, dmg):
        self.hp += -dmg

    def take_xp(self, xp):
        self.xp += xp
        if self.xp >= self.xp_for_next_lvl:
            self.lvlup_ready += 1
            # self.lvlup()

    def lvlup(self,w):
        self.add_weapon(w)
        self.xp_for_next_lvl = self.xp + self.lvl * 100 + 50
        self.lvl += 1
        self.lvlup_ready += -1
        # pygame.event.post("lvlup")
        print("lvlup", self.lvl)

    def add_weapon(self,w):
        print("add_weapon")
        print(w)
        weapon_class = s_Weapons[w[0]]
        if weapon_class == None:
            print("Player add_weapon weapon_class == None")
            return
        # weapon = weapon_class(w)
        if w[0] in self.weapons:
            self.weapons[w[0]].lvlup()
            return

        self.weapons[w[0]] = weapon_class(w)

    def get_direction(self):
        return self.actual_direction
    def get_lvl(self):
        return self.lvl
    def get_hp(self):
        return self.hp

    def direction_change(self, d):
        for elem in s_direct:
            if (elem[0] == self.new_direction and elem[1] == d) or \
                    (elem[1] == self.new_direction and elem[0] == d):

                self.actual_direction = elem[2]
                self.new_direction = d
                return

        self.actual_direction = d
        self.new_direction = d


    def move_left(self):
        # print("move_left")
        self.pos[0] += -self.speed
        self.rect.move_ip(self.speed * -1, self.speed * 0)
        self.direction_change(3)

    def move_right(self):
        # print("move_right")
        self.pos[0] += self.speed
        self.rect.move_ip(self.speed * 1, self.speed * 0)
        self.direction_change(1)

    def move_up(self):
        # print("move_up")
        self.pos[1] += -self.speed
        self.rect.move_ip(self.speed * 0, self.speed * -1)
        self.direction_change(0)

    def move_down(self):
        # print("move_down")
        self.pos[1] += self.speed
        self.rect.move_ip(self.speed * 0, self.speed * 1)
        self.direction_change(2)

    def game_over(self):
        text = "Game Over"
        Painter.draw_text(text, Config.center_width, Config.center_height + 100, 30)
    def act(self):
        Painter.draw_text("lvl: " + str(self.lvl), int(Config.W_w - 200), int(2 * Config.W_h / 80), 30)
        Painter.draw_text("hp: " + str(self.hp), int(Config.W_w - 100), int(2 * Config.W_h / 80), 30)
        if self.hp <= 0:
            self.game_over()
            return

        for key, weapon in self.weapons.items():
            weapon.act()
        self.move()

