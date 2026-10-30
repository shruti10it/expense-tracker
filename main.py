import json
import os

FILE_NAME = "expenses.json"


def load_expenses():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except:
            return []
    return []


def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    try:
        amount = float(input("Enter expense amount: "))

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        category = input("Enter category (Food/Travel/Shopping/Other): ")
        description = input("Enter description: ")

        expense = {
            "amount": amount,
            "category": category,
            "description": description
        }

        expenses.append(expense)
        save_expenses(expenses)

        print("\nExpense added successfully!")

    except ValueError:
        print("\nPlease enter a valid amount.")


def view_expenses(expenses):
    if len(expenses) == 0:
        print("\nNo expenses found.")
        return

    print("\n========== ALL EXPENSES ==========")

    for index, expense in enumerate(expenses, start=1):
        print(
            index,
            "| Amount:", expense["amount"],
            "| Category:", expense["category"],
            "| Description:", expense["description"]
        )

    print("==================================")


def show_total(expenses):
    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    print("\nTotal Expense:", total)


def category_summary(expenses):
    if len(expenses) == 0:
        print("\nNo expenses found.")
        return

    summary = {}

    for expense in expenses:
        category = expense["category"].lower()
        amount = expense["amount"]

        if category in summary:
            summary[category] = summary[category] + amount
        else:
            summary[category] = amount

    print("\n======= CATEGORY SUMMARY =======")

    for category in summary:
        print(category.title(), ":", summary[category])

    print("===============================")


def delete_expense(expenses):
    if len(expenses) == 0:
        print("\nNo expenses to delete.")
        return

    view_expenses(expenses)

    try:
        number = int(input("\nEnter expense number to delete: "))

        if number >= 1 and number <= len(expenses):
            expenses.pop(number - 1)
            save_expenses(expenses)
            print("\nExpense deleted successfully!")
        else:
            print("\nInvalid expense number.")

    except ValueError:
        print("\nPlease enter a valid number.")


def main():

    expenses = load_expenses()

    print("===================================")
    print("       PERSONAL EXPENSE TRACKER")
    print("===================================")

    name = input("Enter your name: ")

    print("\nWelcome", name)

    while True:

        print("\n========== MAIN MENU ==========")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Show Total Expense")
        print("4. Category Summary")
        print("5. Delete Expense")
        print("6. Exit")
        print("===============================")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            show_total(expenses)

        elif choice == "4":
            category_summary(expenses)

        elif choice == "5":
            delete_expense(expenses)

        elif choice == "6":
            print("\nThank you for using Expense Tracker!")
            break

        else:
            print("\nInvalid choice. Please enter 1 to 6.")


if __name__ == "__main__":
    main()