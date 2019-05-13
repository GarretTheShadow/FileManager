# It's gonna be a file with all classes of my own file manager

import os


def change_directory(new_directory):
    os.changedir(new_directory)


def move_up_folder():
    current_path = os.getcwd()
    updated_path = current_path.rfind('\\')
    return current_path[0:updated_path]


def rename_file(input_name, output_name):

    if os.name == 'nt':
        os.rename(input_name, output_name)
        print('File renamed into: '+output_name)

    elif os.name == 'posix':
        return


move_up_folder()
