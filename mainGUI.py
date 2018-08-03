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
    root_writer = JsonFile("root_reg")
    txt_root_dir = StringProperty('')

    def select_to(self, *args):
        try:
            self.txt_root_dir = str(args[1][0])
            self.root_writer.root_persist(self.txt_root_dir)
        except:
            print("Erro")

class Application(App):
    root_reader = JsonFile("root_reg")
    def build(self):
        root_data = self.root_reader.json_details_read()
        str_root = root_data['root']
        MainGUI().txt_root_dir = str(root_data)
        self.title = "Image Digital Scanner and Analyzer"
        return MainGUI()

Application().run()
