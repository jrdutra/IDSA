from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
from kivy.properties import StringProperty

Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '520')


class MainGUI(Screen):
    def select_to(self, *args):
        try:
            print(str(args[1][0]))
            self.str_root = str(args[1][0])
        except:
            print("Erro")

class Application(App):
    def build(self):
        self.title = "Image Digital Scanner and Analyzer"
        return MainGUI()

Application().run()
