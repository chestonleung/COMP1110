# Unit Test Cases


# 1. Adding transactions

## 1.1. Standard case
Input:
```text
1
2026-05-01
200
food
dinner
```

Intended output:
```text
Transaction added and saved.
```

## 1.2. Invalid date
This testcase shows error handling for an invalid date format.

### 1.2.1. Non-numerical date format
Input:
```text
1
cheese
```

Intended output:
```text
Invalid date format or non-existent date. Please use YYYY-MM-DD (e.g., 2025-03-20).
```

### 1.2.2. Incorrect date format
Input:
```text
1
20250320
```

Intended output:
```text
Invalid date format or non-existent date. Please use YYYY-MM-DD (e.g., 2025-03-20).
```

## 1.3. Invalid amount
The user provides non-numeric input for the amount.

Input:
```text
1
2026-05-02
apple
```

Intended output:
```text
Amount must be a number, failed to add transaction.
```

## 1.4. Blank entries
The user leaves the inputs blank.

Input:
```text
1
[Enter]
```

Intended output:
```text
Amount must be a number, failed to add transaction.
```

## 1.5. Negative amount
The user inputs a negative amount.

Input:
```text
1
2026-05-02
-50
```

Intended output:
```text
The amount must be a positive number.
```

# 2. Viewing all transactions

## 2.1. Standard case
After running the cases in Section 1, you can input:
```text
2
```
to view a transaction record. The intended output is:
```text
All Transactions
Date         Amount     Category    Description
2020-10-01   $ 200.00   food        lunch
2020-10-01   $ 60.00    food        dinner
2020-10-02   $ 30.00    food        breakfast
2020-10-02   $ 7.50     transport   mtr
```

## 2.2. No transaction records
In your terminal, after navigating to the project directory, input:
```bash
make clean
```
Then, run the program and input:
```text
2
```

Intended output is:
```text
No transaction records found.
```

# 3. Budget rules and viewing budget rules

## 3.1. Standard inputs
Input:
```text
3
shopping
weekly
200
```

Intended output:
```text
Budget rule added.
```

## 3.2. Invalid period input
Input:
```text
3
ABCD
2
```

Intended output:
```text
Invalid period. Please choose from daily, weekly, monthly.
```

## 3.3. Invalid budget limit
Input:
```text
3
abc
daily
abc
```

Intended output:
```text
Budget limit must be a number.
```

## 3.4. Viewing budget rules
Input:
```text
4
```

Intended output:
```text
Budget Rules
food | weekly | Limit $500.00 | Activated
shopping | weekly | Limit $200.00 | Activated
abc | 2 | Limit $2.00 | Activated
```

## 3.5. Viewing budget rules when there are none
Input:
```text
4
```

Intended output:
```text
No budget rules found.
```

# 4. Spending summary

## 4.1. Standard case
Input:
```text
5
```

Intended output:
```text
Transaction Summary
Total Transactions: 5
Total Spending: $912.00

By Category:
food: $200.00 (21.9%)
shopping: $300.00 (32.9%)
transport: $267.00 (29.3%)
gift: $78.00 (8.6%)
dinner: $67.00 (7.3%)
```

## 4.2. No transactions
Input:
```text
5
```

Intended output:
```text
Transaction Summary
Total Transactions: 0
Total Spending: $0.00
```

# 5. Spending alert

## 5.1. Standard input
Input:
```text
6
```

Intended output:
```text
Budget Alerts
Budget Overspending: food spent $201.00 on 2020-10-10, exceeding the daily budget of $200.00
Spending Percentage Too High: food accounts for 100.0% of total spending, exceeding the 30% threshold
```

# 6. Selection menu

## 6.1. Invalid options
Input:
```text
12
```

Intended output:
```text
Invalid input, please try again
```

Input:
```text
abc
```

Intended output:
```text
Invalid input, please try again
```

# 7. Delete transaction

## 7.1. Standard case
Input:
```text
7
1
```

Intended output:
```text
Deleted transaction: 2026-05-02 $200.00 dinner
```

## 7.2. Invalid numerical delete index
Input:
```text
7
12
```

Intended output:
```text
Invalid number. Deletion cancelled.
```

## 7.3. Non-numerical delete index
Input:
```text
7
a
```

Intended output:
```text
Invalid input. Please enter a number.
```

# 8. Delete budget rule

## 8.1. Standard case
Input:
```text
8
1
```

Intended output:
```text
Deleted budget rule: transport | monthly | $100.00
```

## 8.2. No budget rules in place
Input:
```text
8
```

Intended output:
```text
No budget rules found.
```
