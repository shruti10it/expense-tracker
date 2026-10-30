import streamlit as st

st.set_page_config(
    page_title="Expense Tracker",
    page_icon="💰",
    layout="wide"
)
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

st.title("💰 Expense Tracker Dashboard")

st.subheader("Add New Expense")

with st.form("expense_form"):
    amount = st.number_input("Amount", min_value=0.0, step=10.0)
    category = st.selectbox(
        "Category",
        ["Food", "Travel", "Shopping", "Bills", "Other"]
    )
    description = st.text_input("Description")

    add_button = st.form_submit_button("Add Expense")

expenses = load_expenses()
if add_button:
    if amount > 0:
        expenses.append({
            "amount": amount,
            "category": category,
            "description": description
        })

        with open(FILE_NAME, "w") as file:
            json.dump(expenses, file, indent=4)

        st.success("Expense added successfully!")
        st.rerun()
    else:
        st.warning("Please enter an amount greater than 0.")

total = sum(expense["amount"] for expense in expenses)
total = round(total,2)

st.subheader("Expense Summary")

col1, col2 = st.columns(2)

col1.metric("Total Expense", f"₹{total:.2f}")
col2.metric("Total Entries", len(expenses))

st.subheader("All Expenses")

if expenses:
    st.dataframe(expenses, use_container_width=True)
else:
    st.info("No expenses found.")
    
st.subheader("Category-wise Expenses")

category_totals = {}

for expense in expenses:
    category = expense["category"]
    amount = expense["amount"]

    if category in category_totals:
        category_totals[category] += amount
    else:
        category_totals[category] = amount

if category_totals:
    st.bar_chart(category_totals)
    st.subheader("Manage Expenses")

if expenses:
    expense_options = [
        f"{index + 1}. ₹{float(expense['amount']):.2f} | "
        f"{expense['category']} | {expense['description']}"
        for index, expense in enumerate(expenses)
    ]

    selected_expense = st.selectbox(
        "Select expense to delete",
        expense_options
    )

    selected_index = expense_options.index(selected_expense)

    delete_col, clear_col = st.columns(2)

    if delete_col.button("Delete Selected Expense"):
        expenses.pop(selected_index)

        with open(FILE_NAME, "w") as file:
            json.dump(expenses, file, indent=4)

        st.success("Selected expense deleted successfully!")
        st.rerun()

    if clear_col.button("Clear All Expenses"):
        with open(FILE_NAME, "w") as file:
            json.dump([], file, indent=4)

        st.success("All expenses cleared successfully!")
        st.rerun()
    