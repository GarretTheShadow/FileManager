# It's gonna be a file with all classes of my own file manager

import os


def change_directory(new_directory):
    try:
        os.changedir(new_directory)
    except Exception as er1:
        print("Error! ", er1)
    return


def current_path():
    return os.getcwd()


def move_up_folder():
    if os.name == 'nt' and len(current_path()) > 3:
        updated_path = current_path().rfind('\\')
        return current_path()[0:updated_path]

    else:
        print("Other OS unsupported yet")
    return


def make_directory(path):
    try:
        os.makedirs(path)
    except Exception as er1:
        print("Error! ", er1)
    return


def delete_directory(path):
    try:
        os.removedirs(path)
        print("Folder " + path + "successfully deleted")
    except Exception as er1:
        print("Error! ", er1)
    return


def delete_file(path):
    try:
        os.remove(path)
        print("File " + path + "successfully deleted")
    except Exception as er1:
        print("Error! ", er1)
    return


def rename_file(src_filename, dst_filename):
    os.rename(src_filename, dst_filename)
    print(src_filename + " Renamed into: " + dst_filename)
    return


def existing_check(dst):
    if os.path.exists(dst):
        decision = (input("File already exist, rewrite? ").upper() in ("1", "Y", "YES"))
        return decision


def copy_file(src, dst):
    try:
        if existing_check(dst) or not os.path.exists(dst):
            with open(src, encoding="utf8") as file_buffer:
                content = file_buffer.read()
            with open(dst, "w", encoding="utf8") as file_buffer:
                file_buffer.write(content)
        return
    except Exception as er1:
        print("Error! ", er1)


def cut_file(src, dst):
    try:
        if existing_check(dst) or not os.path.exists(dst):
            with open(src, encoding="utf8") as file_buffer:
                content = file_buffer.read()
            with open(dst, "w", encoding="utf8") as file_buffer:
                file_buffer.write(content)
            delete_file(src)
        return
    except Exception as er1:
        print("Error! ", er1)


copy_file("file.txt", "file2.txt")

