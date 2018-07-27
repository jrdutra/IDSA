import os
from fnmatch import fnmatch
import os.path
import pytesseract as ocr
from PIL import Image

pattern = "*.jpg"

# Lê diretorio
arquivo = open('dir.txt', 'r')
root = arquivo.read()
arquivo.close();


def gerar_ocr(d): # d = diretorio imagem #n = nome imagem #c = caminho do arquivo de imagem
    texto = ocr.image_to_string(Image.open(dir), lang='por')
    arq = open(d+".txt", "w")
    arq.write(texto)
    arq.close()


# Pega Quantidade de arquivos sem OCR
qt_arq = 0
for path, subdirs, files in os.walk(root):
    for name in files:
        if fnmatch(name, pattern):  # se nome do arquivo do subdir tiver a extensao
            dir = os.path.join(path, name)
            if os.path.isfile(dir+".txt") == 0:  # se nao existir o .txt com texto, cria
                qt_arq += 1

# ENTRA NO DIRETORIO E PROCURA POR ARQUIVOS JPG
qt_lida = 0
porcento = 0
for path, subdirs, files in os.walk(root):
    for name in files:
        if fnmatch(name, pattern):  # se nome do arquivo do subdir tiver a extensao
            dir = os.path.join(path, name)
            if os.path.isfile(dir+".txt") == 0:  # se nao existir o .txt com texto, cria
                qt_lida += 1
                porcento = (qt_lida * 100) / qt_arq
                gerar_ocr(dir)
                os.system('cls' if os.name == 'nt' else 'clear')
                print("<%>"+str(int(porcento))+"</%>"+"<numero>"+str(qt_lida)+"</numero>"+"<dir>"+dir+"</dir>")







