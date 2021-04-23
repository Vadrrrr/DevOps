def search_cookbook(cookbook: dict,recipe: dict,section):
    if recipe in cookbook:
        f = cookbook.get(recipe)
        if section in f:
            return f.get(section)
        else:
            return f'There is no section "{section}" in the "{recipe}" recipe.'
    else:
        return f'There is no "{recipe}" recipe in the cookbook.'
