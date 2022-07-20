
import os
import shutil
from pathlib import Path


paths = sorted(Path("C:\\Users\\CarlosLap\\Desktop\\AKA\\Proyecto igor\\docs").iterdir(), key=os.path.getctime)
files = []
for file in paths:
    if "xlsx" in file.name:
        files.append(file)

print(files[-1])

shutil.copy(files[-1], "C:\\Users\\CarlosLap\\Desktop")