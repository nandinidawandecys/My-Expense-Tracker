# My Expense Tracker

# About the Project
My Expense Tracker is a simple, beginner-friendly command-line application built using Python. It allows users to enter their daily expenses one at a time, automatically calculates the total amount spent, and displays a summary when they finish.

# Features
- Enter multiple expense amounts.
- View the updated total after every valid expense.
- Type `done` or `quit` to finish entering expenses.
- Rejects zero and negative amounts.
- Handles invalid inputs without crashing.
- Displays the number of expenses and the total amount spent.

# Technologies Used
- Python 3

## Project Structure
My_Expense_Tracker
 main.py
 README.md

# How to Run
1. Make sure Python 3 is installed on your computer.
2. Extract the ZIP file.
3. Open a terminal or command prompt in the project folder.
4. Run the following command:

bash
python main.py


# How to Use
1. Run the program.
2. Enter an expense amount, for example `150` or `49.50`.
3. The program will show the amount added and the updated total.
4. Enter more expenses as needed.
5. Type `done` or `quit` to stop and view your expense summary.

# Example
*** text
Enter expense amount (or done): 150
Added: Rs. 150.00
Current total: Rs. 150.00

Enter expense amount (or done): 49.50
Added: Rs. 49.50
Current total: Rs. 199.50

Enter expense amount (or done): done

Number of expenses : 2
Total amount spent : Rs. 199.50


## Note
This is a basic console-based project. Expenses are calculated during the current run and are not saved to a file or database.
