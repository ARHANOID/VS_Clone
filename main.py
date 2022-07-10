import pygame, sys, math, random
from pygame.locals import *

# import Projectile
from Projectile import Projectile
from Monster import Monster
from Paiter import Painter
from Player import Player
from Menu import Menu
from Menu_lvlup import Menu_lvlup
from Config import Config
from Hitbox_Manager import Hitbox_Manager
from Exel_export import Exel_export
import time


step = Config.W_h // 6
zero = '0'
cross = 'X'
mass = [zero, cross]

GRAY = (100, 100, 100)
NAVYBLUE = (60, 60, 100)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GREEN_bl = (30, 200, 40)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)

Projectile_speed = 3

def drawscore(x):
    return

"c:\Саша\programming\Pycharming\Heat_World\main.py"
# def no_one_win():
#     fontObj = pygame.font.Font('freesansbold.ttf', WINDOWWIDTH // 20)
#     item = 'No one have won the game'
#     textSurfaceObj = fontObj.render(item, True, RED, BLUE)
#     textRectObj = textSurfaceObj.get_rect()
#     textRectObj.center = (WINDOWWIDTH // 2, WINDOWHEIGHT // 2)
#     DISPLAYSURF.blit(textSurfaceObj, textRectObj)


def spawn_mob():
    offset = 100
    n = Config.W_w*2 + Config.W_h*2
    r = random.randint(0, n)
    if r < Config.W_w:
        x, y = r, 0 - offset
    elif r < (Config.W_w + Config.W_h):
        x, y = Config.W_w + offset, r - Config.W_w
    elif r < (Config.W_h*2 + Config.W_w):
        x, y = r - (Config.W_w + Config.W_h), Config.W_h + offset
    else:
        x, y = 0 - offset, r - (Config.W_w*2 + Config.W_h)

    return (x,y)


def main(level, score):
    Mob_spawn_time_interval = 120
    spawn_intensity = 10

    # proj_id = 0
    mob_id = 0

    Game_time = 0

    amo_in_air = []
    monster_on_board = []

    path_mob = r'exels\\Mobs.xlsx'
    path_weapons = r'exels\\Weapons.xlsx'
    Exel_export.mobs_export(path_mob)
    weapon_data = Exel_export.weapons_export(path_weapons)
    new_weapons = []
    for key, value in weapon_data.items():
        new_weapons.append(key)


    Painter.initialize()
    player_img =Config.s_address["Player_Witch"]
    board_img = pygame.image.load(Config.s_address["Field"])
    # proj_img = pygame.image.load("Images\\Weapons\\Def_proj.png")
    # mob_img = pygame.image.load("Images\\Mobs\\Def_mob.png")
    mob_img = "Images\\Mobs\\Def_mob.png"
    mob_revert_img = pygame.image.load("Images\\Mobs\\Def_mob_revert.png")
    player = Player(0, (Config.center_width, Config.center_height), (50, 50), 1, player_img)
    # weapon_name = "Runetracer"
    # player.add_weapon(weapon_data[weapon_name])
    # new_weapons.remove(weapon_name)

    arrows_actions = (K_LEFT, K_RIGHT, K_UP, K_DOWN)
    wsad_actions = (K_a, K_d, K_w, K_s)
    player_actions = (player.move_left, player.move_right, player.move_up, player.move_down)
    # player_actions = {K_LEFT:player.move_left,
    # K_a:player.move_left,
    # K_RIGHT: player.move_right,
    # K_d: player.move_right,
    # K_UP: player.player.move_up,
    # K_w: player.move_up,
    # K_DOWN: player.move_down,
    # K_s: player.move_down}
    key_presed = [False, False, False, False]

    while True:
        Painter.game_start(board_img)
        tasks = []
        # Painter.draw_text("lvl: " + str(player.get_lvl()), int(Config.W_w - 200), int(2 * Config.W_h / 80), 30)
        # Painter.draw_text("hp: " + str(player.get_hp()), int(Config.W_w - 100), int(2 * Config.W_h / 80), 30)

        mouseClicked = False

        if Game_time % Mob_spawn_time_interval == 0:
            # Mob_spawn_time_interval += 1
            spawn_intensity += 1
            for i in range(int(spawn_intensity/10)):
                # print("Game_time", Game_time)
                # x = random.randint(0, Config.W_w)
                # y = random.randint(0,  Config.W_h)
                # if x > y :
                #     x = 0
                # else:
                #     y = 0
                # proj = Projectile((x,y), 100, 5, proj_id, player.get_pos(), (50, 50), proj_img)
                mob_pos = spawn_mob()
                # print("Main mob_pos ", mob_pos)
                mob = Monster(mob_id, mob_pos,(40, 40), mob_img, mob_revert_img)
                mob_id += 1
                # proj_id += 1


        Hitbox_Manager.action_player()
        Hitbox_Manager.action_proj()
        Hitbox_Manager.action_mob()

        for elem in tasks:
            elem[0](elem[1])

        if player.get_lvlup_ready() > 0:
            weapon_name = Menu_lvlup.Open(new_weapons, weapon_data)
            print("weapon_name", weapon_name)
            if weapon_name is not None:
                player.lvlup(weapon_data[weapon_name])
                # new_weapons.remove(weapon_name)
                for i in range(len(key_presed)):
                    key_presed[i] = False

        for i in range(len(key_presed)):
            if key_presed[i]:
                player_actions[i]()

        for event in pygame.event.get():

            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
            elif event.type == KEYUP and event.key == K_F10:
                weapon_name = Menu_lvlup.Open(new_weapons, weapon_data)
                print("weapon_name", weapon_name)
                if weapon_name is not None:
                    player.lvlup(weapon_data[weapon_name])
                    # new_weapons.remove(weapon_name)

            for i in range(len(key_presed)):
                if event.type == KEYDOWN and (event.key == arrows_actions[i] or event.key == wsad_actions[i]):
                    key_presed[i] = True
                    player_actions[i]()
                if event.type == KEYUP and (event.key == arrows_actions[i] or event.key == wsad_actions[i]):
                    key_presed[i] = False


        if mouseClicked:
            print("mouseClicked", event.pos)

        Game_time += 1
        Painter.update()


if __name__ == '__main__':
    main(1, 0)