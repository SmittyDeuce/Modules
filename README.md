# Modules Assignment

## Overview

This repository contains my attempt at the Modules assignment from Coding Temple. The assignment covers importing both built-in modules and custom modules.

## File Structure

- **main.py**: This file contains the main program logic. It imports and utilizes modules for various tasks.
- **mood_response.py**: This module handles mood responses. It includes a function to generate a response based on a given mood.
- **contacts_manager.py**: This module manages contacts. It includes functions to add, remove, and display contacts.
- **text_utils.py**: This module provides utility functions for string manipulation, such as reversing a string and capitalizing it.

## Usage

1. **main.py**: This is the main program file. It imports `mood_response.py`, `contacts_manager.py`, and `text_utils.py` to perform various tasks, such as managing contacts, generating mood-based responses, and string manipulation.
2. **mood_response.py**: This module defines a function to generate responses based on different moods. It is imported into `main.py` to provide mood-specific responses.
3. **contacts_manager.py**: This module manages contacts. It includes functions to add, remove, and display contacts.
4. **text_utils.py**: This module provides utility functions for string manipulation, such as reversing a string and capitalizing it.

## `list_manager()` Function

The `list_manager()` function in `main.py` is responsible for managing a contact list. Here's a breakdown of how it works:

- The function initializes an empty list to store contacts.
- It enters a loop where it continuously prompts the user to choose an action: add, remove, display contacts, or finish the program.
- If the user chooses to display or remove contacts but the list is empty, it prints a message indicating that the list is empty and continues the loop.
- If the user chooses to finish the program, it prints the current contact list and exits the loop.
- If the user chooses to add, remove, or display contacts, it calls the corresponding functions from `contacts_manager.py`.
- If the user enters an invalid option, it prompts them to try again.
- Finally, it calls the `list_manager()` function to start the program.

## `mood_today()` Function

The `mood_today()` function in `main.py` prompts the user to input their current mood and generates a response based on the input. Here's how it works:

- It prompts the user to enter their current mood.
- It then calls the `mood_responses()` function from `mood_response.py` to generate a custom message based on the mood entered by the user.

## `custom_aliases()` Function

The `custom_aliases()` function in `main.py` is responsible for demonstrating the usage of utility functions for string manipulation defined in `text_utils.py`. Here's how it works:

- The function prompts the user to enter a string.
- It then prompts the user to choose an action: reverse the string or capitalize it.
- Depending on the user's choice, it calls the corresponding utility function from `text_utils.py`.
- If the user enters an invalid option, it prints a message indicating the response must be a number 1 or 2.

## Instructions

To run the main program, execute `main.py` in your Python environment. check all modules are imported to `main.py` to avoid import errors.