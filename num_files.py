import os.path

def num_files():
    path = 'db.'
    result = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
    return result