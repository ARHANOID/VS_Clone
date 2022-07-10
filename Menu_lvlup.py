import pygame, sys, math, random
from pygame.locals import *
from Config import Config
import pickle
from Button import Button
from Cell_Manager import Cell_Manager
from Paiter import Painter
import sqlite3
import time

s_Buttons = []
s_Options =  {}
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

class Menu_lvlup(object):
    def __init__(self):
        pass
    @staticmethod
    def Open(new_weapons, weapon_data):
        if len(new_weapons) < 1:
            return None
        name_1 = new_weapons[random.randint(0, len(new_weapons)-1)]
        # print("Menu_lvlup, Open", new_weapons[random.randint(0, len(new_weapons))], weapon_data[name_1][14])
        name_2 = new_weapons[random.randint(0, len(new_weapons)-1)]
        name_3 = new_weapons[random.randint(0, len(new_weapons)-1)]
        weapon_icon_1 = pygame.image.load(weapon_data[name_1][14])
        weapon_icon_2 = pygame.image.load(weapon_data[name_2][14])
        weapon_icon_3 = pygame.image.load(weapon_data[name_3][14])

        Lvlup_Plate_img = pygame.image.load(Config.s_address["Lvlup_Plate"])
        Lvlup_Button_img = pygame.image.load(Config.s_address["Lvlup_Button"])

        button_pos = (Config.screen_w(12), Config.screen_h(3))
        Painter.image(Lvlup_Plate_img,(button_pos[0]-10,button_pos[1]-10))
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


        return Menu_lvlup.game_start()


    @staticmethod
    def game_start():

        # Menu_lvlup.update()
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
               # if s_Buttons[3].is_mouseover():
               #     print(s_Buttons[3].text, "is clicked")
               #     s_Options.clear()
               #     Menu_lvlup.open_options()
               #     Menu_lvlup.load_screen("Menu_start")
               # if s_Buttons[4].is_mouseover():
               #     print(s_Buttons[4].text, "is clicked")
               #     F10_used = True

            Painter.update()

    @staticmethod
    def open_saves():
        Menu_lvlup.back_ground()

        F10_used = False
        cout = 0

        img1 = pygame.image.load("Images\\Button.png")
        button_retunr = Button(Window, START,  Config.screen_w(26), Config.screen_h(15), 100, 50, img1, "Return")
        s_Options.clear()

        for key, value in Menu_lvlup.Read_db().items():
            load_del = (Button(Window, START,  Config.screen_w(8), Config.screen_h(2) + 50 * cout, 75, 26, None, "Load"),
                        Button(Window, START,  Config.screen_w(10), Config.screen_h(2) + 50 * cout, 75, 26, None, "Dell"))
            Menu_lvlup.drawText(value, Config.screen_w(3), Config.screen_h(2) + 50 * cout)
            s_Options[key] = load_del
            cout += 1
        button_new = Button(Window, START,  Config.screen_w(5), Config.screen_h(3) + 50 * cout, 75, 26, None, "New Save")


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
                    Menu_lvlup.save_all()
                    Menu_lvlup.sql_shenanigans()
                    Menu_lvlup.open_saves()
                    F10_used = True
                for key, value in s_Options.items():
                    if value[0].is_mouseover():
                        print(key, " is clicked Load")
                        data = Menu_lvlup.Load_data_from_db(key)
                        Menu_lvlup.row_to_file(data)
                        Menu_lvlup.load_all()
                        F10_used = True

                    elif value[1].is_mouseover():
                        print(key, " is clicked Dell")
                        Menu_lvlup.deleteRecord(key)
                        Menu_lvlup.open_saves()
                        return True
                        # break




            Menu_lvlup.update()
    @staticmethod
    def show_options():
        cout = 0
        for key, value in Config.s_data.items():
            text = key + ": " + str(value)
            Menu_lvlup.drawText(text, 40, 100 + 50 * cout)
            cout += 1

    @staticmethod
    def open_options():
        Menu_lvlup.back_ground()

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
            s_Options[key]=Button(Window, START, 300, 100+50*cout, 75, 26, None, "Change")
            cout += 1
        before_listing_save = Window.copy()
        Menu_lvlup.show_options()

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
                       Config.s_data[key] += Menu_lvlup.cout_change(decimal)
                       if Config.s_data[key] <0 :
                           Config.s_data[key] = 1
                       break

               Window.blit(before_listing_save, (0, 0))
               Menu_lvlup.show_options()
               text = str(Menu_lvlup.cout_change(decimal))
               Menu_lvlup.drawText(text, 400, 50)


            Painter.update()

    @staticmethod
    def cout_change(desimal):
        number = 0
        if desimal > 0:
            number = 1
            for i in range(desimal-1):
                number *= 10
        elif desimal < 0:
            number = -1
            for i in range((-1*desimal)-1):
                number *= 10

        return number





    @staticmethod
    def open_info():
        len1 = len(Cell_Manager.get_lcell_data())
        if len1>0:
            text01 = str(Cell_Manager.get_lcell_data()[-1].id)
        else:
            text01 = str("0")
        len2 = len(Cell_Manager.get_hcell_data())
        if len2 > 0:
            text02 = str(Cell_Manager.get_hcell_data()[-1].id)
        else:
            text02 = str("0")
        len3 = Cell_Manager.get_acell_count()
        if len3 > 0:
            text03 = str(Cell_Manager.get_hcell_data()[-1].id)
        else:
            text03 = str("0")

        text1 = "Number of life Cells " + str(len1) + "   Last id " + text01
        text2 = "Number of Hunter Cells " + str(len2) + "   Last id " + text02
        text3 = "Number of Ant Cells " + str(len3) + "   Last id " + text03
        Menu_lvlup.drawText(text1, int(Config.W_w/25),  int(2*Config.W_h/8))
        Menu_lvlup.drawText(text2, int(Config.W_w/25),  int(2*Config.W_h/8)+ int(Config.W_h/28))
        Menu_lvlup.drawText(text3, int(Config.W_w / 25), int(2 * Config.W_h / 8) + int(Config.W_h / 28) * 2 )

    @staticmethod
    def drawText(text, x, y, font_size = Config.font_size):
        # print("drawText",text)

        font = pygame.font.SysFont('comicsans', font_size)
        text = font.render(text, True, (255, 255, 255))
        Window.blit(text,(x, y))


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
    def save_all():
        main_screen = s_Screen_saves.get("Main_screen")
        lcells, hcells, acells, anest = Cell_Manager.get_all_data()
        print("hcells ", hcells)

        with open('data.pickle', 'wb') as f:
            pickle.dump(main_screen, f)
            pickle.dump(lcells, f)
            pickle.dump(hcells, f)
            pickle.dump(acells, f)
            pickle.dump(anest, f)

        print("data is saved")

    @staticmethod
    def load_all():
        with open('data.pickle', 'rb') as f:
            main_screen = pickle.load(f)
            s_lcell_temp = pickle.load(f)
            s_hcell_temp = pickle.load(f)
            s_acells_temp = pickle.load(f)
            s_anest_temp = pickle.load(f)

        s_Screen_saves["Main_screen"] = main_screen
        print("s_hcell__temp", s_hcell_temp)
        Cell_Manager.load_all_data(s_lcell_temp, s_hcell_temp, s_acells_temp, s_anest_temp)

    @staticmethod
    def convert_to_binary_data(filename):
        # Преобразование данных в двоичный формат
        with open(filename, 'rb') as file:
            blob_data = file.read()
        return blob_data

    @staticmethod
    def sql_shenanigans():
        b_data = Menu_lvlup.convert_to_binary_data("data.pickle")
        Menu_lvlup.Read_db()
        Menu_lvlup.insert_blob(Menu_lvlup.New_save_id(), "name1", b_data)
        # Menu_lvlup.insert_blob(Menu_lvlup.New_save_id(), "name2", b_data)
        Menu_lvlup.Read_db()

    @staticmethod
    def create_table():
        database = r"Heat_World.db"
        sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS save (
                                                id integer PRIMARY KEY,
                                                name text NOT NULL,
                                                time text,
                                                data BLOB NOT NULL                                     
                                            ); """

        "fast api"
        "seller"
        "posac sql"
        "py instaler"

        conn =  sqlite3.connect(database)

        if conn is not None:
            # create projects table
            cur = conn.cursor()
            cur.execute(sql_create_projects_table)

            # # create tasks table
            # cur = conn.cursor()
            # cur.execute(sql_create_tasks_table)
        else:
            print("Error! cannot create the database connection.")

        conn.close()

    @staticmethod
    def insert_blob(emp_id, name, data):
        database = r"Heat_World.db"
        try:
            sqlite_connection = sqlite3.connect(database)
            cursor = sqlite_connection.cursor()
            print("Подключен к SQLite")

            sqlite_insert_blob_query = """INSERT INTO save
                                      (id, name, time, data) VALUES (?, ?, ?, ?)"""

            time_now = str(time.strftime("%Y.%m.%d.%h.%M.%S"))
            # data = Menu_lvlup.convert_to_binary_data(resume_file)
            # Преобразование данных в формат кортежа
            data_tuple = (emp_id, name, time_now, data)
            cursor.execute(sqlite_insert_blob_query, data_tuple)
            sqlite_connection.commit()
            print("Изображение и файл успешно вставлены как BLOB в таблиу")
            cursor.close()

        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if sqlite_connection:
                sqlite_connection.close()
                print("Соединение с SQLite закрыто")

    @staticmethod
    def New_save_id():
        database = r"Heat_World.db"
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM save ORDER BY id")
        results = cursor.fetchall()
        print(results,
              len(results))  # [('A Aagrh!',), ('A Cor Do Som',), ('Aaron Copland & London Symphony Orchestra',)]
        # cursor.execute("SELECT Name FROM class ORDER BY Name LIMIT 3")
        # results = cursor.fetchall()
        # print(results)  # [('A Aagrh!',), ('A Cor Do Som',), ('Aaron Copland & London Symphony Orchestra',)]
        conn.close()
        if len(results) > 0:
            answer = int(results[-1][0])+1
        else:
            answer = 0
        return answer

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
            # print("binar  = ", row[3])
            result = row[3]
            # print("Salary  = ", row[4])
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
            sql_delete_query = """DELETE from save where id = """+str(id)
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



