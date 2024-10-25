from os.path import isfile, join
from os import walk

def read_file_data(filepath: str) -> bytes:
    if isfile(filepath):
        with open(filepath, 'rb') as file:
            return file.read()

def write_data(filepath: str, data: bytes):
    if isfile(filepath):
        with open(filepath, 'wb') as f:
            f.write(data)
    
def get_file_list(root_folder: str) -> list[str]:
    file_list = []
    for dirpath, _, filenames in walk(root_folder):
        for filename in filenames:
            file_list.append(join(dirpath, filename))
    return file_list