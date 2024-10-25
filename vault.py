from vault.utils import read_file_data
from vault.encrypt import encrypt_dir
from vault.decrypt import decrypt_dir
from cryptography.fernet import Fernet

if __name__ == "__main__":
    path = "test/"

    fernet = Fernet(read_file_data("filekey.key"))
    encrypt_dir(fernet, path)
    decrypt_dir(fernet, path)