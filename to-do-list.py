
tasks = []

while True:
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(i, task)

    elif choice == "3":
        for i, task in enumerate(tasks, start=1):
            print(i, task)

        if tasks:
            try:
                num = int(input("Enter task number to remove: "))
                if 1 <= num <= len(tasks):
                    tasks.pop(num - 1)
                    print("Task removed successfully!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
