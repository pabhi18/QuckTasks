import typer
from rich.console import Console
from rich.table import Table
from src.model import Todo
from src.database import get_all_todos, delete_todo, insert_todo, complete_todo, update_todo

console = Console()

app = typer.Typer()

@app.command(short_help='adds an item')
def add():
    console.print("[bold red]Enter the Task[/bold red]!")
    task = input("")
    console.print("[bold red]Enter the Category[/bold red]")
    category = input("")
    console.print(f"[bold white]Adding[/bold white] [bold green]{task}[/bold green], [bold blue]{category}[/bold blue]")
    todo = Todo(task, category)
    insert_todo(todo)
    show()

@app.command(short_help='delete a task')
def delete():
    console.print("[bold red]Enter the Task Position that you want to Delete[/bold red]!")
    position = int(input(""))
    console.print(f"[bold green]Deleting task at position {position}...[/bold green]")
    delete_todo(position-1)
    show()

@app.command(short_help='update position of task')
def update():
    console.print("[bold red]Enter the Task Position that you want to Update[/bold red]!")
    position = int(input(""))

    console.print("[bold yellow]Enter the New Task[/bold yellow]")
    new_task = input("")

    console.print("[bold blue]Enter the New Category (press Enter to keep it unchanged)[/bold blue]!")
    new_category = input("")

    console.print(f"[bold yellow]Updating task at position {position}...[/bold yellow]")
    update_todo(position-1, new_task, new_category)
    show()

@app.command(short_help='mark complete a task')
def complete():
    console.print("[bold red]Enter the Task Position that you want to Mark as Complete[/bold red]!")
    position = int(input(""))
    console.print(f"Marking task at position {position} as complete...")
    complete_todo(position-1)
    show()

@app.command(short_help='display todo list table')
def show():
    tasks = get_all_todos()
    console.print("[bold magenta]Todos[/bold magenta]!", "💻")

    table = Table(show_header=True, header_style="bold blue")
    table.add_column("#", style="dim", width=6)
    table.add_column("Todo", min_width=20)
    table.add_column("Category", min_width=12, justify="right")
    table.add_column("Done", min_width=12, justify="right")

    def get_category_color(category):
        COLORS = {'Learn': 'cyan', 'Sports': 'cyan', 'Academic': 'red', 'Coding': 'green'}

        lower_category = category.lower()
        if lower_category in COLORS:
            return COLORS[lower_category]
        return 'white'

    for idx, task in enumerate(tasks, start=1):
        c = get_category_color(task.category)
        is_done_str = '✅' if task.status == 2 else '❌'
        table.add_row(str(idx), task.task, f'[{c}]{task.category}[/{c}]', is_done_str)
    console.print(table)


if __name__ == "__main__":
    app()



