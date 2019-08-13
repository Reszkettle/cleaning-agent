import os
import shutil
from catalogs import *


def make_directories(folders):
    try:
        for folder in folders:
            if not os.path.isdir('./' + folder):
                os.mkdir('./' + folder)
    except NotImplementedError:
        print('dir_fd is not implemented on this computer')


def move_files(path):
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
