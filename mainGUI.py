from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config

Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '150')

class MainGUI(BoxLayout):
    pass


class Application(App):
    def build(self):
        self.title = "Image Digital Scanner and Analyzer"
        return MainGUI()

Application().run()