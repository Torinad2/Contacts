# This program manages contacts.
import contact
import pickle

# Global constants for menu choices
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

# Global constant for the filename
FILENAME = 'contacts.dat'

# main function
def main():
    # Load the existing contact dictionary and
    # assign it to mycontacts.
    mycontacts = load_contacts()

    # Initialize a variable for the user's choice.
    choice = 0

    # Process menu selections until the user
    # wants to quit the program.
    while choice != QUIT:

        # Get the user's menu choice.
        choice = get_menu_choice()

        # Process the choice.
        if choice == LOOK_UP:
            look_up(mycontacts)
        elif choice == ADD:
            add(mycontacts)
        elif choice == CHANGE:
            change(mycontacts)
        elif choice == DELETE:
            delete(mycontacts)

    # Save the mycontacts dictionary to a file.
    save_contacts(mycontacts)

def load_contacts():
    try:
        # Open the contacts.dat file for binary reading.
        with open(FILENAME, 'rb') as input_file:
            # Unpickle the dictionary.
            contact_dct = pickle.load(input_file)

    except FileNotFoundError:
        # The file was not found, so create
        # an empty dictionary.
        contact_dct = {}

    # Return the dictionary.
    return contact_dct

# The get_menu_choice function displays the menu
# and gets a validated choice from the user.
def get_menu_choice():
    print()
    print('Menu')
    print('---------------------------')
    print('1. Look up a contact')
    print('2. Add a new contact')
    print('3. Change an existing contact')
    print('4. Delete a contact')
    print('5. Quit the program')
    print()

    # Get the user's choice.
    choice = int(input('Enter your choice: '))

    # Validate the choice.
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Enter a valid choice: '))

    # return the user's choice.
    return choice

