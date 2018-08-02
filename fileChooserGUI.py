from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config

Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '300')


class FileChooserGUI(BoxLayout):
    def select_to(self, *args):
        try:
            print(str(args[1][0]))
        except:
            print("Erro")

class FileChooser(App):
    def build(self):
        self.title = "Select Dir"
        return FileChooserGUI()

FileChooser().run()