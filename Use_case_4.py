"""
USE CASE - 4.

READ THE TEXT FILE AND LOAD THE DATA AS A LIST
"""

with open("indian_states.txt", "r") as file:
    file_content = file.readlines()
    print(file_content)

