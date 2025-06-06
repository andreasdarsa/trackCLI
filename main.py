import click
from todo import add_task, list_tasks, delete_task, mark_done, clear_all, edit_task, search_task
import datetime


@click.group()
def cli():
    pass


@cli.command()
@click.argument("task")
def add(task):
    add_task(task)
    click.echo(f"{task} added to tasks.")


@cli.command()
def list():
    tasks = list_tasks()
    if not tasks:
        click.echo("No tasks found")
    else:
        for idx, t in enumerate(tasks, 1):
            status = "[x]" if t["done"] else "[ ]"
            click.echo(f"{idx}. {status} {t["task"]}")


@cli.command()
@click.argument("index", type=int)
def delete(index):
    removed = delete_task(index-1)
    if not removed:
        click.echo("Task not found")
    else:
        click.echo(f"{removed["task"]} removed from tasks.")


@cli.command()
@click.argument("index", type=int)
def done(index):
    marked = mark_done(index-1)
    if marked:
        click.echo(f"Marked as done: {marked["task"]}")
    else:
        click.echo("Task not found")


@cli.command()
def clear():
    confirm = click.confirm("Are you sure?", default=False)
    if confirm:
        clear_all()
        click.echo("All tasks deleted.")
    else:
        click.echo("Deletion cancelled.")


@cli.command()
@click.argument("index", type=int)
@click.argument("new_text")
def edit(index, new_text):
    edited = edit_task(index-1, new_text)
    if edited:
        click.echo(f"Task edited successfully. New task: {edited["task"]}")
    else:
        click.echo("Task not found")


@cli.command()
@click.argument("query")
def search(query):
    results = search_task(query)
    if not results:
        click.echo("No results")
        return

    for idx, t in results:
        status = "[x]" if t["done"] else "[ ]"
        click.echo(f"{idx+1}. {status} {t["task"]}")


@cli.command()
def help():
    print("----------------")
    print("CLI productivity app\n")
    print("Commands supported (just todo app for now):")
    print("1. add: Add a task (use double quotes)")
    print("2. list: List all tasks")
    print("3. clear: Delete all tasks")
    print("4. edit: Edit the content of a task (provide the number of the task as listed")
    print("and the new content of it)")
    print("5. delete: Delete a task (provide the number of the task as listed)")
    print("6. done: Mark a task as done (provide the number of the task as listed)")
    print("7. search: Search a task (use double quotes)")
    print("8. help: Get help for all commands\n")
    print("----------------")


if __name__ == "__main__":
    cli()
