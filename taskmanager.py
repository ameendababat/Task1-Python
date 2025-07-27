from task import Task
from filestorage import FileStorage


class TaskManager:
    """Manages tasks using a storage backend (abstraction)."""
    
    def __init__(self, storage:FileStorage):
        self.storage = storage
        self.tasks = self.storage.load()
    
    
    def add_task(self, title, description, priority):
        """Adds a new task."""
        self.tasks.append(Task(title, description, priority))
    
    
    def view_tasks(self, done=False):
        """Displays tasks."""
        if not done:
            new_tasks = self.tasks
        else:
            for t in self.tasks:
                if done:
                    new_tasks = t
        for i, task in enumerate(new_tasks, 1):
            print(f"\n {i}. {task} \n")


    def sort_tasks(self):
        """Returns tasks sorted by priority."""
        return  sorted(self.tasks, key=lambda x : x.priority)


    def mark_done(self, index):
        """Marks a task at a given index as done."""
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_done()
            print("\n Task marked Done")
        else:
            print("invalid task Number")   


    def change_priority(self, index, new_priority):
        """Updates the priority of a task."""
        if not self.tasks:
            print("No tasks to change priority")
        if 0 <= index < len(self.tasks):
            self.tasks[index].update_priority(new_priority)
        else:
            print("Invalid task Number")


    def delete_task(self, index):
        """"Deletes a task at a given index."""
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            print("task Deleted")
        else:
            print("Invalid task Number")


    def save_task(self):
        """Saves all tasks using the storage backend."""
        self.storage.save(self.tasks)

