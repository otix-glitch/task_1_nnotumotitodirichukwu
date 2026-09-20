# To-Do List

A simple command-line Python application for managing tasks during a session.

## Features

- View all tasks and their completion status.
- Add new tasks.
- Mark tasks as completed.
- Delete tasks.
- Validates task numbers and menu choices.
- Prevents empty tasks from being added.

## Requirements

- Python 3.6 or newer

No external packages are required.

## Usage

From the project directory, run:

```bash
python skills/to-do-list.py
```

The program displays a menu:

```text
=== To-Do List ===
1. View tasks
2. Add a task
3. Complete a task
4. Delete a task
5. Exit
Choose an option:
```

Enter a menu number to perform an action. Tasks are numbered starting at `1`.

## Example Workflow

1. Choose `2` and enter a task such as `Study Python`.
2. Choose `1` to view the task list.
3. Choose `3`, then enter the task number to mark it as completed.
4. Choose `4`, then enter the task number to delete it.
5. Choose `5` to exit the program.

Completed tasks are displayed with an `x`:

```text
To-do list:
1. [x] Study Python
2. [ ] Read a book
```

## Data Storage

Tasks are stored in memory while the program is running. They are not saved to a file or database, so the list is empty the next time the program starts.
