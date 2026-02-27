# Week 6 - Personal Expense Tracker

expense_records = []
category_totals = {}
unique_categories = set()

print("=== PERSONAL EXPENSE TRACKER ===")

# collect expenses
for i in range(1, 6):
    category = input(f"Enter expense {i} category: ")
    amount = float(input(f"Enter expense {i} amount: "))
    date = input("Enter date (YYYY-MM-DD): ")

    expense_records.append((category, amount, date))

# categorize expenses
for category, amount, date in expense_records:
    unique_categories.add(category)
    category_totals[category] = category_totals.get(category, 0) + amount

# Statistics
amounts = [amount for category, amount, date in expense_records]

total_spending = sum(amounts)
average_expense = total_spending / len(amounts)
highest = max(expense_records, key=lambda x: x[1])
lowest = min(expense_records, key=lambda x: x[1])

# Report
print("\n=== OVERALL SPENDING SUMMARY ===")
print(f"Total Spending: ${total_spending:.2f}")
print(f"Average Expense: ${average_expense:.2f}")
print(f"Highest Expense: ${highest[1]:.2f} ({highest[0]})")
print(f"Lowest Expense: ${lowest[1]:.2f} ({lowest[0]})")

print("\n=== UNIQUE CATEGORIES ===")
print(unique_categories)

print("\n=== SPENDING BY CATEGORY ===")
for category, total in category_totals.items():
    print(f"{category}: ${total:.2f}")
