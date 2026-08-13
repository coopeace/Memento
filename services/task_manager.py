from model import Task
from datetime import datetime
import json

class TaskManager:
    def __init__(self) -> None:
        self.task_counter = 0
        self.tasks = {}

    def add_task(self,title:str) -> str:
        self.task_counter += 1
        self.tasks[self.task_counter] = Task(task_id = self.task_counter,title = title)

        return f"Task '{title}' added successfully."

    def view_tasks(self) -> None:
        for task in self.tasks.values():
             print(f"{task.task_id}. {task.title} [{task.status.value}]")

    def quit_manager(self) -> str:
        save_data = [ task.to_dict() for task in self.tasks.values() ]

        filename = "save.json"
        with open(filename,"w") as writefile:
            json.dump(save_data,writefile,indent=4)

        return f"Tasks successfully saved to {filename}"


taskManager  = TaskManager()
