tasks = []


def show_tasks():
	if not tasks:
		print("\nYour to-do list is empty.")
		return

	print("\nTo-do list:")
	for number, task in enumerate(tasks, start=1):
		status = "x" if task["done"] else " "
		print(f"{number}. [{status}] {task['text']}")


def choose_task(action):
	if not tasks:
		print("\nThere are no tasks to choose from.")
		return None

	show_tasks()
	try:
		number = int(input(f"\nEnter the task number to {action}: "))
	except ValueError:
		print("Please enter a whole number.")
		return None

	if number < 1 or number > len(tasks):
		print("That task number does not exist.")
		return None

	return number - 1


def add_task():
	text = input("\nEnter a task: ").strip()
	if not text:
		print("A task cannot be empty.")
		return

	tasks.append({"text": text, "done": False})
	print("Task added.")


def complete_task():
	index = choose_task("complete")
	if index is None:
		return

	tasks[index]["done"] = True
	print("Task completed.")


def delete_task():
	index = choose_task("delete")
	if index is None:
		return

	deleted_task = tasks.pop(index)
	print(f"Deleted: {deleted_task['text']}")


def main():
	while True:
		print("\n=== To-Do List ===")
		print("1. View tasks")
		print("2. Add a task")
		print("3. Complete a task")
		print("4. Delete a task")
		print("5. Exit")

		choice = input("Choose an option: ").strip()

		if choice == "1":
			show_tasks()
		elif choice == "2":
			add_task()
		elif choice == "3":
			complete_task()
		elif choice == "4":
			delete_task()
		elif choice == "5":
			print("Goodbye!")
			break
		else:
			print("Please choose a number from 1 to 5.")


if __name__ == "__main__":
	main()
