# ------------------------------------------------------------------------ #
# Title: Assignment 07
# Description: Working with Exception Handling and Pickling
#
# ChangeLog (JBernales, 5.31.2023, edited script):
# JBernales,5.29.2023, Created code

# ------------------------------------------------------------------------ #

import pickle

# Processing----------------------------------------------------------- #
def save_data(data, filename):  # Saves user's name to the file name they selected
    try:
        with open(filename, 'wb') as file:  # Write binary file with selected file name
            pickle.dump(data, file)  # Add the user's input name to the pickle
        print(f"Data saved to {filename} successfully.")  # Displays message confirming user data has been saved
    except IOError:
        print("Error: Unable to save data to file.")  # Displays error message if user enters wrong format for name


def is_valid_input(user_input):  # Checks if the user's input is letters only - no numbers or characters
    # Check if the input is a string
    if not isinstance(user_input, str):
        return False

    # Check if the string contains only alphabetic characters
    if not user_input.isalpha():
        return False

    return True


# Ask for input from the user
while True:
    data = input("Enter your name (using letters only!): ")  # Displays prompt for user's name

    if is_valid_input(data):  # If name is letters only, move to next code block
        break
    else:  # If not, display custom error message
        print("Error: Invalid input. Please enter letters only - no numbers or special characters!")

filename = input("Enter filename to save data: ")  # Prompts user to name file to save name input

# Save data
save_data(data, filename)
