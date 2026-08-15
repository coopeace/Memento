from InquirerPy import inquirer
from model import Profile,Status,RepeatCycle,Task
from datetime import datetime
from .session import current_session
from .task_manager import task_manager

class AddTaskCommand:
    def __init__(self):
        self.title = input(" Enter Task: ")

    def execute(self):
        print(task_manager.add_task(self.title))

class ViewTasksCommand():
    def execute(self):
        task_manager.view_tasks()

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
        current_session.QuitExecutions()
