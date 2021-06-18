import os.path
from os import path

def file_exists(filename):
    if (path.exists(filename) == True):
        print("file exists")
    else:
        print("file doesn't exist")

file_exists("test.txt")


