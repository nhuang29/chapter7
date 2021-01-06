import os

# retrieves environmental variables that set on the remote machine
def run(**args):
    
    print("[*] In environment module.")
    return str(os.environ)