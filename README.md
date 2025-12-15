# trackCLI

A command-line tool that helps users organize their every day tasks

## Provides
- Organizes tasks **to-do**
- Keeps track of user's daily **expenses**

## Usage
- Runs on the command line
- Type **python main.py todo help** (or py main.py todo help) in order to get a basic overview on how to use the commands available on the to-do helper.
- Type **python main.py expenses help** (or py main.py expenses help) in order to get a basic overview on how to use the commands available on the expenses tracker.

## To-do organizer: A cheat sheet
- **python main.py todo add "Task to add"**: adds a task with text content "Task to add" to your to-do list
- **python main.py todo list_all**: shows all the tasks in your to-do list
- **python main.py todo clear**: deletes all the tasks from your to-do list (requires confirmation from the user)
- **python main.py todo edit index "New text content"**: edits the text content of the task corresponding to the index provided (ex. python main.py edit 3 "Go shopping" sets the text content of task no.3 to "Go shopping")
- **python main.py todo delete index**: deletes the task corresponding to the index provided (ex. python main.py delete 2 deletes the task no.2)
- **python main.py todo done index**: marks the task corresponding to the index provided as done (ex. python main.py done 4 marks task no.4 as done)
- **python main.py todo search "Search content"**: searches for tasks whose text contains "Search content"
- **python main.py todo help**: lists all available commands
