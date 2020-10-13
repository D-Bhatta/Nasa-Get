import atexit
import logging
import logging.config
from json import load as jload
from pathlib import Path

from cryptography.fernet import Fernet

# Configure logger lg with config for appLogger from config.json["logging"]
CONFIG_DIR = Path(__file__).resolve().parent.parent.parent
with open(CONFIG_DIR / "config.json", "r") as f:
    config = jload(f)
    logging.config.dictConfig(config["logging"])
lg = logging.getLogger("appLogger")
# lg.debug("This is a debug message")


def write_key():
    key = Fernet.generate_key()
    with open(CONFIG_DIR / "secrets.txt", "wb+") as f:
        f.write(key)


def get_key():
    with open(CONFIG_DIR / "secrets.txt", "r+") as f:
        key = f.read()
    return key.encode()


def encrypt(message: str):
    key = get_key()
    f = Fernet(key)
    return f.encrypt(message.encode()).decode()


def decrypt(message: str):
    key = get_key()
    f = Fernet(key)
    return f.decrypt(message.encode()).decode()


def cycle_keys():
    lg.debug("Exiting system")
    print(get_key())
    write_key()
    print(get_key())


write_key()
