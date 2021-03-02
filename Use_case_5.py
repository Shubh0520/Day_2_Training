"""
USE CASE - 5.

STORE THE DETAILS OF ALL THE STATES IN INDIA IN A COLLECTION.
THE DETAILS SHOULD INCLUDE NAME, POPULATION, RANK BASED ON AREA
"""
import csv

states = {"307713": {"name": "Maharashtra",
                     "population": "124862220",
                     "rank": "3rd"},
          "243286": {"name": "UP",
                     "population": "199812341",
                     "rank": "4th"},
          "342239": {"name": "Rajasthan",
                     "population": "81032689",
                     "rank": "1st"}
          }
print(type(states))
print(states["307713"])
dict_keys = states.keys()
print(dict_keys)
print("*" * 40)
dict_values = states.values()
print(dict_values)

with open('indian_states.csv', 'w') as file:
    for key in states.keys():
        file.write("%s,%s\n" % (key, states[key]))
