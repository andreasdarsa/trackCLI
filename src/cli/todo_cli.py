"""
Todo CLI - Command group for todo list operations.

This module contains all commands related to the todo list aspect of the application.
"""

import click
from backend.todo import add_task, list_tasks, delete_task, mark_done, clear_all, edit_task, search_task


@click.group()
def todo():
    """Todo list commands."""
    pass


@todo.command()
@click.argument('task')
def add(task):
    """Add a new task to the todo list."""
    add_task(task)
    click.echo(f"{task} added to tasks.")


@todo.command(name="list_all")
def list_cmd():
    """List all tasks in the todo list."""
    tasks = list_tasks()
    if not tasks:
        click.echo("No tasks found")
    else:
        for idx, t in enumerate(tasks, 1):
            status = "[x]" if t["done"] else "[ ]"
            click.echo(f"{idx}. {status} {t['task']}")


@todo.command()
@click.argument('index', type=int)
def remove(index):
    """Remove a task from the todo list by its index."""
    removed = delete_task(index-1)
    if not removed:
        click.echo("Task not found")
    else:
        click.echo(f"{removed['task']} removed from tasks.")


@todo.command()
@click.argument('index', type=int)
def done(index):
    """Mark a task as done by its index."""
    marked = mark_done(index-1)
    if marked:
        click.echo(f"Marked as done: {marked['task']}")
    else:
        click.echo("Task not found")

@todo.command()
def clear():
    """Clear all tasks from the todo list."""
    confirm = click.confirm("Are you sure?", default=False)
    if confirm:
        clear_all()
        click.echo("All tasks deleted.")
    else:
        click.echo("Deletion cancelled.")

@todo.command()
@click.argument('index', type=int)
@click.argument('text')
def edit(index, text):
    """Edit a task's text by its index."""
    edited = edit_task(index-1, text)
    if edited:
        click.echo(f"Task updated to: {edited['task']}")
    else:
        click.echo("Task not found")

@todo.command()
@click.argument('text')
def search(text):
    """Search for tasks containing the given text."""
    results = search_task(text)
    if not results:
        click.echo("No matching tasks found")
    else:
        for idx, t in results:
            status = "[x]" if t["done"] else "[ ]"
            click.echo(f"{idx + 1}. {status} {t['task']}")

@todo.command(name="help")
def help_todo():
    """Show help for todo commands."""
    click.echo(todo.get_help(click.Context(todo)))


if __name__ == '__main__':
    todo()
