import os

def print_filename():
    name = os.path.basename(__file__) 
    print(name)
print_filename()