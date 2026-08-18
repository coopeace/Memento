from abc import ABC, abstractmethod
from random import choice
from typing import Any
from InquirerPy import inquirer
from rich import panel
from .model import Profile,Status,RepeatCycle,Task
from datetime import datetime, time
from services.session import current_session
from .task_manager import task_manager
from InquirerPy.base.control import Choice
from rich import print
from rich.console import Console
from rich.align import Align
from rich.panel import Panel

console = Console()

class Command(ABC):
    @abstractmethod
    def execute(self)->Any:
        pass

class AddTaskCommand(Command):
    def execute(self):
        title = inquirer.text(message="Title >").execute()
        app_dialogs(task_manager.add_task(title))

class ViewTasksCommand(Command):
    def execute(self):
        task_manager.view_tasks()

class ModifyTasksCommand(Command):
    def execute(self):
        selected_id = select_task("modify")
        new_title = inquirer.text(message="Edit >").execute()
        app_dialogs(task_manager.modify_task(selected_id,new_title))

class RemoveTaskCommand(Command):
    def execute(self):
        print(task_manager.remove_task(select_task("remove")))

class EmptyDatabaseCommand(Command):
    def execute(self):
        choice = None
        while not (choice=="yes" or choice=="q"): 
            print("Are you sure want to remove every tasks?")
            print("Type [cyan]'yes'[/cyan] for confirmation or [cyan]'q'[/] to return")
            choice = inquirer.text(message=">").execute()
            if choice == "q" :
                app_dialogs("[blue]Returning to main menu.....[/]")
            elif choice  == "yes" :
                task_manager.empty_database()
                task_manager.view_tasks()
            else :
                app_dialogs("[red]'Warning': Enter a valid option[/]")

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

def select_task(choice:str) -> int :
    task_id = inquirer.select(
    message=f"Which task do you want to {choice}: ",
    choices=[
        Choice(value=key,name=task.title) 
        for key, task in task_manager.tasks.items()
        ]
    ).execute()
    return task_id

def app_dialogs(dialog:str) -> None:
    console.print(
            Align.right(
                Panel.fit(
                    dialog,border_style="cyan"
                    )
                )
            )
