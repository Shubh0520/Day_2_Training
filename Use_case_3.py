"""
USE CASE - 3.

STORE/SAVE THE VALUES OF LIST INTO A TEXT FILE.
"""
user_input = input("Enter State of India : ")
indian_states = []
indian_states.append(user_input)
states_in_india = tuple(indian_states, )
with open("indian_states.txt", "w") as file:
    for list_item in indian_states:
        file.write("%s" % list_item + '\n')
