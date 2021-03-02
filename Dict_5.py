"""Write a Python program to iterate over dictionaries using for loops"""

dict_elements = {0: 110, 1: 120, 2: 130, 3: 140, 4: 150}


def iteration_dict():
    for (dict_key, dict_values) in dict_elements.items():
        print(dict_key, '->', dict_values)


iteration_dict()
