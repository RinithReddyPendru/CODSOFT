class TodoList:
    def __init__(self):
        self.tasks = []

    def add_a_task(self, task):
        self.tasks.append({'task': task, 'completed': False})  # adds a task with incomplete status

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the To-do list.")
        else:
            for idx, task in enumerate(self.tasks, start=1):
                status = "✓" if task['completed'] else "✗"
                print(f"{idx}. {task['task']} [{status}]")  # prints the status of the tasks in the list

    def complete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]['completed'] = True
        else:
            print("Invalid task number.")

    def remove_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            del self.tasks[task_number - 1]  # deletes the task from the tasks list
        else:
            print("Invalid task number.")

if __name__ == "__main__":
    todo_list = TodoList()

    while True:
        print("\nTo-Do List:")
        todo_list.view_tasks()

        print("\nOptions:")
        print("1. Add task")
        print("2. Complete task")
        print("3. Remove task")
        print("4. Quit")

        choice = input("Choose an option to perform: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_a_task(task)
        elif choice == '2':
            task_number = int(input("Enter the task number to mark as complete: "))
            todo_list.complete_task(task_number)
        elif choice == '3':
            task_number = int(input("Enter the task number to remove: "))
            todo_list.remove_
