import sys
from COcrReader import OcrReader

if len(sys.argv) == 3:
    root_dir = str(sys.argv[1])
    img_type = str(sys.argv[2])
else:
    print("Wrong arguments...")

ocrreader = OcrReader(str(root_dir).replace("_", " "))

try:
    ocrreader.generate_all(img_type)
except:
    print("Something wrong...")
