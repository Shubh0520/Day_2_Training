"""
USE CASE - 1.

["hari","balu", "john"]
Iterate and print

["hari","balu", "john", "paul"]

["hari","john", "paul"]

"""

name_of_persons = [person for person in ["hari", "balu", "john"]]
print(name_of_persons[0])
print(name_of_persons[1])
print(name_of_persons[2])
print("*" * 20)

# Adding person to list
persons_list = ["hari", "balu", "john"]
updated_persons_list = persons_list + ["Paul"]
print(updated_persons_list)

# Removing person from list
updated_after_removal = [person for person in updated_persons_list if person != "balu"]
print(updated_after_removal)
