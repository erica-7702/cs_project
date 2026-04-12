# Personal Finance And Budget Simulation System

## Overview

This is a Python-based project designed to help users manage their financial activities. It allows users to record their income and expenses, track their balance, analyze their spending, forecast future finances, and save and load their transactions.
------------------------------------------------------------------------

## Contributors

-   Erica Boakye
-   Matilda Armah

------------------------------------------------------------------------

## Features

- Add income with categories (salary, allowance, business)
- Add expenses with categories (food, rent, transport, etc.)
- View current balance
- View all transactions
- Filter transactions by category
- Spending analysis (total, category breakdown, highest spending, averages)
- Forecast future balance
- Save data to file
- Load data from file
- Budget limits with warnings


------------------------------------------------------------------------

## Tech Stack

- Programming Language(s): Python
- Libraries: Standard Python libraries (file handling, input/output)
------------------------------------------------------------------------

## Project Structure


    project-folder/
    
├── main.py              # Main program (user interface)
├── analysis.py          # Spending analysis functions
├── file_handler.py      # Save and load functionality
├── finance_data.txt     # Data file (auto-generated)
└── README.md

------------------------------------------------------------------------

## Setup Instructions



### 1. Navigate to the project folder

```bash
cd Final_project

### 2. Run the program
python3 main.py


------------------------------------------------------------------------

## Usage
1. The user runs the program from the terminal
2. A menu is displayed with options
3. The user selects options by entering numbers


Example actions:
Add income → enter amount and category
Add expense → enter amount and category
View balance → shows current balance
Analyse spending → shows breakdown of expenses
Save → stores data in a file
Load → retrieves saved data



------------------------------------------------------------------------

## Example Output

PERSONAL FINANCE SYSTEM
1. Add Income
2. Add Expenses
3. View Balance

Current Balance: 1500

~ Spending Analysis ~
Total Expenses: 500
food : 200
rent : 300
Highest Spending Category: rent - 300


------------------------------------------------------------------------

## Challenges & Limitations

-   Used text file instead of a database
-   No graphical user interface (CLI only)
-   No user authentication system
-   Manual category input may lead to inconsistency


------------------------------------------------------------------------

## Future Improvements

-   Implement Object-Oriented Programming (classes)
-   Support multiple user accounts
-   Use a database instead of a text file


------------------------------------------------------------------------

## References
-  Python Documentation 
-  Class lecture notes
-  Online tutorials for file handling and data structures
