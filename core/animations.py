# coding = utf-8
# using namespace std
try:
    from progressbar import *
except ImportError or ImportWarning:
    from os import system
    system("sudo apt-get install python-progressbar python3-progressbar")
    from progressbar import *
from time import sleep


# TODO Terminar td antes