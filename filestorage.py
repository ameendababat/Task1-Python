from task import Task
from interfaces import StorageInterface
import json
import os


class FileStorage(StorageInterface):
    """File-based storage for saving and loading tasks in JSON format."""
    
    
    def __init__(self, tasks_file="tasks.json"):
        
        self.tasks_file=tasks_file
    
    
    def save(self, tasks):
        """Saves a list of tasks to the JSON file."""
        with open(self.tasks_file, "w") as f:
            json.dump([task.__dict__ for task in tasks], f, indent=2)


    def load(self):
        """Loads tasks from the JSON file."""
        if os.path.exists(self.tasks_file):
            with open(self.tasks_file, "r") as f:
                try:
                    data = json.load(f)
                    return [Task(**task) for task in data]
                except json.JSONDecodeError:
                    print("load JSON Error! returning empty list " )
                    return []
        else:
            print("file dose not exists")
            return []
            