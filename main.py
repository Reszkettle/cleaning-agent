from folder_functions import make_directories, move_files, get_folder, folder_names

path = get_folder()
if path is not None:
    make_directories(folder_names, path)
    move_files(path)
