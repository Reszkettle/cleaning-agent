import os
import shutil
from catalogs import *

path = 'C:/Users/reszk/Downloads'

os.chdir(path)

try:
    for folder in folder_names:
        if not os.path.isdir('./' + folder):
            os.mkdir('./' + folder)
            # print('Folder: ' + folder + ' has been successfully created.')
except NotImplementedError:
    print('dir_fd is not implemented on this computer')

moved_files = 0

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
            moved_files += 1
