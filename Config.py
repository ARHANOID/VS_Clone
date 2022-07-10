class Config():
    W_w = 1920#800#1920#1024
    W_h = 1080#600#1080#840


    center_width = W_w // 2
    center_height = W_h // 2

    Bright_green = (0, 85, 0)
    Bright_blue = (0, 0, 85)
    Bright_smt = (0, 185, 185)
    Bright_smt = (0, 55, 55)
    Shine_smt = (0, 155, 155)
    font_size = int(W_w/50)

    right = ( 1, 0)
    up = (0,  1)
    left = (-1, 0)
    douw = (0, -1)
    Direction = ((right, up, left, douw),(up, left, douw, right),(left, douw, right, up), (douw, right, up, left))

    s_data = {"Player_units_limit": 32,
              "starting_heat": 25,
              "FPS": 60}

    s_address = {"Field": "Images\\UI\\Field.png",
              "Player_Witch": "Images\\Players\\Witch.png",
              "Lvlup_Button": "Images\\UI\\Lvlup_Button.png",
            "Lvlup_Plate": "Images\\UI\\Lvlup_Plate.png",
            "FPS": 60
                 }

    @staticmethod
    def screen_w(x):
        return int(x*Config.W_w/(34))
    @staticmethod
    def screen_h(x):
        return int(x*Config.W_h/(28))


