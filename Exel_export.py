import pandas as pd


class Exel_export():

    @staticmethod
    def mobs_export(path):
        ex_data = pd.read_excel(path)
        # col = pd.DataFrame(ex_data, columns=["name", "size", "speed", "hp", "dmg", "img", "img_revert"])
        col = ("name", "size", "speed", "hp", "dmg", "img", "img_revert")
        df = pd.DataFrame(ex_data, columns=col)
        # print(df)
        full_data = {}
        raw_data = {}
        for i in range(8):
            # print(i)
            raw = df.iloc[i]
            mb_list = list(raw.tail(10))
            for i in range(len(col)):
                raw_data[col[i]] = mb_list[i]
            full_data[mb_list[0]] = mb_list

            # for key, value in raw_data.items():
            #     print(key, value)
        return full_data

    @staticmethod
    def weapons_export(path):
        ex_data = pd.read_excel(path)
        col = ("name", "size", "max_level", "base_damage", "speed", "duration", "cooldown",
               "hitbox_delay", "AOE", "crit_multi", "projectils", "pierce",
               "img", "exp_img", "icon", "temp", "sound",
               "lvl_2 name",
               "lvl_2 value", "lvl_3 name", "lvl_3 value", "lvl_4 name", "lvl_4 value",
               "lvl_5 name", "lvl_5 value", "lvl_6 name", "lvl_6 value")
        df = pd.DataFrame(ex_data, columns=col)
        # print(df)
        full_data = {}
        raw_data = {}
        for i in range(10):
            raw = df.iloc[i]
            mb_list = list(raw.tail(100))
            for i in range(len(col)):
                raw_data[col[i]] = mb_list[i]
            full_data[mb_list[0]] = mb_list

            # for key, value in raw_data.items():
            #     print(key, value)
        return full_data
