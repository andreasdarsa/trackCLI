import json
import os

DATA_FILE = os.environ.get("TASKS_FILE", "data/tasks.json")


def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_tasks(tasks):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def add_task(task_text):
    task_data = {
        "task": task_text,
        "done": False
    }
    tasks = load_tasks()
    tasks.append(task_data)
    save_tasks(tasks)


def list_tasks():
    return load_tasks()


def delete_task(idx):
    tasks = load_tasks()
    if 0 <= idx < len(tasks):
        removed = tasks.pop(idx)
        save_tasks(tasks)
        return removed
    return None


def mark_done(idx):
    tasks = load_tasks()
    if 0 <= idx < len(tasks):
        tasks[idx]["done"] = True
        save_tasks(tasks)
        return tasks[idx]
    return None


def clear_all():
    save_tasks([])


def edit_task(idx, text):
    tasks = load_tasks()
    if 0 <= idx < len(tasks):
        tasks[idx]["task"] = text
        save_tasks(tasks)
        return tasks[idx]
    return None


def search_task(text):
    tasks = load_tasks()
    results = []

    for idx, t in enumerate(tasks):
        if text.lower() in t["task"].lower():
            results.append((idx, t))

    return results