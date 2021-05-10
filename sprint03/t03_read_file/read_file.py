
def read_file(fi):
    res = ''
    if fi:
        print(f'File "{fi}" has the following message:')
        file = open(fi, 'r')
        res = file.read()
        file.close()
    else:
        return f'Failed to read file "{fi}".'

    return res