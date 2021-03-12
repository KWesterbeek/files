__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os

cache_location = ".\\cache\\"


def clean_cache():
    try:
        # checks if cache exists and moves into it
        os.chdir(cache_location)
    except:
        # creates cache folder
        os.mkdir(cache_location)
    else:
        # The following will only be executed if cache already existed.
        # creates list of files in cache and loops over the list to delete
        cache_content = os.listdir()
        for file in cache_content:
            os.remove(file)
        # changes current working directory back to the parent of cache
        os.chdir("..")


def cache_zip(file_path, cache_dir_path):
    from zipfile import ZipFile

    # Clean cache or create it:
    clean_cache()
    # unzips contents of zipfile (file_path) into cache_dir_path
    with ZipFile(file_path, "r") as zip_object:
        zip_object.extractall(path=cache_location)


def cached_files():
    # for the .path method to give a list of absolute paths the scandir must be
    # executed with an absolute path as argument.
    # the following gives us the absolute path of the cache folder
    os.chdir(cache_location)
    cache_path_absolute = os.getcwd()
    os.chdir("..")
    # this will create a list of objects of the os.DirEntry class
    file_objects = os.scandir(path=cache_path_absolute)
    # creates an empty list to hold the file paths of the files in cache
    file_paths = []
    # Loops over the file objects to get their absolute paths and put
    # it in the file_paths list
    for file_object in file_objects:
        file_path = file_object.path
        file_paths.append(file_path)

    return file_paths


def find_password(cached_files):
    # loops over the cached files one by one and opens them
    for file in cached_files:
        txt_file = open(file, "r")
        # then loops over the lines in the opened file
        for line in txt_file:
            # if the line contains password it will slice from the space
            # till the end of the line and put that in the variable 'password'
            # it will close the file and return password thus ending the loops
            if "password" in line:
                password = line[line.find(" ") + 1 : -1]
                txt_file.close

                return password
