from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.config import Config
from kivy.properties import StringProperty
from CJsonFile import JsonFile

Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '520')


class MainGUI(BoxLayout):
    root_file = JsonFile("root_reg")
    txt_root_dir = StringProperty('')
    txt_root_current_dir = StringProperty('')
    data = root_file.json_details_read()
    txt_root_dir = str(data['root'])
    def select_to(self, *args):
        try:
            self.txt_root_dir = str(args[1][0])
            self.root_file.root_persist(self.txt_root_dir)
            self.txt_root_current_dir = str(args[1][0])
        except:
            print("Erro")

class Application(App):

    def build(self):
        self.title = "Image Digital Scanner and Analyzer"
        return MainGUI()

Application().run()
