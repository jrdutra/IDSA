import os
from fnmatch import fnmatch
import os.path
import pytesseract as ocr
from PIL import Image
from CJsonFile import JsonFile


class OcrReader:

    def __init__(self, _root):
        self.root = _root
        self.qt_arq = 0
        self.qt_lida = 0
        self.porcento = 0
        self.current_data = JsonFile("current_data")

    def generate_ocr(self, current_dir):  # d = diretorio imagem #n = nome imagem #c = caminho do arquivo de imagem
        texto = ocr.image_to_string(Image.open(current_dir), lang='por')
        arq = open(current_dir + ".txt", "w")
        arq.write(texto)
        arq.close()

    def get_quantity(self, img_extension):
        self.qt_arq = 0
        for path, subdirs, files in os.walk(self.root):
            for name in files:
                if fnmatch(name, '*.' + img_extension):  # se nome do arquivo do subdir tiver a extensao
                    current_dir = os.path.join(path, name)
                    if os.path.isfile(current_dir + ".txt") == 0:  # se nao existir o .txt com texto, cria
                        self.qt_arq += 1
                        print(img_extension + ' file foud:' + current_dir)
        return self.qt_arq

    def generate_all(self, img_extension):
        self.qt_lida = 0
        if self.qt_arq == 0:
            self.qt_arq = self.get_quantity(img_extension)
        for path, subdirs, files in os.walk(self.root):
            for name in files:
                if fnmatch(name, '*.' + img_extension):  # se nome do arquivo do subdir tiver a extensao
                    current_dir = os.path.join(path, name)
                    if os.path.isfile(current_dir + ".txt") == 0:  # se nao existir o .txt com texto, cria
                        self.qt_lida += 1
                        print("Converting: " + current_dir)
                        self.generate_ocr(current_dir)
                        self.current_data.json_img_txt_details_conversion(self.qt_arq, self.qt_lida, current_dir)
