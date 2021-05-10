def extractor(extractable, value_type):
    new_dict = dict(filter(lambda x: isinstance(x[1], value_type), extractable.items()))

    return new_dict

