from cryptography.fernet import Fernet
from os.path import join

def generate_key() -> bytes:
    return Fernet.generate_key()

def init_fernet(key):
    return Fernet(key)