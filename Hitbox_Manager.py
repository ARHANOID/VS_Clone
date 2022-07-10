from Config import Config
import random
import pygame


s_projectiles_rect = []
s_mob_rect = []
s_player_rect = []

s_projectiles_id = []
s_mob_id = []
s_player_id = []

s_proj_memory = []
s_mob_memory = []

s_id_data = [4]


class Hitbox_Manager():



    @staticmethod
    def add_id():
        s_id_data[0] += 1
        return s_id_data[0]

    @staticmethod
    def add_proj(proj):
        s_projectiles_id.append(proj)
        s_projectiles_rect.append(proj.get_rect())

    @staticmethod
    def add_mob(mob):
        s_mob_id.append(mob)
        s_mob_rect.append(mob.get_rect())

    @staticmethod
    def add_player(player):
        s_player_id.append(player)
        s_player_rect.append(player.get_rect())

    @staticmethod
    def remove_proj(id):
        s_proj_memory.append(id)

    @staticmethod
    def remove_proj_finaly(id):
        for i in range(len(s_projectiles_id)):
            if s_projectiles_id[i].get_id() == id:
                s_projectiles_id.pop(i)
                s_projectiles_rect.pop(i)
                return

    @staticmethod
    def remove_mob(id):
        s_mob_memory.append(id)

    @staticmethod
    def remove_mob_finaly(id):
        for i in range(len(s_mob_id)):
            if s_mob_id[i].get_id() == id:
                s_mob_id.pop(i)
                s_mob_rect.pop(i)
                return

    @staticmethod
    def remove_player(rect):
        for i in range(len(s_player_rect)):
            if s_player_rect[i] == rect:
                s_player_id.pop(i)
                s_player_rect.pop(i)
                return

    @staticmethod
    def get_nearest_mob(x_y):
        x, y = x_y
        x2, y2 = 0,0
        minl = 9999999
        for elem in s_mob_id:
            x1, y1 = elem.get_pos()
            l = Hitbox_Manager.lenght(x, y, x1, y1)
            if minl > l:
                minl = l
                x2, y2 = x1, y1
        return (x2, y2)

    @staticmethod
    def lenght(x1, y1, x2, y2):
        r1 = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        return r1


    @staticmethod
    def get_player(id):
        return s_player_id[id]

    @staticmethod
    def take_xp_player(xp):
        for elem in s_player_id:
            elem.take_xp(xp)

    @staticmethod
    def do_proj_exist(proj):
        if proj in s_projectiles_id:
            return True

        return False


    @staticmethod
    def action_proj():
        Hitbox_Manager.mem_clean()
        list_of_mobs = list(s_mob_rect)
        # result = False
        for proj in s_projectiles_id:
            proj.act()
            index = proj.get_rect().collidelist(list_of_mobs)
            if index > -1:
                proj.collide(s_mob_id[index])


                # print(" if index > -1:", index, elem.get_id(), len(s_mob_id))
                # if proj.collide(s_mob_id[index]):
                    # result = True
        # return result


    @staticmethod
    def mem_clean():
        for elem in s_proj_memory:
            Hitbox_Manager.remove_proj_finaly(elem)
        s_proj_memory.clear()

        for elem in s_mob_memory:
            Hitbox_Manager.remove_mob_finaly(elem)
        s_mob_memory.clear()

    @staticmethod
    def action_mob():
        for elem in s_mob_id:
            elem.act()

    @staticmethod
    def action_player():
        list_of_mobs = list(s_mob_rect)
        for elem in s_player_id:
            elem.act()
            index = elem.get_rect().collidelist(list_of_mobs)
            if index > -1:
                # print(" if index > -1:", index, elem.get_id(), s_mob_id[index].get_id())
                elem.collide(s_mob_id[index])

