# todo.py

tasks = []

# load tasks from file
try:
    file = open("tasks.txt", "r")
    for line in file:
        tasks.append(line.strip())
    file.close()
except:
    pass   # if file not found, ignore


while True:
    print("\n--- TO DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    # ADD TASK
    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)

        file = open("tasks.txt", "w")
        for t in tasks:
            file.write(t + "\n")
        file.close()

        print("Task added!")

    # VIEW TASKS
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks found.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i+1, "-", tasks[i])

    # REMOVE TASK
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            for i in range(len(tasks)):
                print(i+1, "-", tasks[i])

            num = int(input("Enter task number to remove: "))
            tasks.pop(num-1)

            file = open("tasks.txt", "w")
            for t in tasks:
                file.write(t + "\n")
            file.close()

            print("Task removed!")

    # EXIT
    elif choice == "4":
        print("Bye Bye 👋")
        break

    else:
        print("Invalid choice!")
