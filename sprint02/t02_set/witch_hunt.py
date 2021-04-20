def witch_hunt(suspect_sets,innocent_sets):
    if (not suspect_sets and not innocent_sets) or not suspect_sets:
        return set()
    elif suspect_sets and innocent_sets:
        witch = set.intersection(*suspect_sets)
        print(sorted(witch.difference(*innocent_sets)))
    elif not innocent_sets:
        print(set.intersection(*suspect_sets))
