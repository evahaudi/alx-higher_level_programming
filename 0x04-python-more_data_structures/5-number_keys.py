#!/usr/bin/python3
def number_keys(a_dictionary):
    numbr = 0
    list_keys = list(a_dictionary.keys())

    for i in list_keys:
        numbr += 1

    return (numbr)
