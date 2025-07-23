

class Task:
    """Represents a task with a title, description, priority, and status."""

    def __init__(self, title, description, priority, done=False):
        self.title=title
        self.description=description
        self.priority=priority
        self.done=done
    
        
    def mark_done(self):
        """Marks the task as done"""
        self.done=True
    
    
    def update_priority(self, new_priority):
        """Updates the task's priority."""
        self.priority=new_priority
    
    
    def __str__(self):
        """Returns a string representation of the task."""
        status = "Done" if self.done else "Not Done"
        return f"status: [{status}] \n   title:  {self.title} \n   priority: {self.priority} \n   description:  {self.description}"
