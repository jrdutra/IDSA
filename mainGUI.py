from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.config import Config
from kivy.properties import StringProperty, NumericProperty
from CJsonFile import JsonFile
import os
from kivy.clock import Clock

Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '520')


class MainGUI(BoxLayout):

    txt_root_current_dir = StringProperty('')
    txt_root_dir = ''
    img_ext = StringProperty('')
    percent = NumericProperty()
    current_number = NumericProperty()
    rage_numer = NumericProperty()
    current_process_dir = StringProperty()
    info_text = StringProperty()

    root_file = JsonFile("root_reg")
    data = root_file.json_details_read()
    txt_root_dir = str(data['root'])

    info_file = JsonFile("current_data")

    def select_to(self, *args):
        try:
            self.txt_root_dir = str(args[1][0])
            self.root_file.root_persist(self.txt_root_dir)
            self.txt_root_current_dir = str(args[1][0])
        except:
            print("Erro")

    def click_run_button(self):
        root_file = JsonFile("root_reg")
        data = root_file.json_details_read()
        Clock.schedule_interval(self.gui_refresh, 0.1)
        try:
            command = 'start python mainProcess.py ' + data['root'] + ' ' + self.img_ext
            os.system(command)
        except:
            print("Something wrong.")

    def gui_refresh(self, dt):
        self.info_data = self.info_file.json_details_read()
        self.percent = self.info_data['%']
        self.current_number = self.info_data['current']
        self.rage_numer = self.info_data['range']
        self.current_process_dir = str(self.info_data['dir'])
        self.info_text = "File " + str(self.current_number) + " from " + str(self.rage_numer) + " files."


class Application(App):

    def build(self):
        self.title = "Image Digital Scanner and Analyzer"
        return MainGUI()

Application().run()
