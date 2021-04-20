def contains(strin: str, subs: list):
    lstr = strin.lower()
    res = []
    for i in subs:
        if i in lstr:
            res.append(i)
    return res