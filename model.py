from datetime import datetime
from enum import Enum

class Status(Enum):
    UNSTARTED = "unstarted"
    PAUSED = "paused"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"

class RepeatCycle(Enum):
    NONE = "none"
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    YEARLY = "yearly"

class Profile:
    def __init__(self,
                 user:str = "guest",
                 password: str | None = None,
                 file_path: str | None = None
                 ) -> None:
        self.user : str
        self.password : str | None = None
        self.profile_created : str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.file_path : str | None = None
        self.login : bool = False

class Task:
    def __init__(self,task_id:int,title:str) -> None:
        self.task_id : int = task_id
        self.title : str = title
        self.created : str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.last_updated : str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.status : Status = Status.UNSTARTED
        self.to_be_repeated : RepeatCycle =  RepeatCycle.NONE
    
    def to_dict(self)->dict:
        return {
                "task_id" : self.task_id,
                "title" : self.title,
                "created" : self.created,
                "last_updated" : self.last_updated,
                "status" : self.status.value,
                "to_be_repeated" : self.to_be_repeated.value
                }
