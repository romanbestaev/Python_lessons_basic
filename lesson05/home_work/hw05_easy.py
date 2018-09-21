import os
import sys
from shutil import copyfile
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
def folds_on():
    for i in range(1,10):
        try:
            os.mkdir('dir_'+str(i))
        except:
            continue
    return 0

def folds_off():
    for i in range(1,10):
        try:
            os.rmdir('dir_'+str(i))
        except:
            continue    
    return 0
#folds_on()
#folds_off()


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def print_all_dir():
    dirs = []
    i = 0
    print('Список папок:')
    for x in os.listdir():
        if os.path.isdir(x):
            i += 1
            print(i,x)
            dirs.append(x)
    return(dirs)
#print_all_dir()


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
def copy_this_file():
    src = str(sys.argv[0])
    dst = src.replace('.py','_copy.py')
    copyfile(src, dst)
#copy_this_file()