#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return (None)
    x = set(a_dictionary.values())
    k = max(x)
    for item, key in a_dictionary.items():
        if key == k:
            return (item)
