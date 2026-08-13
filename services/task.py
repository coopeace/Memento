from InquirerPy import inquirer
from model import Profile,Status,RepeatCycle,Task
from datetime import datetime

from .task_manager import taskManager

class AddTaskCommand(Task):
    def __init__(self):
        self.title = input("Enter Task:")

    def execute(self):
        print(taskManager.add_task(self.title))

class ViewTasksCommand():
    def execute(self):
        taskManager.view_tasks()

class ModifyTasksCommand():
    def execute(self):
        pass

class RemoveTaskCommand():
    def execute(self):
        pass

class EmptyDatabaseCommand():
    def execute(self):
        pass

class CommpletedTasksCommand():
    def execute(self):
        pass

class QuitCommand():
    def execute(self):
        print(taskManager.quit_manager())
        print("Exiting....")
        quit()
    
