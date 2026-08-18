from InquirerPy import inquirer
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from core import task
from services.session import current_session

Menu = {
        "➕ Add a Task":task.AddTaskCommand,
        "🛠️ Modify Task":task.ModifyTasksCommand,
        "❌ Remove Task":task.RemoveTaskCommand,
        "📋 View Tasks":task.ViewTasksCommand,
        "🧹 Empty Database":task.EmptyDatabaseCommand,
        "💾 Save and Quit":task.QuitCommand,
        "✅ Show me Completed Tasks":task.CommpletedTasksCommand
}

def main():

    current_session.StartUpExecutions()

    while(True):
        try :
            console = Console()

            console.print(
                    Align.center(
                        Panel.fit(
                            "[bold green]Memento[/]",
                            border_style="cyan"
                            )
                        )
                    )

            console.print()

            choice = inquirer.select(
                    "",
                    choices= list(Menu.keys()),
                    ).execute()

            command = Menu.get(choice)

            if command:
                command_instance = command()
                command_instance.execute()

        except KeyboardInterrupt:
            quit_application = task.QuitCommand()
            quit_application.execute()
        

if __name__=="__main__":
    main()
