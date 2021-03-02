"""Write a Python script to concatenate following dictionaries to create a new one"""

dict_one_data = {0: 25, 1: 26, 2: 28, 3: 56}
dict_two_data = {4: 234, 5: 76, 6: 20, 7: 92}
dict_result = {}
for dict_dt in (dict_one_data, dict_two_data):
    dict_result.update(dict_dt)
print(f"Concatenation of dictionaries results is: {dict_result}")
