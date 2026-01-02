"""
CliOutputFormattingSkill - professional, colorful, and user-friendly CLI output formatting
"""

from typing import List
from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich.prompt import Prompt
from models.todo import Todo, TodoStatus


class CliOutputFormattingSkill:
    """
    Provide professional, colorful, and user-friendly CLI output formatting.

    Capabilities:
    - Format success, warning, and error messages
    - Display Todo lists using tables and status indicators
    - Improve readability and visual clarity of console output

    Reusability:
    - Can be reused across different CLI-based applications
    """

    def __init__(self):
        self.console = Console(force_terminal=True)

    def print_success(self, message: str) -> None:
        """
        Format and print a success message

        Args:
            message: Success message to print
        """
        self.console.print(f"[green]SUCCESS: {message}[/green]")

    def print_error(self, message: str) -> None:
        """
        Format and print an error message

        Args:
            message: Error message to print
        """
        self.console.print(f"[red]ERROR: {message}[/red]")

    def print_warning(self, message: str) -> None:
        """
        Format and print a warning message

        Args:
            message: Warning message to print
        """
        self.console.print(f"[yellow]WARNING: {message}[/yellow]")

    def print_info(self, message: str) -> None:
        """
        Format and print an info message

        Args:
            message: Info message to print
        """
        self.console.print(f"[blue]INFO: {message}[/blue]")

    def print_todo_list(self, todos: List[Todo], title: str = "Todo List") -> None:
        """
        Display a list of todos in a formatted table

        Args:
            todos: List of todos to display
            title: Title for the table
        """
        if not todos:
            self.print_info("No todos found.")
            return

        table = Table(title=title, show_header=True, header_style="bold magenta")
        table.add_column("ID", style="dim", width=8)
        table.add_column("Status", style="bold")
        table.add_column("Title", min_width=20)
        table.add_column("Category", style="cyan")
        table.add_column("Description", min_width=15)

        for todo in todos:
            status_symbol = "✓" if todo.status == TodoStatus.COMPLETE else "○"
            status_text = f"[green]{status_symbol}[/green]" if todo.status == TodoStatus.COMPLETE else f"[red]{status_symbol}[/red]"
            title_text = todo.title if todo.status == TodoStatus.INCOMPLETE else f"[strikethrough]{todo.title}[/strikethrough]"

            table.add_row(
                todo.id,  # Full ID (no longer truncated since users provide custom IDs)
                status_text,
                title_text,
                todo.category,
                todo.description or "No description"
            )

        self.console.print(table)

    def print_menu(self, title: str, options: List[str]) -> None:
        """
        Display a formatted menu

        Args:
            title: Title for the menu
            options: List of menu options
        """
        self.console.print(f"\n[bold underline]{title}[/bold underline]")
        for i, option in enumerate(options, 1):
            self.console.print(f"{i}. {option}")
        self.console.print()

    def print_todo_detail(self, todo: Todo) -> None:
        """
        Display detailed information about a single todo

        Args:
            todo: Todo to display
        """
        status_text = "Complete" if todo.status == TodoStatus.COMPLETE else "Incomplete"
        status_symbol = "✓" if todo.status == TodoStatus.COMPLETE else "○"

        self.console.print(f"\n[bold]Todo Details:[/bold]")
        self.console.print(f"ID: {todo.id}")
        self.console.print(f"Status: {status_symbol} [green]{status_text}[/green]")
        self.console.print(f"Title: {todo.title}")
        self.console.print(f"Category: [cyan]{todo.category}[/cyan]")
        if todo.description:
            self.console.print(f"Description: {todo.description}")
        self.console.print(f"Created: {todo.created_at.strftime('%Y-%m-%d %H:%M:%S')}")