# COMP1110
# Personal Budget Assistant

## Overview

Personal Budget Assistant is a command-line application that helps users manage their personal finances by tracking transactions, setting budget rules, and receiving alerts about spending patterns. The program provides features to add transactions, view spending summaries, set budget limits across different time periods, and automatically detect spending anomalies.

## Project Structure

### Files

- **Personal_Budget_Assistance_D12.py** - The main application file containing all the logic for:
  - Transaction management (add, view, delete transactions)
  - Budget rule management (add, view, delete budget rules)
  - Spending summary and analysis
  - Alert system for budget overruns and spending anomalies
  - Data persistence (loading/saving to text files)

- **transactions.txt** - Data file storing all recorded transactions (created automatically)
  - Format: `date|amount|category|description`

- **budgets.txt** - Data file storing all budget rules (created automatically)
  - Format: `category|period|threshold|enabled`

## Features

- **Transaction Management**: Add, view, and delete financial transactions with date, amount, category, and description
- **Budget Rules**: Create daily, weekly, or monthly budget limits for specific spending categories
- **Spending Summary**: View total spending and breakdown by category with percentages
- **Multi-Level Alerts**: Automatic detection of:
  - Budget overruns (exceeding category limits)
  - High spending percentages (categories exceeding 30% of total)
  - Uncategorized transactions
  - Consecutive days of overspending

## Requirements

- Python 3.6 or higher

## How to Run

1. Open a terminal and navigate to the project directory
2. Run the program with:
   ```bash
   python3 Personal_Budget_Assistance_D12.py
   ```
   or
   ```bash
   python Personal_Budget_Assistance_D12.py
   ```

3. The program will display a main menu with the following options:
   - **1**: Add a new transaction
   - **2**: View all recorded transactions
   - **3**: Add a new budget rule
   - **4**: View all budget rules
   - **5**: Display spending summary
   - **6**: View budget alerts
   - **7**: Delete a transaction
   - **8**: Delete a budget rule
   - **0**: Quit the program

## Usage Instructions

### Adding a Transaction
- Select option 1
- Enter date in format `YYYY-MM-DD`
- Enter transaction amount (positive number)
- Enter category (e.g., food, transport, shopping)
- Enter a description

### Setting a Budget Rule
- Select option 3
- Enter the category to limit
- Select period: daily, weekly, or monthly
- Enter the budget limit amount

### Checking Alerts
- Select option 6 to view all active alerts including budget overruns and spending anomalies

## Data Storage

- All transactions and budget rules are automatically saved to `transactions.txt` and `budgets.txt`
- These files are stored in the same directory as the Python script
- Data persists between program sessions
