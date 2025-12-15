import click


@click.group()
def cli():
    """Main CLI router for trackCLI productivity app"""
    pass


@cli.group()
def todo():
    """Todo list commands."""
    pass


# Import todo commands after group definition to avoid circular imports
from cli.todo_cli import add, list_cmd, remove, done, clear, edit, search, help_todo

todo.add_command(add)
todo.add_command(list_cmd, name="list_all")
todo.add_command(remove)
todo.add_command(done)
todo.add_command(clear)
todo.add_command(edit)
todo.add_command(search)
todo.add_command(help_todo, name="help")


@cli.group()
def expenses():
    """Expense management commands."""
    pass

# Import expenses commands after group definition to avoid circular imports
from cli.expenses_cli import add, list_cmd, remove, clear, edit, search, total, by_category, average, highest, lowest, help_expenses

expenses.add_command(add)
expenses.add_command(list_cmd, name="list_all")
expenses.add_command(remove)
expenses.add_command(clear)
expenses.add_command(edit)
expenses.add_command(search)
expenses.add_command(total)
expenses.add_command(by_category, name="by_category")
expenses.add_command(average, name="avg")
expenses.add_command(highest, name="max")
expenses.add_command(lowest, name="min")
expenses.add_command(help_expenses, name="help")


if __name__ == "__main__":
    cli()
