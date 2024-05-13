from mood_response import mood_responses
import contacts_manager
import text_utils
# 1. Python Modules and Data Handling Assignment
# Objective:
# The aim of this assignment is to assess your understanding and ability to implement Python modules, both built-in and custom, and to apply data handling techniques using Python's data structures and error handling. This assignment will help solidify your grasp on creating and using modules, as well as manipulating and processing data effectively in Python.

# Task 1: Your Mood Today

# Problem Statement: Create a Python program using a custom module that asks the user how they are feeling today and responds with a custom message based on the mood entered.
# Code Example:
# ```python
# # mood_responses.py
# def mood_response(mood):
# # Implement your response logic here
# # main.py
# import mood_responses
# mood = input("How are you feeling today? ")
# print(mood_responses.mood_response(mood))
# Expected Outcome: The program should be able to take a user's mood as input (e.g., happy, sad, excited) and return a corresponding custom message.

# ```
# moods = ['happy', 'sad', 'excited', 'angry', 'relaxed', 'anxious']

def mood_today():
    
    mood = input("How are you feeling today? ") # ask user to input mood
    mood_responses(mood) # calls mood_responses() from mood_responses.py to determine response

# mood_today() # calls mood_today func to execute code




# 2. Exploring Python Modules and Data Structures Assignment
# Objective:
# The aim of this assignment is to deepen your understanding of Python modules, both built-in and custom, and to enhance your skills in working with various Python data structures like lists, dictionaries, and sets. This assignment focuses on practical applications of these concepts in real-world scenarios.

# Task 1: Contact List Manager

# Problem Statement: Create a Python script using a custom module to manage a contact list. The script should allow adding, removing, and displaying contacts stored in a list.
# Code Example:
#     # contacts_manager.py
#     # Define functions to add, remove, and display contacts

#     # main.py
#     # Implement the logic to interact with the contact manager
#  

def list_manager():
    contact_list = []  
    while True:
        # Prompt the user to choose an action
        what_to_do = input("\nadd, remove, or display contacts?:\n(enter 'done' when finished)\n").lower()

        # Check if the user wants to display contacts, but the list is empty
        if what_to_do == 'display' and len(contact_list) == 0:
            print("\nContact list is empty")
            continue

        # Check if the user wants to remove contacts, but the list is empty
        if what_to_do == 'remove' and len(contact_list) == 0:
            print("\nContact List is empty")
            continue
        
        # Check if the user wants to finish the program
        if what_to_do == "done":
            print(contact_list)
            break

        # If the user wants to add contacts, call the add_contact function
        if what_to_do == 'add':
            contacts_manager.add_contact(contact_list)

        # If the user wants to remove contacts, call the remove_contact function
        if what_to_do == "remove":
            contacts_manager.remove_contact(contact_list)

        # If the user wants to display contacts, call the display_contacts function
        if what_to_do == "display":
            contacts_manager.display_contacts(contact_list)

        # If invalid option, prompt user to try again
        else:
            print("\nPlease enter 'add', 'remove', 'display', or 'done'")


# list_manager()



# 3. Mastering Python Modules and Aliases
# Objective:
# The aim of this assignment is to enhance your proficiency in using Python modules, both standard and custom, with a specific focus on importing with aliases. This will develop your skills in organizing code, simplifying access to module components, and effectively managing namespace in Python programs.

# Task 1: Custom Module with Aliases

# Problem Statement: Create a custom module named text_utils.py with functions for string manipulation (e.g., reversing a string, capitalizing). In your main script, import this module using an alias and utilize its functions.
# Code Example:
# ```python
# # text_utils.py
# def reverse_string(s):
# # function to reverse a string
# def capitalize_string(s):
#     # function to capitalize a string

# # main.py
# # Import text_utils using an alias and utilize its functions

# ```
# Expected Outcome: Your main script should be able to use the functions from text_utils.py via an alias, demonstrating an understanding of custom module creation and aliasing.

def custom_aliases():

    test_str = input("Enter a String: ")

    print("Enter (1) to reverse or (2) to capitalize ")
    test_cases = int(input("Enter your choice: "))
    
    if test_cases == 1:
        text_utils.reverse_string(test_str)

    elif test_cases == 2:
        text_utils.capitalize_string(test_str)
    
    else:
        print("Response MUST be a number 1-3")



custom_aliases()