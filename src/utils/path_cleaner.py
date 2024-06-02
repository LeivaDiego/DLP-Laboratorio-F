import os

def replace_slash_with_backslash(path):
    return path.replace('\\', '/')

def extract_file_name(path):
    file_name = os.path.basename(path)
    return os.path.splitext(file_name)[0]