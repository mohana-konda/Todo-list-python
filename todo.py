tasks=[]

while True:
  print("1. Add task")
  print("2. View tasks")
  print("3. Delete task")
  print("4. Exit")

  choice=input("Enter your choice: ")
  if choice == '1':
    task=input("Enter your task: ")
    tasks.append(task)
    print("Task added successfully!")
  elif choice == '2':
    if not tasks:
      print("No tasks are available")
    else:
      for i in range(len(tasks)):
        print(f"{i+1}. {tasks[i]}")
  elif choice == '3':
    if not tasks:
      print("No tasks to delete")
    else:
      for i in range(len(tasks)):
        print(f"{i+1}. {tasks[i]}")
      task_num=int(input("Enter the task number to delete:"))
      deleted_task=tasks[task_num-1]
      tasks.pop(task_num-1)
      print(f"Task '{deleted_task}' deleted successfully!")
  elif choice == '4':
    print("Exiting... Goodbye!")
    break
  else:
    print("Invalid choice! Please try again." )
        