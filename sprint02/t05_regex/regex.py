import re

def check_address(case: dict):
    pattern = '^\D+[A-z]+\s\D[A-z]+\s\d'
    for i in case:
        if re.search(pattern, case[i]):
            print(f'The address of {i} is valid.')
        else:
            print(f'The address of {i} is invalid.')