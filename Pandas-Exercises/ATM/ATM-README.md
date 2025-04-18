### ATM project

# Project Guidlines:

This project uses different Python concepts to build a program that will simulate the behaviour of an ATM. It follows these instructions:
- Print a main menu to ask the user different options for displaying the bank account balance, for depositing money, to withdraw money, and to exit from the ATM. Ideally create a function for each menu option to be executed. Use conditional statements for asking the user the different menu options.
Additional (optional): Ask the user a PIN to access to the ATM menu once the PIN is correct otherwise ask the user to try again.
- Prompt the user to enter an option:
  - If ‘1’ is entered, display the current balance and return to main menu.
  - If ‘2’ is entered, print a sub-menu with different withdrawal amounts (give also a choice for “other amount’ to let the user enter an amount) :
  - Check that the requested withdrawal is allowed, print a message to show that the money has been withdrawn, calculate the new balance and return to main menu.
  - If ‘other_amount’ is selected, then prompt the user for an integer value. Check this number is a multiple of 10 and that the withdrawal is permitted, print a message to show that the money has been withdrawn, calculate the new balance and return to main menu.
  - If ‘exit’ is selected print a goodbye message and exit (break).
  - If another value is entered, print an error message and print the menu again.

-Re-use the ATM menu options across the program to ask the user if he/she would like to perform another operation on the bank account.

# The finished script

The finished script uses several different python concept, including the following:
- If, elif, else conditionals.
- For and While loops with breaks and boolean checks.
- String formatting and identification.
- Functions with parameters.
- Read/Write operations to .csv files.
- Pandas DB to store, search, and append data.
