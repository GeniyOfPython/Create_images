import os

def find_path_to_file(filename):
    file_path = __file__
    file_path = file_path.split("\\")
    del file_path[-1]
    del file_path[-1]
    file_path = "\\".join(file_path)
    file_path = os.path.join(file_path, filename)
    return file_path
