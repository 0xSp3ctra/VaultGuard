from os.path import join, isfile
from vault.utils import *
import time

def decrypt_file_data(fernet, data: bytes):
    return fernet.decrypt(data)

def decrypt_dir(fernet, path: str):
    filenames = get_file_list(path)

    start = time.time()
    for filename in filenames:
        if isfile(filename):
            file_data = read_file_data(filename)
            decrypted_file_data = decrypt_file_data(fernet, file_data)
            write_data(filename, decrypted_file_data)
    
    end = time.time()
    print(f"Finished decrypting {len(filenames)} files in {end - start}")