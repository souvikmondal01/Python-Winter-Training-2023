import json
from datetime import date

emptyDoc = False
task_count =0

while True:
    with open("todoDB.json","r") as f:
        # reading the todoDB
        todoData = json.load(f)

    keys = list(todoData.keys())    
    currentDate = date.today()

    #checking whether the user is a new user or not
    if len(todoData) == 0:
        emptyDoc = True
        username = input(
            "Hi there! Welcome to TodoCLI, Please enter your name:"
        )
        todoData["name"] = username
        todoData["date"] = str(currentDate)
        print(f"Hey {username}! I hope you had a good start of the day,\nYou can create your task by typing create task or add task")

        cmd = input(">>")

        todoData["today"] = []

        if cmd == "create task" or cmd == "add task":
            print("\nPlease provide details about your task:")
            print("Add time in miitary format:")

            #take the task description as input
            task_description = input("\nPlease enter your task description: ")
            scheduled_time = input("Please enter scheduled time: ")

            task = {
                "taskId": task_count,
                "description": task_description,
                "scheduled_time": scheduled_time,
                "status":"TBD"
            }
            todoData["today"].append(task)
            with open("todoDB.json","w") as f:
                json.dump(todoData,f,indent=4)

        elif cmd == "break" or cmd == "close":
            break

    elif "today" in list(todoData.keys()):
        tasks = todoData["today"]
        username = todoData["name"]
        print(f"\nToday is {currentDate}")
        #show the user all the existing tasks
        print(f"\nHey {username}, here are the tasks for your day")
        for task in tasks:
            print(f"\nTask {tasks.index(task)+1}")
            print("\nTask description:",task["description"])
            print("\nScheduled time:",task["scheduled_time"])

        print("\n add more tasks for the day")
        cmd = input(">>")

        if cmd == "create task" or cmd == "add task":
            task_description = input("\nEnter your description:")
            scheduled_time = input("\nEnter your scheduled time:")

            task = {
                "taskId": task_count,
                "description": task_description,
                "scheduled_time": scheduled_time,
                "status":"TBD"
            }    

            todoData["today"].append(task)
            with open("todoDB.json","r+") as f:
                f.seek(0)
                json.dump(todoData,f,indent=4)

            print("\nTask created successfully")
            print("\nType <create task> or <add task> to add more tasks")
            print("\ntype <done> or <exit> to exit from the add")
            continue

        # elif cmd == "Delete user":
        #     todoData["today"] == []
            
        #     with open("todoDB.json","w") as f:
        #         f.seek(0)
        #         json.dump(todoData,f,indent=4)
        #     print("\nUser deleted successfully")
        #     continue
        # elif cmd == "clear tasks":
        #     todoData["today"] = []

        #     with open("todoDB.json","w") as f:
        #         json.dump(todoData,f,indent=4)
        #     print("\nTasks deleted successfully")
        #     continue
        # elif cmd == "change status":
        #     taskId = input("Enter task id:")
        #     tasks = todoData["today"]
        #     for task in tasks:
        #         if taskId == tasks.index(task):
        #             tasks.remove(task)
        #             break
        #     continue                      

        # elif cmd == "done" or cmd == "exit":
        #     break

        if cmd=="delete user":
            with open("todoDB.json","w") as f:
                json.dump({},f,indent=4)
            print("all data deleted successfully!!!")
        if cmd=='done' or cmd=='exit':
            print('have a great day')
            exit()
        if cmd=="delete task":
            if  "today" in list(todoData.keys()):
                todoData['today']=[]
                todoData['name']=username
                todoData['date']=str(currentDate)
                with open("todoDB.json","w") as f:
                    json.dump(todoData,f,indent=4)

            
        if cmd == "mark task as done":
            tasks = todoData["today"]
            username = todoData["name"]
            print(f"\nToday is {currentDate}")
            #show the auer all the existing tasks
            print(f"\nTask {tasks.index(task)+1}")
            print("\nTask description:",task["description"])
            print("\nScheduled time:",task["scheduled_time"])
            print("\nStatus:",task["status"])


        task_id = int(input("\nEnter task id:"))

        for task in tasks:
            if task["taskId"] == task_id:
                todoData["today"][tasks.index(task)]["status"] = "DONE"
            else:
                continue

        with open("todoDB.json","r+") as f:
            json.dump(todoData,f,indent=4)
        continue                 
    
