# glob module can loop each files and their contents
import glob

myfiles = glob.glob("__pycache__/files/*.txt")

for filepath in myfiles:
    with open(filepath, 'r') as file:
        print(file.read().upper())
