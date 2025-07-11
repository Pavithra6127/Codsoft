
# TASK-1-To-Do List

todo_list = []
def show_menu():
    print("\nTo-Do List Menu:")
    print("1.Add Task")
    print("2.View Tasks")
    print("3.Mark Task as Done")
    print("4.Exit")

while True:
    show_menu()
    choice = input("Enter Your Choice (1 - 4): ")

    if choice == "1":
        task = input("Enter The Task: ")
        todo_list.append({"Task": task, "Done": False})
        print("Task added!!")
    
    elif choice == "2":
        print("\nYour To-Do List:")
        for i, item in enumerate(todo_list):
            status = "✅" if item["Done"] else "❌"
            print(f"{i+1}. {item['Task']} [{status}]")
    
    elif choice == "3":
        task_num = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= task_num < len(todo_list):
            todo_list[task_num]["Done"] = True
            print("Task marked as done!")
        else:
            print("Invalid task number.")
    
    elif choice == "4":
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice. Please Enter (1-4).")



