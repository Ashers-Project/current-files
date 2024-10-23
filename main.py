import threading
from kivy.lang import Builder
from kivymd.app import MDApp
# To set the reference size to your display
# Used in the .kv file
from kivy.metrics import dp
from kivymd.icon_definitions import md_icons
from kivymd.uix.button import MDTextButton
# To set up for multiple windows
from kivymd.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.screenmanager import MDScreenManager
# To change the screen size
from kivy.core.window import Window
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.menu import MDDropdownMenu
from kivy.utils import platform
from kivy.uix.label import Label
from kivy.core.text import Label as CoreLabel
from threading import Thread , ThreadError
from kivymd.uix.snackbar import MDSnackbar
from kivymd.uix.label import MDLabel
from kivy.clock import mainthread
import requests
#ghghgh
print(platform)

# url for light server
light_url = "http://74.105.96.160:2222"
# url for sensor server
sensor_url = "http://74.105.96.160:3333"

#from kivymd.uix.behaviors import LongPressBehavior

class MainWindow(Screen):
    pass
class WIfiWindow(Screen):
    pass
class ChandelierWindow(Screen):
    pass
class LibraryWindow(Screen):
    pass
class SconeWindow(Screen):
    pass
class MapWindow(Screen):
    pass
class Welcome(Screen):
    pass
class WindowManager(ScreenManager):
    pass
class Zyon(MDApp):

    def on_start(self):
        self.iphonemapscreen = "Map View"
        self.mainscreen = "Main Window"
        self.start_server_thread()

        try:
            open(self.user_data_dir +"settings.txt", "r")
        except:
            open(self.user_data_dir +"settings.txt", "w").write("True")

        setting = open(self.user_data_dir +"settings.txt", "r")
        statement = str(setting.readline())
        print(setting.readline())
        setting.close()
        if statement == "True":
            print("first time")
            self.root.current = "welcome_page"
            setting = open(self.user_data_dir +"settings.txt", "w")
            setting.write("False")
            setting.close()
        else:
            self.root.current = "Map View"
    def start_server_thread(self):
        threading.Thread(target= self.light_server).start()
        threading.Thread(target=self.sensor_server).start()
    def light_server(self):
        print("Starting Server For Lights")
        while True:
            try:
                lights_data = requests.get(light_url)
                l_data = lights_data
                self.set_light(l_data)

            except:
                print("g")
                self.send_error(code = "1404")
    def sensor_server(self):
        print("Starting Server For Sensors")
        while True:
            try:

                sensor_data = requests.get(sensor_url)
                s_data = sensor_data
                self.set_sensor(s_data)
                print("worked")
            except:
                print("y")
                self.send_error(code = "1408")
    def build(self):
        Window.size = (393,852) # regular
        #Window.size = (430, 932) # pro max
        return Builder.load_file("main.kv")
    @mainthread
    def send_error(self, code):
        MDSnackbar(
            MDLabel(text="Please Contact Support With Error Code: " + str(code))
        ).open()
        print(str(code))
    @mainthread
    def set_sensor(self, p_data):
        try:

            fpw = str(p_data.text).split("\n")[0]
            brw = str(p_data.text).split("\n")[1]
            gw = str(p_data.text).split("\n")[2]
            bw = str(p_data.text).split("\n")[3]
            sw = str(p_data.text).split("\n")[4]
            kw = str(p_data.text).split("\n")[5]
            lw = str(p_data.text).split("\n")[6]
            gd = str(p_data.text).split("\n")[7]
            sd = str(p_data.text).split("\n")[8]
            ld = str(p_data.text).split("\n")[9]
            boned = str(p_data.text).split("\n")[10]
            btwod = str(p_data.text).split("\n")[11]
            kd = str(p_data.text).split("\n")[13]
            guestw = str(p_data.text).split("\n")[14]

            print()

            try:
                if "fpw" in fpw:
                    if "0" in fpw:
                        self.root.get_screen(self.iphonemapscreen).ids.main_floor_marking.fpw = (0, 1, 0, 1)
                    else:
                        self.root.get_screen(self.iphonemapscreen).ids.main_floor_marking.fpw = (1, 0, 0, 1)

                if "brw" in brw:
                    if "0" in brw:
                        self.root.get_screen(self.iphonemapscreen).ids.main_floor_marking.brw = (0, 1, 0, 1)
                    else:
                        self.root.get_screen(self.iphonemapscreen).ids.main_floor_marking.brw = (1, 0, 0, 1)

                if "gw" in gw:
                    if "0" in gw:
                        self.root.get_screen(self.iphonemapscreen).ids.main_floor_marking.gw = (0, 1, 0, 1)
                    else:
                        self.root.get_screen(self.iphonemapscreen).ids.main_floor_marking.gw = (1, 0, 0, 1)

                if "bw" in bw:
                    if "0" in bw:
                        self.root.get_screen(self.iphonemapscreen).ids.main_floor_marking.bw = (0, 1, 0, 1)
                    else:
                        self.root.get_screen(self.iphonemapscreen).ids.main_floor_marking.bw = (1, 0, 0, 1)

                if "sw" in sw:
                    if "0" in sw:
                        self.root.get_screen(self.iphonemapscreen).ids.main_floor_marking.sw = (0, 1, 0, 1)
                    else:
                        self.root.get_screen(self.iphonemapscreen).ids.main_floor_marking.sw = (1, 0, 0, 1)

                if "kw" in kw:
                    if "0" in kw:
                        self.root.get_screen(self.iphonemapscreen).ids.main_floor_marking.kw = (0, 1, 0, 1)
                    else:
                        self.root.get_screen(self.iphonemapscreen).ids.main_floor_marking.kw = (1, 0, 0, 1)

                if "lw" in lw:
                    if "0" in lw:
                        self.root.get_screen(self.iphonemapscreen).ids.main_floor_marking.lw = (0, 1, 0, 1)
                    else:
                        self.root.get_screen(self.iphonemapscreen).ids.main_floor_marking.lw = (1, 0, 0, 1)

                if "gd" in gd:
                    if "0" in gd:
                         self.root.get_screen(self.iphonemapscreen).ids.main_floor_marking.gd = (0, 1, 0, 1)
                    else:
                        self.root.get_screen(self.iphonemapscreen).ids.main_floor_marking.gd = (1, 0, 0, 1)

                if "sd" in sd:
                    if "0" in sd:
                        self.root.get_screen(self.iphonemapscreen).ids.main_floor_marking.sd = (0, 1, 0, 1)
                    else:
                        self.root.get_screen(self.iphonemapscreen).ids.main_floor_marking.sd = (1, 0, 0, 1)

                if "ld" in ld:
                    if "0" in ld:
                        self.root.get_screen(self.iphonemapscreen).ids.main_floor_marking.ld = (0, 1, 0, 1)
                    else:
                        self.root.get_screen(self.iphonemapscreen).ids.main_floor_marking.ld = (1, 0, 0, 1)

                if "boned" in boned:
                    if "0" in boned:
                        self.root.get_screen(self.iphonemapscreen).ids.main_floor_marking.boned = (0, 1, 0, 1)
                    else:
                        self.root.get_screen(self.iphonemapscreen).ids.main_floor_marking.boned = (1, 0, 0, 1)

                if "btwod" in btwod:
                    if "0" in btwod:
                        self.root.get_screen(self.iphonemapscreen).ids.main_floor_marking.btwod = (0, 1, 0, 1)
                    else:
                        self.root.get_screen(self.iphonemapscreen).ids.main_floor_marking.btwod = (1, 0, 0, 1)

                if "kd" in kd:
                    if "0" in kd:
                        self.root.get_screen(self.iphonemapscreen).ids.main_floor_marking.kd = (0, 1, 0, 1)
                    else:
                        self.root.get_screen(self.iphonemapscreen).ids.main_floor_marking.kd = (1, 0, 0, 1)

                if "guestw" in guestw:
                    if "0" in guestw:
                        self.root.get_screen(self.iphonemapscreen).ids.main_floor_marking.guestw = (0, 1, 0, 1)
                    else:
                        self.root.get_screen(self.iphonemapscreen).ids.main_floor_marking.guestw = (1, 0, 0, 1)

            except:
                pass

        except:
            pass
    @mainthread
    def set_light(self, s_light):
        try:
            drivway_light_sts = str(s_light.text).split("\n")[0]
            outside_sts = str(s_light.text).split("\n")[1]
            front_round_sts = str(s_light.text).split("\n")[2]
            front_flood_sts = str(s_light.text).split("\n")[3]
            game_room_sts = str(s_light.text).split("\n")[4]
            garage_door_carrage_sts = str(s_light.text).split("\n")[5]
            front_scone_sts = str(s_light.text).split("\n")[6]
            chandelier_sts = str(s_light.text).split("\n")[7]
            chandelier_dim_val = str(s_light.text).split("\n")[8]
            scone_sts = str(s_light.text).split("\n")[9]
            scone_dim_val = str(s_light.text).split("\n")[10]
            bookshelf_sts = str(s_light.text).split("\n")[11]
            round_room_sts = str(s_light.text).split("\n")[12]
            round_room_dim_val = str(s_light.text).split("\n")[13]
            baxkyard_sts = str(s_light.text).split("\n")[14]
            print(front_round_sts)

            try:
                #TODO: add main screen buttons
                if "0" in front_round_sts:

                    self.root.get_screen(self.iphonemapscreen).ids.front_round_room_lights.md_bg_color = (0.827, 0.827, 0.827, 0.5)

                else:

                    self.root.get_screen(self.iphonemapscreen).ids.front_round_room_lights.md_bg_color = (1, 0.85, 0.31, 1)


                if  "0" in round_room_sts:
                    self.root.get_screen(self.iphonemapscreen).ids.library_light_button.md_bg_color = (0.827, 0.827, 0.827, 0.5)
                else:
                    self.root.get_screen(self.iphonemapscreen).ids.library_light_button.md_bg_color = (1, 0.85, 0.31, 1)

                if  "0" in baxkyard_sts:
                    self.root.get_screen(self.iphonemapscreen).ids.backyard_flood_button.md_bg_color = (0.827, 0.827, 0.827, 0.5)
                    self.root.get_screen(self.iphonemapscreen).ids.backyard_flood_light_button_2.md_bg_color = (0.827, 0.827, 0.827, 0.5)
                else:
                    self.root.get_screen(self.iphonemapscreen).ids.backyard_flood_button.md_bg_color = (1, 0.85, 0.31, 1)
                    self.root.get_screen(self.iphonemapscreen).ids.backyard_flood_light_button_2.md_bg_color = (1, 0.85, 0.31, 1)

                if  "0" in chandelier_sts:
                    self.root.get_screen(self.iphonemapscreen).ids.chandelier_button.md_bg_color = (0.827, 0.827, 0.827, 0.5)
                    self.root.get_screen(self.mainscreen).ids.chandelier_button.md_bg_color = (16/255, 29/255, 65/255, 1)
                else:
                    self.root.get_screen(self.iphonemapscreen).ids.chandelier_button.md_bg_color = (1, 0.85, 0.31, 1)
                    self.root.get_screen(self.mainscreen).ids.chandelier_button.md_bg_color = (16 / 255, 29 / 255, 65 / 255, 1)
                if "0" in front_scone_sts:
                    self.root.get_screen(self.iphonemapscreen).ids.front_door_button.md_bg_color = (0.827, 0.827, 0.827, 0.5)
                else:
                    self.root.get_screen(self.iphonemapscreen).ids.front_door_button.md_bg_color = (1, 0.85, 0.31, 1)

                if  "0" in front_flood_sts:
                    self.root.get_screen(self.iphonemapscreen).ids.front_flood_button.md_bg_color = (0.827, 0.827, 0.827, 0.5)
                else:
                    self.root.get_screen(self.iphonemapscreen).ids.front_flood_button.md_bg_color = (1, 0.85, 0.31, 1)

                if  "0" in game_room_sts:
                    self.root.get_screen(self.iphonemapscreen).ids.slope_light_button.md_bg_color = (0.827, 0.827, 0.827, 0.5)
                else:
                    self.root.get_screen(self.iphonemapscreen).ids.slope_light_button.md_bg_color = (1, 0.85, 0.31, 1)

                if  "0" in outside_sts:
                    self.root.get_screen(self.iphonemapscreen).ids.outside_kitchen_button.md_bg_color = (0.827, 0.827, 0.827, 0.5)
                else:
                    self.root.get_screen(self.iphonemapscreen).ids.outside_kitchen_button.md_bg_color = (1, 0.85, 0.31, 1)

                if  "0" in scone_sts:
                    self.root.get_screen(self.iphonemapscreen).ids.scone_button_r.md_bg_color = (0.827, 0.827, 0.827, 0.5)
                else:
                    self.root.get_screen(self.iphonemapscreen).ids.scone_button_r.md_bg_color = (1, 0.85, 0.31, 1)

                if  "0" in garage_door_carrage_sts:
                    self.root.get_screen(self.iphonemapscreen).ids.garage_carrage_light_button_1.md_bg_color = (0.827, 0.827, 0.827, 0.5)
                else:
                    self.root.get_screen(self.iphonemapscreen).ids.garage_carrage_light_button_1.md_bg_color = (1, 0.85, 0.31, 1)

            except:
                pass

        except:
            self.send_error(code="1409")
    def open_screen(self, x):
        self.root.current = x
    # TODO: remove test
    def test(self):
        print("worked ya")
    def set_device(self, x):
        try:
            open("modeltype.txt", "r")
        except:
            model = open(self.user_data_dir + "modeltype.zyon", "w")
            model.write(x)
            model.close()
        else:
            model = open(self.user_data_dir + "modeltype.zyon", "w")
            model.write(x)
            model.close()

        self.root.current = "Main Window"
        #getting the position of click
    def handle_click(self, touch_x, touch_y):
        print(f"Clicked at X: {touch_x}, Y: {touch_y}")
        # checking for double tap to open dimmer panel
        # TODO: ADD haptic touch or vibration when pressed
    def check_double_tap(self, card, touch):
        if touch.is_double_tap:
            print("Double-tap detected")
            self.root.current = "Chandelier Window"

    # TODO: ADD haptic touch or vibration when pressed
    # check for double tap then open special page for dimmer panel
    def check_double_tap_scone(self, card, touch):
        if touch.is_double_tap:
            print("Double-tap detected")
            self.root.current = "Scone Window"
    # TODO: ADD haptic touch or vibration when pressed
    # check for double tap then open special page for dimmer panel
    def check_double_tap_library(self, card, touch):
        if touch.is_double_tap:
            print("Double-tap detected")
            self.root.current = "Library Window"
    # initalisation of menu items
    def show_menu(self):
        menu_items = [
            {
                "text": "Home",
                "on_release": lambda x="Main Window": self.open_screen(x),
            },
            {
                "text": "Floor View",
                "on_release": lambda x="Map View": self.open_screen(x),
            }
        ]
        MDDropdownMenu(caller = self.root.get_screen("Main Window").ids.menu_caller, items = menu_items).open()
Zyon().run()
#TODO: create send commands

# TODO: button cammands