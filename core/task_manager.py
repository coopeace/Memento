# from core.task import select_task

from .model import Task
from datetime import datetime
import json
from services import utils
from pathlib import Path

class TaskManager:
    def __init__(self,file_name:str) -> None:
        self.FILE_NAME = Path(file_name)
        self.tasks : dict[int,Task] = {}
        self.task_counter : int = 0 

    def add_task(self,title:str) -> str:
        self.task_counter += 1
        self.tasks[self.task_counter] = Task(task_id = self.task_counter,title = title)

        return f"Task '{title}' added successfully."

    def view_tasks(self) -> None:
        if not len(self.tasks) == 0: 
            for task in self.tasks.values():
                print(f"{task.task_id}. {task.title} [{task.status.value}]")
        else :
            print("[Database is empty]")

    def remove_task(self,id:int) -> str :
        try :
            task = task_manager.tasks.pop(id)
            task_manager.task_counter -= 1
            for key,value in task_manager.tasks.items():
                if key > id :
                    key -= 1
                    value.task_id -= 1

            return f"'{task.title}' is removed."
        except KeyError as err:
            return f"{err}"

    def modify_task(self,id:int,new_title:str) -> str:
        task = self.tasks[id]
        previous_title = task.title
        task.title = new_title
        task.last_updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"'[green]{previous_title}[/]'\n title is modified to\n'{task.title}'\n at '{task.last_updated}'."

    def empty_database(self) -> None:
        self.tasks = {}
        self.task_counter = 0

    def save_to_json(self) -> str:
        save_data = [ task.to_dict() for task in self.tasks.values() ]

        with open(self.FILE_NAME,"w") as writefile:
            json.dump(save_data,writefile,indent=4)

        return f"Tasks successfully saved to {self.FILE_NAME}"

    def load_from_json(self):
        data = []

        if not self.FILE_NAME.exists():
            return

        try :
            with open(self.FILE_NAME,"r") as read_file:
                data = json.load(read_file)
            n = len(data)
            if not n == 0 :
                for item in data:
                    task =  Task.from_dict(item)
                    # task = Task(**item)
                    self.tasks[task.task_id] = task
            self.task_counter = n

        except json.JSONDecodeError as err: 
            print(f"{err}")

task_manager = TaskManager(file_name="save.json")
