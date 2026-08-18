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
    def __init__(self,
                 task_id : int,
                 title : str,
                 created : str = datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 
                 last_updated : str = datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                 status = Status.UNSTARTED,
                 to_be_repeated = RepeatCycle.NONE
                 ) -> None:
        self.task_id : int = task_id
        self.title : str = title
        self.created : str = created
        self.last_updated : str = last_updated
        self.status : Status = Status(status) if isinstance(status,str) else status 
        self.to_be_repeated : RepeatCycle = RepeatCycle(to_be_repeated) if isinstance(to_be_repeated,str) else to_be_repeated
    
    def to_dict(self)->dict:
        return {
                "task_id" : self.task_id,
                "title" : self.title,
                "created" : self.created,
                "last_updated" : self.last_updated,
                "status" : self.status.value,
                "to_be_repeated" : self.to_be_repeated.value
                }

    @classmethod
    def from_dict(cls,data:dict)->Task:
        return cls(
                task_id = int(data["task_id"]),
                title = data["title"],
                created = data["created"],
                last_updated = data["last_updated"],
                status = Status(data["status"]),
                to_be_repeated = RepeatCycle(data["to_be_repeated"]),
                )
