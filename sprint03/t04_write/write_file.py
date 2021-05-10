def write_file(fn, msg=None):
    if fn.endswith('.txt'):
        fi = open(fn, 'w')
        fi.write(msg)
        fi.close()

        fi = open(fn, 'r')
        res = fi.read()
        if res != msg:
            return 'Something went wrong...'
        else:
            return f'Your message has been written to fi "{fn}".\nFile "{fn}" now contains \'' \
                   f'the following text:\n{res}'
    else:
        return f'Please enter the filename in the format "filename.txt".\nFailed to write to fi "{fn}".'