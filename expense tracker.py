# =====================================
# Project 2 - Expense Tracker
# =====================================

print("===================================")
print("       EXPENSE TRACKER")
print("===================================")

total = 0.0

while True:
    expense = input("Enter expense amount (or type 'done' to finish): ")

    if expense.lower() == "done":
        break

    try:
        amount = float(expense)

        if amount < 0:
            print("Expense cannot be negative.")
            continue

        total += amount
        print(f"Current Total: {total:.2f}")

    except ValueError:
        print("Please enter a valid number.")

print("\n===================================")
print(f"Total Spent: {total:.2f}")
print("Thank you for using Expense Tracker!")
print("===================================")