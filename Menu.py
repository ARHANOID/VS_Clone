import pygame, sys, random
from pygame.locals import *
import Config
from Button import Button
from Paiter import Painter
import sqlite3

s_Buttons = []
s_Options = {}
s_Screen_saves = {}

step = Config.W_h // 6
zero = '0'
cross = 'X'
mass = [zero, cross]

START = (0, 0, 0)

GRAY = (100, 100, 100)
NAVYBLUE = (60, 60, 100)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)

Projectile_speed = 3


class Menu(object):
    def __init__(self):
        pass

    @staticmethod
    def lvl_up_open(new_weapons, weapon_data):
        sound = pygame.mixer.Sound("Sound\\UI\\Lvlup.mp3")
        sound.play()
        if len(new_weapons) < 1:
            return None
        name_1 = new_weapons[random.randint(0, len(new_weapons) - 1)]
        name_2 = new_weapons[random.randint(0, len(new_weapons) - 1)]
        name_3 = new_weapons[random.randint(0, len(new_weapons) - 1)]
        weapon_icon_1 = pygame.image.load(weapon_data[name_1][14])
        weapon_icon_2 = pygame.image.load(weapon_data[name_2][14])
        weapon_icon_3 = pygame.image.load(weapon_data[name_3][14])

        Lvlup_Plate_img = pygame.image.load(Config.s_address["Lvlup_Plate"])
        Lvlup_Button_img = pygame.image.load(Config.s_address["Lvlup_Button"])

        button_pos = (Config.screen_w(12), Config.screen_h(3))
        Painter.image(Lvlup_Plate_img, (button_pos[0] - 10, button_pos[1] - 10))
        size = Lvlup_Button_img.get_size()

        s_Buttons.append(
            Button(START, button_pos[0], Config.screen_h(3) + (10 + size[1]) * len(s_Buttons),
                   Lvlup_Button_img, name_1))
        Painter.image(weapon_icon_1, (button_pos[0], Config.screen_h(0) + (10 + size[1]) * len(s_Buttons)))
        s_Buttons.append(
            Button(START, button_pos[0], button_pos[1] + (10 + size[1]) * len(s_Buttons),
                   Lvlup_Button_img, name_2))
        Painter.image(weapon_icon_2, (button_pos[0], Config.screen_h(0) + (10 + size[1]) * len(s_Buttons)))

        s_Buttons.append(
            Button(START, button_pos[0], button_pos[1] + (10 + size[1]) * len(s_Buttons),
                   Lvlup_Button_img, name_3))
        Painter.image(weapon_icon_3, (button_pos[0], Config.screen_h(0) + (10 + size[1]) * len(s_Buttons)))

        return Menu.game_start()

    @staticmethod
    def game_start():
        F10_used = False

        while not F10_used:

            mouseClicked = False
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEMOTION:
                    mousex, mousey = event.pos
                elif event.type == MOUSEBUTTONUP:
                    mousex, mousey = event.pos
                    mouseClicked = True
                elif (event.type == KEYUP and event.key == K_F10):
                    F10_used = True
                    s_Buttons.clear()

            if mouseClicked:
                if s_Buttons[0].is_mouseover():
                    text = s_Buttons[0].text
                    print(text, "is clicked")
                    s_Buttons.clear()
                    return text
                if s_Buttons[1].is_mouseover():
                    text = s_Buttons[1].text
                    print(text, "is clicked")
                    s_Buttons.clear()
                    return text
                    # F10_used = True
                if s_Buttons[2].is_mouseover():
                    text = s_Buttons[2].text
                    print(text, "is clicked")
                    s_Buttons.clear()
                    return text

            Painter.update()

    @staticmethod
    def Starting_screen():
        sound = pygame.mixer.Sound("Sound\\UI\\Lvlup.mp3")
        sound.play()

        Start_Screen_img = pygame.image.load(Config.s_address["Start_Screen"])
        Lvlup_Button_img = pygame.image.load(Config.s_address["SMenu_Button"])

        button_pos = (Config.screen_w(14), Config.screen_h(19))
        Painter.image(Start_Screen_img, (0, 0))
        size = Lvlup_Button_img.get_size()

        s_Buttons.append(
            Button(START, button_pos[0], button_pos[1] + (10 + size[1]) * len(s_Buttons),
                   Lvlup_Button_img, "Start"))
        s_Buttons.append(
            Button(START, button_pos[0], button_pos[1] + (10 + size[1]) * len(s_Buttons),
                   Lvlup_Button_img, "Save"))

        s_Buttons.append(
            Button(START, button_pos[0], button_pos[1] + (10 + size[1]) * len(s_Buttons),
                   Lvlup_Button_img, "Load"))

        return Menu.game_start()

    @staticmethod
    def open_saves():
        Menu.back_ground()

        F10_used = False
        cout = 0

        img1 = pygame.image.load("Images\\Button.png")
        button_retunr = Button(Window, START, Config.screen_w(26), Config.screen_h(15), 100, 50, img1, "Return")
        s_Options.clear()

        for key, value in Menu.Read_db().items():
            load_del = (Button(Window, START, Config.screen_w(8), Config.screen_h(2) + 50 * cout, 75, 26, None, "Load"),
                        Button(Window, START, Config.screen_w(10), Config.screen_h(2) + 50 * cout, 75, 26, None,
                               "Dell"))
            Menu.drawText(value, Config.screen_w(3), Config.screen_h(2) + 50 * cout)
            s_Options[key] = load_del
            cout += 1
        button_new = Button(Window, START, Config.screen_w(5), Config.screen_h(3) + 50 * cout, 75, 26, None, "New Save")

        while not F10_used:
            mouseClicked = False
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEMOTION:
                    mousex, mousey = event.pos
                elif event.type == MOUSEBUTTONUP:
                    mousex, mousey = event.pos
                    mouseClicked = True
                elif (event.type == KEYUP and event.key == K_F10):
                    F10_used = True
                    s_Options.clear()

            if mouseClicked:
                if button_retunr.is_mouseover():
                    F10_used = True
                if button_new.is_mouseover():
                    Menu.save_all()
                    Menu.sql_shenanigans()
                    Menu.open_saves()
                    F10_used = True
                for key, value in s_Options.items():
                    if value[0].is_mouseover():
                        print(key, " is clicked Load")
                        data = Menu.Load_data_from_db(key)
                        Menu.row_to_file(data)
                        Menu.load_all()
                        F10_used = True

                    elif value[1].is_mouseover():
                        print(key, " is clicked Dell")
                        Menu.deleteRecord(key)
                        Menu.open_saves()
                        return True
                        # break

            Menu.update()

    @staticmethod
    def show_options():
        cout = 0
        for key, value in Config.s_data.items():
            text = key + ": " + str(value)
            Menu.drawText(text, 40, 100 + 50 * cout)
            cout += 1

    @staticmethod
    def open_options():
        Menu.back_ground()

        F10_used = False
        cout = 0
        decimal = 1
        img1 = pygame.image.load("Images\\Button.png")
        mult10 = Button(Window, START, 300, 50 + 50 * cout, 50, 30, None, "X10")
        division10 = Button(Window, START, 350, 50 + 50 * cout, 50, 30, None, ":10")
        button_retunr = Button(Window, START, 800, 700, 100, 50, img1, "Return")
        s_Options.clear()
        for key, value in Config.s_data.items():
            text = key + ": " + str(value)
            s_Options[key] = Button(Window, START, 300, 100 + 50 * cout, 75, 26, None, "Change")
            cout += 1
        before_listing_save = Window.copy()
        Menu.show_options()

        while not F10_used:
            mouseClicked = False
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEMOTION:
                    mousex, mousey = event.pos
                elif event.type == MOUSEBUTTONUP:
                    mousex, mousey = event.pos
                    mouseClicked = True
                elif (event.type == KEYUP and event.key == K_F10):
                    F10_used = True
                    s_Options.clear()

            if mouseClicked:
                if mult10.is_mouseover():
                    decimal += 1
                if division10.is_mouseover():
                    decimal += -1
                if button_retunr.is_mouseover():
                    F10_used = True
                    # break
                for key, value in s_Options.items():
                    if value.is_mouseover():
                        Config.s_data[key] += Menu.cout_change(decimal)
                        if Config.s_data[key] < 0:
                            Config.s_data[key] = 1
                        break

                Window.blit(before_listing_save, (0, 0))
                Menu.show_options()
                text = str(Menu.cout_change(decimal))
                Menu.drawText(text, 400, 50)

            Painter.update()

    @staticmethod
    def cout_change(desimal):
        number = 0
        if desimal > 0:
            number = 1
            for i in range(desimal - 1):
                number *= 10
        elif desimal < 0:
            number = -1
            for i in range((-1 * desimal) - 1):
                number *= 10

        return number

    @staticmethod
    def save_screen(name):
        screen = Painter.save_display()
        s_Screen_saves[name] = screen

    @staticmethod
    def load_screen(name):
        screen = s_Screen_saves.get(name)
        Painter.load_display(screen)

    @staticmethod
    def row_to_file(data):
        with open('data.pickle', 'wb') as f:
            f.write(data)

    @staticmethod
    def Read_db():
        results = {}
        database = r"Heat_World.db"
        conn = sqlite3.connect(database)
        cursor = conn.cursor()

        cursor.execute("SELECT id FROM save ORDER BY id")
        ids = cursor.fetchall()

        cursor.execute("SELECT time FROM save ORDER BY id")
        times = cursor.fetchall()
        conn.close()

        for i in range(len(ids)):
            results[ids[i][0]] = times[i][0]
        print(results)

        return results

    @staticmethod
    def Load_data_from_db(id):
        database = r"Heat_World.db"
        conn = sqlite3.connect(database)
        cursor = conn.cursor()

        sql_select_query = """select * from save where id = ?"""
        cursor.execute(sql_select_query, (id,))
        records = cursor.fetchall()
        for row in records:
            print("name = ", row[1])
            print("time  = ", row[2])
            result = row[3]
        cursor.close()

        return result

    @staticmethod
    def deleteRecord(id):
        database = r"Heat_World.db"
        try:
            sqliteConnection = sqlite3.connect(database)
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")

            # Deleting single record now
            sql_delete_query = """DELETE from save where id = """ + str(id)
            cursor.execute(sql_delete_query)
            sqliteConnection.commit()
            print("Record deleted successfully ")
            cursor.close()

        except sqlite3.Error as error:
            print("Failed to delete record from sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("the sqlite connection is closed")
