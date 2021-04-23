def contains(strin: str, subs: list):
    res = []
    for i in subs:
        if i.lower() in strin.lower():
            res.append(i)
    return res
