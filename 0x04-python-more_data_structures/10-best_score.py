#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return (None)

    ret = list(a_dictionary.keys())[0]
    x = set(a_dictionary.values())
    k = max(x)
    for item, key in a_dictionary.items():
        if key == k:
            ret == item
            return (ret)
