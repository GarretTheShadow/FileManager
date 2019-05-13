# It's gonna be a file with all classes of my own file manager

import os


def change_directory(new_directory):

    os.changedir(new_directory)
    return


def move_up_folder():

    current_path = os.getcwd()
    if os.name == 'nt' and len(current_path) > 3:
        updated_path = current_path.rfind('\\')
        return current_path[0:updated_path]

    else:
        print('Other OS unsupported yet')
    return

def make_directory(path):

    os.makedirs(path)
    return


def delete_directory(path):

    os.removedirs(path)
    print('Folder '+path+'successfully deleted')
    return

def delete_file(path):

    os.remove(path)
    return


def rename_file(src, dst):

        os.rename(src, dst)
        print(src+' Renamed into: '+dst)
        return


def copy_file(src, dst):

    #comming soon


move_up_folder()
