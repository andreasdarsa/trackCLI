# CLI Productivity Helper

A command-line tool that helps users organize their every day tasks

## Provides
- Organizes tasks **to-do**
(More features to be added soon)

## Usage
- Runs on the command line
- Type **python main.py help** (or py main.py help) in order to get a basic overview on how to use the commands available.

## To-do organizer: A cheat sheet
- **python main.py add "Task to add"**: adds a task with text content "Task to add" to your to-do list
- **python main.py list**: shows all the tasks in your to-do list
- **python main.py clear**: deletes all the tasks from your to-do list (requires confirmation from the user)
- **python main.py edit index "New text content"**: edits the text content of the task corresponding to the index provided (ex. python main.py edit 3 "Go shopping" sets the text content of task no.3 to "Go shopping")
- **python main.py delete index**: deletes the task corresponding to the index provided (ex. python main.py delete 2 deletes the task no.2)
- **python main.py done index**: marks the task corresponding to the index provided as done (ex. python main.py done 4 marks task no.4 as done)
- **python main.py search "Search content"**: searches for tasks whose text contains "Search content"
- **python main.py help**: lists all available commands
