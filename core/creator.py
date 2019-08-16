# coding = utf-8
# using namespace std
import json
from string import ascii_letters, punctuation, digits
from core.configurator import ConfigFile

configs = ConfigFile()
all_chars = ascii_letters + punctuation + digits


class EncryptionLoader(object):
    """"""
    