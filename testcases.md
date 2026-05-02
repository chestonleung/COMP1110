# Testcases for Personal Budget Assistant

## Remarks
If you would like to reset the system after certain tests, you can run the following command in your terminal after navigating to the project directory:
```bash
make reset
```

## Testcase 1: Food Budget Tracking

### 1.1. Add budget rule
Objective: test the adding of a budget rule.

**Input**
```text
3
food
daily
50
```

**After these inputs, the program should output:**
```text
Budget rule added.
```

### 1.2. Verifying budget rule
Objective: test the 'view budget rules' function.

**Input**
```text
4
```

**After these inputs, the program should output:**
```text
--- Budget Rules ---
food | daily | Limit $50.00 | Activated
```

### 1.3. Add transactions
Objective: test adding transactions.

**Input**
```text
1
2026-05-02
35
food
lunch
```

**After these inputs, the program should output:**
```text
Transaction added and saved.
```

**Input**
```text
1
2026-05-03
25
food
snack
```

**After these inputs, the program should output:**
```text
Transaction added and saved.
```

### 1.4. Percentage threshold alert
Objective: to test that the alert does not wrongly activate at this stage.

**Input**
```text
6
```

**After these inputs, the program should output:**
```text
--- Budget Alerts ---
Spending Percentage Too High: food accounts for 100.0% of total spending, exceeding the 30% threshold
```
Here, there has been no triggering of the budget rule we set as our spending is only $35 < $50. 

### 1.5. Exceeding the daily budget
Objective: test the alert system for exceeding daily food budget. 

**(Add first transaction) Input**
```
1
2026-05-02
15
food
snack
```

**(Add second transaction) Input**
```
1
2026-05-02
40
food
dinner
```

**(Check alerts) Input**
```
6
```

**The program should output:**
```text
--- Budget Alerts ---
Budget Overspending: food spent $90.00 on 2026-05-02, exceeding the daily budget of $50.00
Spending Percentage Too High: food accounts for 100.0% of total spending, exceeding the 30% threshold
```

---

### 1.6. Final transaction review and exit
The user views the complete transaction history and quits the application.

**Input**
```text
2
```

**After these inputs, the program should output:**
```text
--- All Transactions ---
Date         Amount     Category        Description                   
----------------------------------------------------------------------
2026-05-02   $   35.00  food            lunch                         
2026-05-03   $   25.00  food            snack                         
2026-05-02   $   15.00  food            snack                         
2026-05-02   $   40.00  food            dinner
```

**Input**
```text
0
```

**After these inputs, the program should output:**
```text
All data saved. Goodbye!
```

## Testcase 4: Multiple Budget Categories and Deletion

### 4.1. Setting multi-category budgets
Objective: setting diverse budget rules for food, transport, and entertainment with varying periods.

**Input**
```text
3
food
monthly
600
3
transport
daily
20
3
entertainment
weekly
100
```

**After these inputs, the program should output:**
```
Budget rule added.
Budget rule added.
Budget rule added.
```


### 4.2. Logging various expenses 
Objective: log various expenses across all defined categories.

**Input**
```text
1
2025-05-02
300
food
dinner
```
```
1
2025-05-02
15
transport
bus
```
```
1
2025-05-03
100
entertainment
movie
```
```
1
2025-05-03
200
food
lunch
```
```
1
2025-05-03
20.5
transport
MTR
```
```
1
2025-05-12
58
entertainment
gacha
```
```
1
2025-05-20
120
entertainment
games
```
```
1
2025-05-21
56
food
lunch
```
After each input, the output should be:
```
Transaction added and saved.
```

### 4.3. Triggering multiple alerts
Objective: add an 'accidental' large expense and view alerts

**Input (large expense)**
```text
1
2025-05-29
1000
entertainment
PS5
```
**Input to view alerts:**
```
6
```

**After these inputs, the program should output:**
```text
--- Budget Alerts ---
Budget Overspending: transport spent $20.50 on 2025-05-03, exceeding the daily budget of $20.00
Budget Overspending: entertainment in week starting 2025-05-19 spent $120.00, exceeding the weekly budget of $100.00
Budget Overspending: entertainment in week starting 2025-05-26 spent $1000.00, exceeding the weekly budget of $100.00
Spending Percentage Too High: entertainment accounts for 68.4% of total spending, exceeding the 30% threshold
```

### 4.4. Deleting a transaction
Objective: test 'delete transaction' feature

**Input**
```text
7
```

**After these inputs, the program should output:**
```text
--- Delete Transaction ---
Select transaction to delete:
No.   Date         Amount     Category        Description                   
...
9     2025-05-29   $ 1000.00  entertainment   PS5
```

**Input**
```
9
```
**After these inputs, the program should output:**
```
Deleted transaction: 2025-05-29 $1000.00 - PS5
```

### 4.5. Checking transaction summary
Objective: test transaction summary for various categories
**Input**
```
5
```
**After this inputs, the program should output:**
```
--- Transaction Summary ---
Total Transactions: 8
Total Spending: $869.50

By Category:
  food: $556.00 (63.9%)
  transport: $35.50 (4.1%)
  entertainment: $278.00 (32.0%)
```

---

### 4.6. Exit
The user saves and closes the session.

**Input**
```text
0
```

**After these inputs, the program should output:**
```text
All data saved. Goodbye!
```

## 1. Adding transactions 
### 1.1 Standard case

Input:
```bash
1
2026-05-01
200
food
dinner
```
Intended output: 
```bash
Transaction added and saved.
```

### 1.2. Invalid date
This testcase shows error handling for an invalid date format.
#### 1.2.1: Non-numerical date format

Input:
```bash
1
cheese
```

Intended output: 
```
Invalid date format or non-existent date. Please use YYYY-MM-DD (e.g., 2025-03-20).
```
#### 1.2.2: Incorrect date format

Input:
```bash
20252003
```
Intended output: 
```
Invalid date format or non-existent date. Please use YYYY-MM-DD (e.g., 2025-03-20).
```

### 1.3. Invalid amount
The user provides non-numeric input for the amount. 

Input:
```
1
2026-05-02
apple
```

Intended output:
```
Amount must be a number, failed to add transaction.
```

### 1.4. Blank entries
The user leaves the inputs blank.

Input:
```
1


```
Intended output:
```
Amount must be a number, failed to add transaction. 
```

### 1.5. Negative amount
The user leaves the inputs blank.

Input:
```
1
2026-05-01
-50
```
Intended output:
```
The amount must be a positive number. 
```

## 2. Viewing all transactions
### 2.1. Standard case
After running the cases in Section 1, you can input:
```
2
```
to view a transaction record. The intended output is:
```


### 2.2. No transaction records
In your terminal, after navigating to the project directory, input: 
```bash
make clean
```
Then, run the program and input 
```
2
```
Intended output is:
```
No transaction records found.
```
