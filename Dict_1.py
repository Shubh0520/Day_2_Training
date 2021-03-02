""" Write a Python program to sort (ascending and descending) a dictionary by value. """

import operator

dict_data = {3: 4, 2: 3, 5: 6, 0: 1}
print(f"Dictionary defined is {dict_data}")
ascend = sorted(dict_data.items())
print(f"Sorted Dictionary in ascending order is: {ascend}")
descend = sorted(dict_data.items(), reverse=True)
print(f"Sorted Dictionary in Descending order is: {descend}")
