def search_cookbook(cookbook: dict,recipe: dict,section):
    if recipe in cookbook:
        f = cookbook.get(recipe)
        if section in f:
            print(f.get(section))
        else:
            print(f'There is no section "{section}" in the "{recipe}" recipe')
    else:
        print(f'There is no "{recipe}" recipe in the cookbook.')
