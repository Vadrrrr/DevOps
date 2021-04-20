def song(verses: tuple, chorus: tuple):
    result = ()
    for i in verses:
        result += i + chorus
    result += chorus
    return result
