def raise_error(err ,msg):
    if err == 'value':
        raise ValueError (msg)
    elif err == 'key':
        raise KeyError (msg)
    elif err == 'index':
        raise IndexError (msg)
    elif err == 'memory':
        raise MemoryError (msg)
    elif err == 'name':
        raise NameError (msg)
    elif err =='eof':
        raise EOFError (msg)
    else:
        raise ValueError ('No error with such key.')