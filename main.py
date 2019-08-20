from folder_functions import *

path = get_folder()
if path is not None:
    make_directories(folder_names, path)
    move_files(path)
