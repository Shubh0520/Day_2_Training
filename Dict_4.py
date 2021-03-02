"""Write a Python script to check whether a given key already exists in a dictionary"""

dict_dt = {0: 12, 1: 34, 2: 45, 3: 56, 4: 75}


def is_key_present(key):
    if key in dict_dt:
        print(f"Key is present")
    else:
        print(f"Key is not present")


is_key_present(0)
is_key_present(2)
is_key_present(5)
