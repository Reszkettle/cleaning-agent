import os
import shutil
from catalogs import *
from tkinter import filedialog
from tkinter import Tk


def make_directories(folders, path):
    os.chdir(path=path)
    list_items = os.listdir(path=path)
    list_length = len(list_items)
    counter = 0
    for item in list_items:
        if os.path.isdir(item) or item.endswith('.ini'):
            counter += 1
    if counter == list_length:
        return 0
    try:
        for folder in folders:
            if not os.path.isdir('./' + folder):
                os.mkdir('./' + folder)
    except NotImplementedError:
        print('dir_fd is not implemented on this computer')
    return 1


def move_files(path):
    moved = 0
    for f in os.listdir(path):
        downloads_prefix = path + '/'
        current_dir = downloads_prefix + f
        for key in extensions.keys():
            if f.endswith(extensions[key]):
                try:
                    shutil.move(current_dir, downloads_prefix + key)
                except:
                    renamed_path = downloads_prefix + 'copy_' + f
                    os.rename(current_dir, renamed_path)
                    shutil.move(renamed_path, downloads_prefix + key)
                moved += 1
    return moved


def get_folder(title="Choose folder to organize"):
    root = Tk()
    root.iconbitmap('icon.ico')
    root.withdraw()
    path = filedialog.askdirectory(title=title)
    return path
