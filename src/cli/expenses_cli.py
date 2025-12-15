"""
CLI commands for managing expenses.
"""
import click
from backend.expenses import add_expense, list_expenses, delete_expense, clear_expenses, edit_expense, search_expenses, total_expenses, expenses_by_category, average_expense, highest_expense, lowest_expense

@click.group()
def expenses():
    """Expense management commands."""
    pass

@expenses.command()
@click.argument('category')
@click.argument('amount', type=float)
@click.option('--description', default="", help="Description of the expense")
def add(category, amount, description):
    """Add a new expense."""
    add_expense(category, amount, description)
    click.echo(f"Added expense: {category}, Amount: {amount}, Description: {description}")

@expenses.command(name="list_all")
def list_cmd():
    """List all expenses."""
    expenses = list_expenses()
    if not expenses:
        click.echo("No expenses found")
    else:
        for idx, exp in enumerate(expenses, 1):
            click.echo(f"{idx}. Category: {exp['category']}, Amount: {exp['amount']}, Description: {exp['description']}")

@expenses.command()
@click.argument('index', type=int)
def remove(index):
    """Remove an expense by its index."""
    removed = delete_expense(index-1)
    if not removed:
        click.echo("Expense not found")
    else:
        click.echo(f"Removed expense: Category: {removed['category']}, Amount: {removed['amount']}")

@expenses.command()
def clear():
    """Clear all expenses."""
    confirm = click.confirm("Are you sure?", default=False)
    if confirm:
        clear_expenses()
        click.echo("All expenses deleted.")

@expenses.command()
@click.argument('index', type=int)
@click.option('--category', help="New category")
@click.option('--amount', type=float, help="New amount")
@click.option('--description', help="New description")
def edit(index, category, amount, description):
    """Edit an expense by its index."""
    edited = edit_expense(index-1, category, amount, description)
    if edited:
        click.echo(f"Edited expense: Category: {edited['category']}, Amount: {edited['amount']}, Description: {edited['description']}")
    else:
        click.echo("Expense not found")

@expenses.command()
@click.argument('keyword')
def search(keyword):
    """Search expenses by keyword."""
    results = search_expenses(keyword)
    if not results:
        click.echo("No matching expenses found")
    else:
        for idx, exp in enumerate(results, 1):
            click.echo(f"{idx}. Category: {exp['category']}, Amount: {exp['amount']}, Description: {exp['description']}")

@expenses.command()
def total():
    """Show total expenses."""
    total_amount = total_expenses()
    click.echo(f"Total expenses amount: {total_amount}")

@expenses.command()
def by_category():
    """Show expenses by category."""
    category_totals = expenses_by_category()
    for category, total in category_totals.items():
        click.echo(f"Category: {category}, Total Amount: {total}")

@expenses.command(name="avg")
def average():
    """Show average expense amount."""
    avg = average_expense()
    click.echo(f"Average expense amount: {avg}")

@expenses.command(name="max")
def highest():
    """Show highest expense."""
    highest_exp = highest_expense()
    if highest_exp:
        click.echo(f"Highest expense: Category: {highest_exp['category']}, Amount: {highest_exp['amount']}, Description: {highest_exp['description']}")
    else:
        click.echo("No expenses found")

@expenses.command(name="min")
def lowest():
    """Show lowest expense."""
    lowest_exp = lowest_expense()
    if lowest_exp:
        click.echo(f"Lowest expense: Category: {lowest_exp['category']}, Amount: {lowest_exp['amount']}, Description: {lowest_exp['description']}")
    else:
        click.echo("No expenses found")

@expenses.command(name="help")
def help_expenses():
    """Show help for expense commands."""
    click.echo(expenses.get_help(click.Context(expenses)))

