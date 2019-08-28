import os
import shutil
from catalogs import *
from tkinter import filedialog
from tkinter import Tk


def make_directories(folders, path):
    """
    Checks if directory is empty, then makes directories for special file extensions.
    :param folders: List of directories.
    :param path: Path to folder in which directories will be made.
    :return: 0 if directory is empty, 1 if directory needs to be organized.
    """
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
    """
    Moving files to corresponding folders considering their extensions.
    :param path: Path to folder containing files to move.
    :return: Number of items successfully moved. \
    """
    moved = 0
    for f in os.listdir(path):
        prefix = path + '/'
        current_dir = prefix + f
        for key in extensions.keys():
            if f.endswith(extensions[key]):
                try:
                    os.rename(current_dir, prefix + key + '/' + f)
                except OSError:
                    for i in range(10000):
                        try:
                            os.rename(current_dir, prefix + key + '/' + 'copy_' + str(i) + f)
                        except:
                            continue
                        break
                moved += 1
    return moved


def get_folder(title="Choose folder to organize"):
    """
    Selecting folder to organize.
    :param title: Title of window.
    :return: Path to selected folder.
    """
    root = Tk()
    root.iconbitmap('icon.ico')
    root.withdraw()
    path = filedialog.askdirectory(title=title)
    return path
