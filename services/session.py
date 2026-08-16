# from .utils import get_file_name
from .task_manager import task_manager

class Session():

    def StartUpExecutions(self):

        print("Starting Session......")
        print("Imported Saved Data .....")

        # file_name = get_file_name()
        # task_manager.file_name = file_name
        task_manager.load_from_json()
        
    def QuitExecutions(self):
        print(task_manager.save_to_json())
        print("Exiting....")
        quit()

current_session = Session()
