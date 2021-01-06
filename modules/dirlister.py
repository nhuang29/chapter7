import os

# run function that lists out all the files in the current directory
def run(**args):
    
    print("[*] In dirlister module.")
    files = os.listdir(".")
    
    return str(files)