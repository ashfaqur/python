import os

size = 0

folder_path = 'C:/ash/pycharm'

for path, dirs, files in os.walk(folder_path):
    for f in files:
        fp = os.path.join(path, f)
        size += os.path.getsize(fp)
print("Directory size: " + str(round(size/1000000000,2)))
