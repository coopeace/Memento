from abc import ABC, abstractmethod
from typing import Any
from InquirerPy import inquirer
from model import Profile,Status,RepeatCycle,Task
from datetime import datetime, time
from .session import current_session
from .task_manager import task_manager
from InquirerPy.base.control import Choice

class Command(ABC):
    @abstractmethod
    def execute(self)->Any:
        pass

class AddTaskCommand(Command):
    def execute(self):
        title = input(" > ")
        print(task_manager.add_task(title))

class ViewTasksCommand(Command):
    def execute(self):
        task_manager.view_tasks()

class ModifyTasksCommand(Command):
    def execute(self):
        pass

class RemoveTaskCommand(Command):
    def execute(self):
        print(task_manager.remove_task(select_task()))

class EmptyDatabaseCommand(Command):
    def execute(self):
        pass

class CommpletedTasksCommand(Command):
    def execute(self):
        pass

class QuitCommand(Command):
    def execute(self):
        current_session.QuitExecutions()

def set_status() -> str:
    return inquirer.select(
            message = "Status",
            choices= [s.name for s in Status]
            ).execute()

def set_repeat_cycle() -> str:
    return inquirer.select(
            message= "RepeatCycle",
            choices= [r.name for r in RepeatCycle]
            ).execute()

def select_task() -> int :
    task_id = inquirer.select(
    message="Which task do you want to remove: ",
    choices=[
        Choice(value=key,name=task.title) 
        for key, task in task_manager.tasks.items()
        ]
    ).execute()
    return task_id
