def sum_dict(dict_1, dict_2):
    all_keys = set()
    dict_3 = {}
    for key in dict_1.keys():
        all_keys.add(key)

    for key in dict_2.keys():
        all_keys.add(key)

    for key in all_keys:
        dict_3[key] = 0
        if key in dict_1:
            dict_3[key] += dict_1[key]
        if key in dict_2:
            dict_3[key] += dict_2[key]

    return dict_3