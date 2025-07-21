import json
import os


tasks_file = "tasks.json"
tasks = []

def load_tasks():
    """ load task from file"""
    if os.path.exists(tasks_file):
        with open(tasks_file,'r') as f:
            tasks = json.load(f)
            # print(tasks)
            return tasks

def add_task():
    """ add new task to   TO DO list """
    global tasks
    # task = input("Enter your task:")
    # tasks.append(task)
    # print("task added successfully")
    
    title = input("Enter your task title")
    description = input("Enter your task description")
    
    while True:
        
        try:
            priority = int(input("Enter your Task priority (0-5):"))
            if 0 <= priority <= 5:
                break
            else:
                print("priority must be between 1 and 5")
        except ValueError:
            print("invalid number! Try again")
            
    task = {
        "title":title,
        "description":description,
        "priority":priority,
        "done":False
    }
                
    tasks.append(task)
    

def view_tasks(tasks):
    
    """ view all tasks in TO Do List """
    
    if not tasks:
        print("No task to show")
        return
    print("\n Tasks:")
    i= 0
    while i < len(tasks):
        task =tasks[i]
        if task["done"]:
            status = "Done"
        else:
            status = "Not Done" 
        print(f"{i+1}. [{status}] {task["title"]} (priority: {task["priority"]}) \n {task["description"]}") 
        i+=1


def sort_tasks(tasks):
    
    """ sorted tasks by priority"""
    
    if not tasks:
        print("not Tasks to sort")
        return
    k = lambda x : x["priority"]
    sorted_tasks = sorted(tasks,k)
    print("\n sorted tasks by priority:")
    i = 0
    while i < len(sorted_tasks):
        task = sort_tasks[i]
        if task["done"]:
            status = "Done"
        else:
            status = "Not Done"
        print(f"{i+1}. [{status}] {task["title"]} (priority: {task["priority"]}) \n {task["description"]}")
        i+=1        
    
    
    
    
def mark_done():
    
    global tasks
    view_tasks(tasks)
    
    if (not tasks):
        print("No task to mark Done")
        return
    try:
        task_num = int(input("Enter task number to mark Done"))-1
        if 0 <= task_num < len(tasks):
            tasks[task_num]["done"] = True
            print("Task marked Done")
        else:
            print("invalid task Number")    
        
    except ValueError:
        print("invalid number Try again")    
    
    
    
    

def change_priority():
    """ Change task by priority""" 
    global tasks  
    view_tasks(tasks)
    if (not tasks):
        print("No tasks to change priority")
        return
    try:
        task_num = int(input("Enter task Number to change priority"))-1
        if 0 <= task_num < len(tasks):
            new_priority = int(input("Enter priority Number [0 to 5]"))
            if 0 <= new_priority <= 5:
                tasks[task_num]["priority"]= new_priority
            else:
                print("Invalid new priority")
        else:
            print("Invalid task Number")            
    except ValueError:
        print("invalid number Try again")

def delete_task():
    global tasks
    view_tasks()
    if (not tasks):
        print("No task to Delete")
        return
    
    try:
        task_number = int(input("Enter task Number To Deleted"))-1
        if 0 <=task_number < len(tasks):
            tasks.pop(task_number)
            print("task Deleted")
        else:
            print("Invalid task Number")
    except ValueError:
        print("invalid number Try again")
        
        
    
    
    
    
def close_program():
    print("Goodbye!")
    exit()
    
    
    
    
    
    
def save_task(tasks):
    """ save task in file tasks.json """ 
    
    with open(tasks_file,'w') as f:
        json.dump(tasks,f,indent=2) #json.dump convert python object to json format        
    print("all tasks saved to json file")
        
        

        
def show_menu():
    print("""
        To-Do list menu:
        1. Add task
        2. View Task
        3. sort Task By priority 
        4. mark Task as Done
        5. change Task priority 
        6. Delete Task 
        7. Save 
        8. Exit
        """)    



def main():   
    global tasks
    tasks= load_tasks()
    while True:
        show_menu()
        choice = int(input("Eneter option From menu: [1 - 8]"))
        match choice:
            case 1: add_task()
            case 2: view_tasks(tasks)
            case 3: sort_tasks(tasks)
            case 4: mark_done()
            case 5: change_priority()
            case 6:delete_task()
            case 7:save_task(tasks)
            case 8: close_program()
            case _: print("Invalid option.")
        

if __name__ == "__main__":
    main()    