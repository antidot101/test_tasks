def flatten(data):
    """ Converting multilevel dictionary to single-level dictionary """
    flattened_dict = {}
    for k, v in data.items():
        if type(v) is dict:
            nested_dict = flatten(v)
            for nk, nv in nested_dict.items():
                flattened_dict[str(k) + '.' + str(nk)] = nv
        else:
            flattened_dict[k] = v
    return flattened_dict
