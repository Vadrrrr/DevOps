import re

def check_address(case: dict):
    pattern = r'^Ukraine,[ ]*[A-Za-z-[ ]*]*,[ ]*[A-Za-z-[ ]*]*[ ]*\d{1,6},[ ]*\d{5}$'
    res = []
    for i in case:
        if re.search(pattern, case[i]):
            res.append(f"The address of {i} is invalid.")
        else:
            res.append(f"The address of {i} is valid.")
    return res
