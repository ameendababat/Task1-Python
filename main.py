from filestorage import FileStorage
from taskmanager import TaskManager


def input_priority():
    """Gets a valid priority input from the user."""
    while True:
        try:
                p = int(input("Enter priority: (0 - 5): "))
                if 0 <= p <= 5:
                    return p
                else:
                    print("Priority must be between 0 and 5 ") 
        except ValueError:
            print("Invalid Number")    


def show_menu():

        print("""
        
            ======== To-Do list menu: ========

            1. Add task
            2. View Task
            3. sort Task By priority 
            4. mark Task as Done
            5. change Task priority 
            6. Delete Task 
            7. Save 
            8. Exit

            ====================================
            """) 


def main():
    manager = TaskManager(FileStorage())
    while True:
        show_menu()
        try:
            choice = int(input("Choose: "))
        except ValueError:
            print("Enter a Number! ")
            continue
        match choice:
            case 1:
                t = input("Title: ").strip()
                d = input("Description: ").strip()
                p = input_priority()
                manager.add_task(t,d,p)
                print("added task successfully ")
            case 2:
                manager.view_tasks()
            case 3:
                sorted_tasks = manager.sort_tasks()
                for i, task in enumerate(sorted_tasks,1):
                    print(f"\n {i}. {task} \n")
            case 4:
                manager.view_tasks()
                i = int(input("Which task? "))-1
                manager.mark_done(i)
            case 5:
                manager.view_tasks()
                i = int(input("Which task? "))-1
                new_p = input_priority()
                manager.change_priority(i, new_p)
            case 6:
                manager.view_tasks()
                i = int(input("Which task? "))-1
                manager.delete_task(i)
            case 7:
                manager.save_task()
            case 8:
                manager.save_task()
                print("Goodbye! ")
                break
            case _:
                print("Invalid choice ")

if __name__ == "__main__":
    main()