def make_unique(case):
    for i in case:
        case[i] = set(case[i])
        case[i] = list(sorted(case[i]))
    return(case)