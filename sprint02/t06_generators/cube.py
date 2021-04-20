def cube(intg: int):
    while intg > 0:
        yield intg ** 3
        intg -= 1