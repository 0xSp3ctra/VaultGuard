from os.path import join, isfile
from vault.utils import *
import time

def encrypt_file_data(fernet, data: bytes):
    return fernet.encrypt(data)

def encrypt_dir(fernet, path: str):
    filenames = get_file_list(path)

    start = time.time()
    for filename in filenames:
        if isfile(filename):
            file_data = read_file_data(filename)
            encrypted_file_data = encrypt_file_data(fernet, file_data)
            write_data(filename, encrypted_file_data)

    end = time.time()
    print(f"Finished encrypting {len(filenames)} files in {end - start}")