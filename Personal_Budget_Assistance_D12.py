"""
COMP1110 Group D12 - Personal Budget Assistant
"""
import os
from datetime import datetime, timedelta

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TRANS_FILE = os.path.join(SCRIPT_DIR, "transactions.txt")
BUDGET_FILE = os.path.join(SCRIPT_DIR, "budgets.txt")

# ============================================================
# Transaction
# ============================================================
class Transaction:
    def __init__(self, date, amount, category, description):
        self.date = date
        self.amount = float(amount)
        self.category = category
        self.description = description

    def to_line(self):
        return f"{self.date}|{self.amount}|{self.category}|{self.description}"
    

def transaction_from_line(line):
    parts = line.strip().split("|")
    if len(parts) == 4:
        return Transaction(parts[0], float(parts[1]), parts[2], parts[3])
    return None


def save_transactions(transactions):
    with open(TRANS_FILE, "w", encoding="utf-8") as f:
        for t in transactions:
            f.write(t.to_line() + "\n")


def load_transactions():
    transactions = []
    try:
        with open(TRANS_FILE, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    t = transaction_from_line(line)
                    if t:
                        transactions.append(t)
    except FileNotFoundError:
        pass
    return transactions


def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def add_transaction(transactions):
    print("\n--- Adding Transaction ---")
    
    while True:
        date = input("Date (YYYY-MM-DD): ")
        if is_valid_date(date):
            break
        else:
            print("Invalid date format or non-existent date. Please use YYYY-MM-DD (e.g., 2006-10-09).")
    
    try:
        amount = float(input("Amount: "))
        category = input("Category (food, transport, shopping, etc.): ")
        description = input("Description: ")
        t = Transaction(date, amount, category, description)
        transactions.append(t)
        save_transactions(transactions)
        print("Transaction added and saved.")
    except ValueError:
        print("Amount must be a number, failed to add transaction.")


def view_transactions(transactions):
    print("\n--- All Transactions ---")
    if not transactions:
        print("No transaction records found.")
        return
    print(f"{'Date':<12} {'Amount':<10} {'Category':<15} {'Description':<30}")
    print("-" * 70)
    for t in transactions:
        print(f"{t.date:<12} ${t.amount:>8.2f}  {t.category:<15} {t.description:<30}")


# ============================================================
# Budget
# ============================================================


class BudgetRule:
    def __init__(self, category, period, threshold, enabled=True):
        self.category = category
        self.period = period
        self.threshold = float(threshold)
        self.enabled = enabled

    def to_line(self):
        return f"{self.category}|{self.period}|{self.threshold}|{self.enabled}"


def budget_from_line(line):
    parts = line.strip().split("|")
    if len(parts) == 4:
        enabled = (parts[3] == "True")
        return BudgetRule(parts[0], parts[1], float(parts[2]), enabled)
    return None


def save_budgets(budgets):
    with open(BUDGET_FILE, "w", encoding="utf-8") as f:
        for b in budgets:
            f.write(b.to_line() + "\n")


def load_budgets():
    budgets = []
    try:
        with open(BUDGET_FILE, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    b = budget_from_line(line)
                    if b:
                        budgets.append(b)
    except FileNotFoundError:
        pass
    return budgets


def add_budget(budgets):
    print("\n--- Adding Budget Rule ---")
    category = input("Category: ")
    period = input("Period (daily/weekly/monthly): ")
    try:
        threshold = float(input("Budget Limit: "))
        b = BudgetRule(category, period, threshold)
        budgets.append(b)
        save_budgets(budgets)
        print("Budget rule added.")
    except ValueError:
        print("Budget limit must be a number.")


def view_budgets(budgets):
    print("\n--- Budget Rules ---")
    if not budgets:
        print("No budget rules found.")
        return
    for b in budgets:
        status = "Activated" if b.enabled else "Deactivated"
        print(f"{b.category} | {b.period} | Limit ${b.threshold:.2f} | {status}")


# ============================================================
# Summary
# ============================================================


def show_summary(transactions):
    total = 0
    for t in transactions:
        total += t.amount
    print("\n--- Transaction Summary ---")
    print(f"Total Transactions: {len(transactions)}")
    print(f"Total Spending: ${total:.2f}")
    if transactions:
        cat_total = {}
        for t in transactions:
            cat_total[t.category] = cat_total.get(t.category, 0) + t.amount
        print("\nBy Category:")
        for cat, amt in cat_total.items():
            pct = (amt / total * 100) if total > 0 else 0
            print(f"  {cat}: ${amt:.2f} ({pct:.1f}%)")


# ============================================================
# Rule Based Alerts
# ============================================================


def get_spent_in_period(transactions, category, start_date, end_date):
    total = 0
    for t in transactions:
        if category and t.category != category:
            continue
        if start_date and t.date < start_date:
            continue
        if end_date and t.date > end_date:
            continue
        total += t.amount
    return total


def check_budget_alerts(transactions, budgets):
    alerts = []
    
    today = datetime.now().strftime("%Y-%m-%d")
    for b in budgets:
        if not b.enabled:
            continue
        
        if b.period == "daily":
            continue
        
        if b.period == "weekly":
            dt = datetime.now()
            start = (dt - timedelta(days=dt.weekday())).strftime("%Y-%m-%d")
            end = today
        elif b.period == "monthly":
            start = datetime.now().replace(day=1).strftime("%Y-%m-%d")
            end = today
        else:
            continue
        
        spent = get_spent_in_period(transactions, b.category, start, end)
        if spent > b.threshold:
            alerts.append({
                "type": "budget",
                "category": b.category,
                "period": b.period,
                "spent": spent,
                "threshold": b.threshold,
                "message": f"Budget Overspending: {b.category} this{b.period} has spent ${spent:.2f}, exceeding the budget of ${b.threshold:.2f}"
            })
    
    for b in budgets:
        if not b.enabled or b.period != "daily":
            continue
        
        daily_spent = {}
        for t in transactions:
            if t.category != b.category:
                continue
            daily_spent[t.date] = daily_spent.get(t.date, 0) + t.amount
        
        for date, spent in daily_spent.items():
            if spent > b.threshold:
                alerts.append({
                    "type": "budget",
                    "category": b.category,
                    "period": "daily",
                    "date": date,
                    "spent": spent,
                    "threshold": b.threshold,
                    "message": f"Budget Overspending: {b.category} spent ${spent:.2f} on {date}, exceeding the daily budget of ${b.threshold:.2f}"
                })
    
    return alerts


def check_percentage_alerts(transactions, threshold_percent=30):
    alerts = []
    total = sum(t.amount for t in transactions)
    if total == 0:
        return alerts
    cat_totals = {}
    for t in transactions:
        cat_totals[t.category] = cat_totals.get(t.category, 0) + t.amount
    for cat, amt in cat_totals.items():
        pct = (amt / total) * 100
        if pct > threshold_percent:
            alerts.append({
                "type": "percentage",
                "category": cat,
                "percentage": pct,
                "threshold": threshold_percent,
                "message": f"Spending Percentage Too High: {cat} accounts for {pct:.1f}% of total spending, exceeding the {threshold_percent}% threshold"
            })
    return alerts


def check_uncategorized_alerts(transactions):
    alerts = []
    for i, t in enumerate(transactions):
        if t.category == "" or t.category.lower() == "uncategorized":
            alerts.append({
                "type": "uncategorized",
                "transaction": t,
                "message": f"Uncategorized Transaction: {t.date} ${t.amount} - {t.description}"
            })
    return alerts


def check_consecutive_overspending(transactions, budgets, consecutive_days=3):
    from datetime import datetime, timedelta

    daily_spent = {}
    for t in transactions:
        if t.date not in daily_spent:
            daily_spent[t.date] = {}
        daily_spent[t.date][t.category] = daily_spent[t.date].get(t.category, 0) + t.amount

    alerts = []
    for b in budgets:
        if not b.enabled or b.period != "daily":
            continue

        dates_with_cat = [d for d, cats in daily_spent.items() if b.category in cats]
        if not dates_with_cat:
            continue

        min_date = min(dates_with_cat)
        max_date = max(dates_with_cat)
        start = datetime.strptime(min_date, "%Y-%m-%d")
        end = datetime.strptime(max_date, "%Y-%m-%d")

        consecutive = 0
        current = start
        while current <= end:
            date_str = current.strftime("%Y-%m-%d")
            spent = daily_spent.get(date_str, {}).get(b.category, 0)
            if spent > b.threshold:
                consecutive += 1
                if consecutive >= consecutive_days:
                    alerts.append({
                        "type": "consecutive",
                        "category": b.category,
                        "days": consecutive_days,
                        "message": f"Consecutive Overspending: {b.category} has exceeded the daily budget ${b.threshold:.2f} for {consecutive_days} consecutive days"
                    })
                    break
            else:
                consecutive = 0
            current += timedelta(days=1)

    return alerts


def check_all_alerts(transactions, budgets):
    all_alerts = []
    all_alerts.extend(check_budget_alerts(transactions, budgets))
    all_alerts.extend(check_percentage_alerts(transactions, 30))
    all_alerts.extend(check_uncategorized_alerts(transactions))
    all_alerts.extend(check_consecutive_overspending(transactions, budgets, 3))
    return all_alerts


def show_alerts(transactions, budgets):
    print("\n--- Budget Alerts ---")
    alerts = check_all_alerts(transactions, budgets)
    if not alerts:
        print("No alerts triggered. Everything is good!")
    else:
        for alert in alerts:
            print(alert["message"])

# ============================================================
# Main Menu
# ============================================================
def main():
    transactions = load_transactions()
    budgets = load_budgets()

    while True:
        print("\n" + "="*50)
        print("       Personal Budget Assistant")
        print("="*50)
        print("1. Add Transaction")
        print("2. View All Transactions")
        print("3. Add Budget Rule")
        print("4. View Budget Rules")
        print("5. Show Spending Summary")
        print("6. View Alerts")
        print("0. Quit")
        print("="*50)
        choice = input("Please select an option: ")

        if choice == "1":
            add_transaction(transactions)
        elif choice == "2":
            view_transactions(transactions)
        elif choice == "3":
            add_budget(budgets)
        elif choice == "4":
            view_budgets(budgets)
        elif choice == "5":
            show_summary(transactions)
        elif choice == "6":
            show_alerts(transactions, budgets)
        elif choice == "0":
            save_transactions(transactions)
            save_budgets(budgets)
            print("All data saved. Goodbye!")
            break
        else:
            print("Invalid input, please try again")


main()
