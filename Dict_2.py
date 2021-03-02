""" Write a Python script to add a key to a dictionary. """

dict_dt = {0: 100, 2: 250}
print(f"Initial dictionary object is {dict_dt}")
add_dict_dt = dict_dt.update({3: 450, 4: 1000, 1: 350})
print(f"Updated dictionary object is {dict_dt}")
