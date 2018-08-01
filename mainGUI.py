from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config

Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '500')

class MainGUI(BoxLayout):
    pass


class Application(App):
    def build(self):
        return MainGUI()

Application().run()