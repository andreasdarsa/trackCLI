"""
CLI commands for managing expenses.
"""
import json
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent
DEFAULT_FILES_DIR = BASE_DIR.parent.parent/ "src" / "data" / "expenses.json"
DATA_FILE = os.environ.get("EXPENSES_FILE", str(DEFAULT_FILES_DIR))

def load_expenses():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)
    
def save_expenses(expenses):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=2)

def add_expense(category, amount, description=""):
    expense_data = {
        "category": category,
        "amount": amount,
        "description": description
    }
    expenses = load_expenses()
    expenses.append(expense_data)
    save_expenses(expenses)

def list_expenses():
    return load_expenses()

def delete_expense(idx):
    expenses = load_expenses()
    if 0 <= idx < len(expenses):
        removed = expenses.pop(idx)
        save_expenses(expenses)
        return removed
    return None

def clear_expenses():
    save_expenses([])

def search_expenses(keyword):
    expenses = load_expenses()
    return [exp for exp in expenses if keyword.lower() in exp["category"].lower() or keyword.lower() in exp["description"].lower()]

def edit_expense(idx, category=None, amount=None, description=None):
    expenses = load_expenses()
    if 0 <= idx < len(expenses):
        if category is not None:
            expenses[idx]["category"] = category
        if amount is not None:
            expenses[idx]["amount"] = amount
        if description is not None:
            expenses[idx]["description"] = description
        save_expenses(expenses)
        return expenses[idx]
    return None

def total_expenses():
    expenses = load_expenses()
    return sum(exp["amount"] for exp in expenses)

def expenses_by_category():
    expenses = load_expenses()
    category_totals = {}
    for exp in expenses:
        category = exp["category"]
        category_totals[category] = category_totals.get(category, 0) + exp["amount"]
    return category_totals

def average_expense():
    expenses = load_expenses()
    if not expenses:
        return 0
    total = sum(exp["amount"] for exp in expenses)
    return total / len(expenses)

def highest_expense():
    expenses = load_expenses()
    if not expenses:
        return None
    return max(expenses, key=lambda exp: exp["amount"])

def lowest_expense():
    expenses = load_expenses()
    if not expenses:
        return None
    return min(expenses, key=lambda exp: exp["amount"])

def expense_stats():
    expenses = load_expenses()
    if not expenses:
        return {
            "total": 0,
            "average": 0,
            "highest": None,
            "lowest": None
        }
    total = sum(exp["amount"] for exp in expenses)
    average = total / len(expenses)
    highest = max(expenses, key=lambda exp: exp["amount"])
    lowest = min(expenses, key=lambda exp: exp["amount"])
    return {
        "total": total,
        "average": average,
        "highest": highest,
        "lowest": lowest
    }