from folder_functions import *

path = get_path()
if path is not None:
    make_directories(folder_names)
    move_files(path)
