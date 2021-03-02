"""
USE CASE - 2.

FIND THE OPTION TO STORE THE DETAILS OF ALL THE STATES IN INDIA IN AN IMMUTABLE COLLECTION.
"""

user_input = input("Enter State of India : ")
indian_states = []
indian_states.append(user_input)
states_in_india = tuple(indian_states,)
print(f"States in India are {states_in_india}")