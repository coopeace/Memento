from InquirerPy import inquirer
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from services import task

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
    while(True):

        console = Console()

        console.print(
            Align.center(
                Panel.fit(
                    "[bold green]My Awesome App[/]",
                    border_style="cyan"
                )
            )
        )

        choice = inquirer.select(
            "",
            choices= list(Menu.keys()),
          ).execute()

        command = Menu.get(choice)

        if command:
            command_instance = command()
            command_instance.execute()
            

if __name__=="__main__":
    main()
