import re

def check_address(case: dict):
    pattern = '^\D+[A-z]+\s\D[A-z]+\s\d'
    res = []
    for i in case:
        if re.search(pattern, case[i]):
            res.append(f"The address of {i} is valid.")
        else:
            res.append(f"The address of {i} is invalid.")
    return res
