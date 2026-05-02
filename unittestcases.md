
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
