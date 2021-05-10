import functools

def multiplier(l):
    if all(l) :
        return functools.reduce(lambda a,b : a * b,l)
    else:
        raise ValueError ("The given data is invalid.")
