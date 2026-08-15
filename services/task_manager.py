from model import Task
from datetime import datetime
import json
from services import utils

class TaskManager:
    def __init__(self,file_name:str) -> None:
        self.file_name = file_name
        self.tasks : dict[int,Task] = {}
        self.task_counter : int = 0 

    def add_task(self,title:str) -> str:
        self.task_counter += 1
        self.tasks[self.task_counter] = Task(task_id = self.task_counter,title = title)

        return f"Task '{title}' added successfully."

    def view_tasks(self) -> None:
        for task in self.tasks.values():
             print(f"{task.task_id}. {task.title} [{task.status.value}]")

    def save_to_json(self) -> str:
        save_data = [ task.to_dict() for task in self.tasks.values() ]

        with open(self.file_name,"w") as writefile:
            json.dump(save_data,writefile,indent=4)

        return f"Tasks successfully saved to {self.file_name}"

    def load_from_json(self):
        data = []
        with open(self.file_name,"r") as readfile:
            data = json.load(readfile)
        n = len(data)
        if not n == 0 :
            for item in data:
                task =  Task.from_dict(item)
                # task = Task(**item)
                self.tasks[task.task_id] = task
        self.task_counter = n

task_manager = TaskManager(file_name="save.json")
