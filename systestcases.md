# System Testcases for Personal Budget Assistant

## Remarks
**Please reset the system after each test.**
To do this, you can run the following command in your terminal after navigating to the project directory:
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

## Testcase 2: Transport Budget Tracking

### 2.1. Add budget rule
Objective: test the adding of a budget rule for transport.

Input
```text
3
transport
monthly
100
```

After these inputs, the program should output:
```text
--- Adding Budget Rule ---
Category: transport
Period (daily/weekly/monthly): monthly
Budget Limit: 100
Budget rule added.
```

### 2.2. Add initial transactions
Objective: log the first few public transport expenses.

Input
```text
1
2026-05-02
4.5
transport
MTR
1
2026-05-03
12.1
transport
MTR
1
2026-05-04
14.2
transport
MTR
1
2026-05-04
14.2
transport
MTR
```

After these inputs, the program should output:
```text
Transaction added and saved.
```

### 2.3. Delete a transaction
Objective: test the 'delete transaction' feature on a duplicate entry.

Input
```text
7
4
```

After these inputs, the program should output:
```text
--- Delete Transaction ---

Select transaction to delete:
No.   Date         Amount     Category        Description                   
---------------------------------------------------------------------------
1     2026-05-02   $    4.50  transport       MTR                           
2     2026-05-03   $   12.10  transport       MTR                           
3     2026-05-04   $   14.20  transport       MTR                           
4     2026-05-04   $   14.20  transport       MTR                           

Enter the number of the transaction to delete (0 to cancel): 4
Deleted transaction: 2026-05-04 $14.20 - MTR
```

### 2.4. Logging additional expenses
Objective: log the rest of the monthly transport expenses.

Input
```text
1
2026-05-05
6.7
transport
MTR
1
2026-05-07
12.1
transport
MTR
1
2026-05-10
20.7
transport
MTR
1
2026-05-12
17.2
transport
MTR
1
2026-05-13
14.4
transport
MTR
1
2026-05-17
13.2
transport
MTR
```

After these inputs, the program should output:
```text
Transaction added and saved.
```

### 2.5. Checking transaction summary
Objective: view the summary for the transport category.

Input
```text
5
```

After these inputs, the program should output:
```text
--- Transaction Summary ---
Total Transactions: 9
Total Spending: $115.10

By Category:
  transport: $115.10 (100.0%)
```

### 2.6. View all transactions
Objective: test the 'view all transactions' feature.

Input
```text
2
```

After these inputs, the program should output:
```text
--- All Transactions ---
Date         Amount     Category        Description                   
----------------------------------------------------------------------
2026-05-02   $    4.50  transport       MTR                           
2026-05-03   $   12.10  transport       MTR                           
2026-05-04   $   14.20  transport       MTR                           
2026-05-05   $    6.70  transport       MTR                           
2026-05-07   $   12.10  transport       MTR                           
2026-05-10   $   20.70  transport       MTR                           
2026-05-12   $   17.20  transport       MTR                           
2026-05-13   $   14.40  transport       MTR                           
2026-05-17   $   13.20  transport       MTR
```

### 2.7. Triggering budget alerts
Objective: check alerts after exceeding the monthly transport budget.

Input
```text
6
```

After these inputs, the program should output:
```text
--- Budget Alerts ---
Budget Overspending: transport in 2026-05 spent $115.10, exceeding the monthly budget of $100.00
Spending Percentage Too High: transport accounts for 100.0% of total spending, exceeding the 30% threshold
```

### 2.8. Delete budget rule
Objective: test deleting a budget rule.

Input
```text
8
```
After these inputs, the program should output:
```text
--- Delete Budget Rule ---

Select budget rule to delete:
No.   Category        Period     Limit      Status    
-------------------------------------------------------
1     transport       monthly    $100.00    Activated 
```

Input: 
```
1
```
After these inputs, the program should output:
```
Deleted budget rule: transport | monthly | $100.00
```

### 2.9. Verifying budget rule deletion
Objective: verify the rules list is empty.

Input
```text
4
```

After these inputs, the program should output:
```text
--- Budget Rules ---
No budget rules found.
```

### 2.10. Exit
Objective: save and close the session.

Input
```text
0
```

After these inputs, the program should output:
```text
All data saved. Goodbye!
```

---

## Testcase 3: Entertainment Budget Tracking

#### 3.1. Add budget rule
Objective: test the adding of a weekly entertainment budget rule.

Input
```text
3
entertainment
weekly
400
```

After these inputs, the program should output:
```text
--- Adding Budget Rule ---
Budget rule added.
```

### 3.2. Add a transaction with an incorrect category
Objective: input a transaction to later test deletion.

Input
```text
1
2025-05-02
120
cinema
cinema
```

After these inputs, the program should output:
```text
Transaction added and saved.
```

### 3.3. Delete transaction
Objective: remove the previously added wrong transaction.

Input
```text
7
```

After these inputs, the program should output:
```text
--- Delete Transaction ---

Select transaction to delete:
No.   Date         Amount     Category        Description                   
---------------------------------------------------------------------------
1     2025-05-02   $  120.00  cinema          cinema                        
```
Input
```
1
```
After these inputs, the program should output:
```
Deleted transaction: 2025-05-02 $120.00 - cinema
```

### 3.4. Log valid expenses
Objective: add entertainment transactions within limits.

Input
```text
1
2026-05-02
120
entertainment
cinema
1
2026-05-12
350
entertainment
concert
```

After these inputs, the program should output:
```text
Transaction added and saved.
```

### 3.5. Percentage threshold alert
Objective: check alerts before exceeding the monetary budget rule.

Input
```text
6
```

After these inputs, the program should output:
```text
--- Budget Alerts ---
Spending Percentage Too High: entertainment accounts for 100.0% of total spending, exceeding the 30% threshold
```

### 3.6. Verifying budget rule
Objective: view the active budget rules.

Input
```text
4
```

After these inputs, the program should output:
```text
--- Budget Rules ---
entertainment | weekly | Limit $400.00 | Activated
```

### 3.7. Exceeding the weekly budget
Objective: add a transaction that pushes the weekly spending over the limit.

Input
```text
1
2026-05-14
120
entertainment
live band show
```

After these inputs, the program should output:
```text
Transaction added and saved.
```

### 3.8. Checking transaction summary
Objective: view the total entertainment spending.

Input
```text
5
```

After these inputs, the program should output:
```text
--- Transaction Summary ---
Total Transactions: 3
Total Spending: $590.00

By Category:
  entertainment: $590.00 (100.0%)
```

### 3.9. Checking overspending alerts
Objective: confirm the budget overspending alert triggers for the week.

Input
```text
6
```

After these inputs, the program should output:
```text
--- Budget Alerts ---
Budget Overspending: entertainment in week starting 2026-05-11 spent $470.00, exceeding the weekly budget of $400.00
Spending Percentage Too High: entertainment accounts for 100.0% of total spending, exceeding the 30% threshold
```

### 3.10. Modifying the budget limit
Objective: delete the original rule and replace it with a higher limit.

**Input**
```text
8
1
```

**After these inputs, the program should output:**
```text
Deleted budget rule: entertainment | weekly | $400.00
```

**Input**
```
3
entertainment
weekly
1000
```
**After these inputs, the program should output:**
```
--- Adding Budget Rule ---
Category: entertainment
Period (daily/weekly/monthly): weekly
Budget Limit: 1000
Budget rule added.
```

### 3.11. Verify resolved overspending alert
Objective: confirm the overspending alert is gone after raising the budget.

Input
```text
6
```

After these inputs, the program should output:
```text
--- Budget Alerts ---
Spending Percentage Too High: entertainment accounts for 100.0% of total spending, exceeding the 30% threshold
```

### 3.12. Exit
Objective: save and close the session.

Input
```text
0
```

After these inputs, the program should output:
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
