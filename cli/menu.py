"""
Menu navigation structure using prompt_toolkit
"""

from typing import List, Optional
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich.table import Table

from models.todo import Todo, TodoStatus
from models.todo_list import TodoList
from skills.cli_formatting import CliOutputFormattingSkill
from utils.validators import TodoValidationSkill


class Menu:
    """Interactive menu with arrow-key navigation"""

    def __init__(self):
        self.todo_list = TodoList()
        self.formatter = CliOutputFormattingSkill()
        self.running = True
        self.categories = ["Work", "Personal", "Shopping", "Health", "General", "Other"]
        self._add_sample_data()

    def run(self):
        """Run the main application loop"""
        self.formatter.print_info("Welcome to the Interactive Todo Application!")

        while self.running:
            try:
                self._show_main_menu()
            except KeyboardInterrupt:
                self._exit_app()
                break
            except Exception as e:
                self.formatter.print_error(f"An error occurred: {str(e)}")

    def _show_main_menu(self):
        """Display the main interactive menu"""
        options = [
            "Add todo",
            "List all todos",
            "Search todos",
            "Filter todos by category",
            "Complete todo",
            "Mark todo as incomplete",
            "Update todo",
            "Delete todo",
            "Undo last action",
            "Help",
            "Exit"
        ]

        self.formatter.print_menu("Main Menu", options)

        try:
            choice = Prompt.ask(
                "[bold]Select an option (1-11)[/bold]",
                choices=[str(i) for i in range(1, len(options) + 1)],
                default="1"
            )

            choice_num = int(choice)

            if choice_num == 1:
                self._add_todo()
            elif choice_num == 2:
                self._list_todos()
            elif choice_num == 3:
                self._search_todos()
            elif choice_num == 4:
                self._filter_todos_by_category()
            elif choice_num == 5:
                self._complete_todo()
            elif choice_num == 6:
                self._mark_incomplete()
            elif choice_num == 7:
                self._update_todo()
            elif choice_num == 8:
                self._delete_todo()
            elif choice_num == 9:
                self._undo_last_action()
            elif choice_num == 10:
                self._show_help()
            elif choice_num == 11:
                self._exit_app()
        except Exception as e:
            self.formatter.print_error(f"Invalid input: {str(e)}")

    def _add_todo(self):
        """Add a new todo"""
        try:
            title = Prompt.ask("[bold]Enter todo title[/bold]").strip()
            if not title:
                self.formatter.print_error("Title is required!")
                return

            # Ask for custom ID
            custom_id = Prompt.ask("[bold]Enter custom ID (optional, press Enter for auto-generated)[/bold]", default="")

            description = Prompt.ask("[bold]Enter description (optional)[/bold]", default="")

            # Use regular prompt for category selection
            category_choices = [f"{i+1}. {cat}" for i, cat in enumerate(self.categories)]
            self.formatter.console.print("\n[bold]Available Categories:[/bold]")
            for choice in category_choices:
                self.formatter.console.print(f"  {choice}")

            category_choice = Prompt.ask(
                "[bold]Enter category number or name[/bold]",
                choices=[str(i) for i in range(1, len(self.categories) + 1)] + self.categories,
                default="1"
            )

            # Determine category based on input
            if category_choice.isdigit():
                idx = int(category_choice) - 1
                if 0 <= idx < len(self.categories):
                    category = self.categories[idx]
                else:
                    category = "General"  # Default if invalid number
            else:
                # Check if the input matches a category name (case-insensitive)
                category = "General"  # Default
                for cat in self.categories:
                    if cat.lower() == category_choice.lower():
                        category = cat
                        break

            # Validate the todo data
            validation_errors = TodoValidationSkill.validate_todo_data(title, description, category)
            if validation_errors:
                for error in validation_errors:
                    self.formatter.print_error(error)
                return

            # Create and add the todo with custom ID if provided
            if custom_id.strip():
                todo = Todo(title=title, description=description, category=category, todo_id=custom_id.strip())
            else:
                todo = Todo(title=title, description=description, category=category)

            self.todo_list.add(todo)

            if custom_id.strip():
                self.formatter.print_success(f"Todo '{todo.title}' added successfully with custom ID: {todo.id}!")
            else:
                self.formatter.print_success(f"Todo '{todo.title}' added successfully with auto-generated ID: {todo.id}!")

        except KeyboardInterrupt:
            self.formatter.print_info("Add todo cancelled.")
        except Exception as e:
            self.formatter.print_error(f"Error adding todo: {str(e)}")

    def _list_todos(self):
        """List all todos"""
        todos = self.todo_list.get_all()
        if todos:
            self.formatter.print_todo_list(todos, "All Todos")
        else:
            self.formatter.print_info("No todos in the list.")

    def _search_todos(self):
        """Search todos by title or description"""
        try:
            query = Prompt.ask("[bold]Enter search query[/bold]").strip()
            if not query:
                self.formatter.print_info("Search query cannot be empty.")
                return

            results = self.todo_list.search(query)
            if results:
                self.formatter.print_todo_list(results, f"Search Results for '{query}'")
            else:
                self.formatter.print_info(f"No todos found matching '{query}'.")

        except KeyboardInterrupt:
            self.formatter.print_info("Search cancelled.")

    def _filter_todos_by_category(self):
        """Filter todos by category"""
        try:
            # Use regular prompt for category selection
            category_choices = [f"{i+1}. {cat}" for i, cat in enumerate(self.categories)]
            self.formatter.console.print("\n[bold]Available Categories:[/bold]")
            for choice in category_choices:
                self.formatter.console.print(f"  {choice}")

            category_choice = Prompt.ask(
                "[bold]Enter category number or name to filter by[/bold]",
                choices=[str(i) for i in range(1, len(self.categories) + 1)] + self.categories,
                default="1"
            )

            # Determine category based on input
            if category_choice.isdigit():
                idx = int(category_choice) - 1
                if 0 <= idx < len(self.categories):
                    category = self.categories[idx]
                else:
                    self.formatter.print_info("Invalid category number.")
                    return
            else:
                # Check if the input matches a category name (case-insensitive)
                category = None
                for cat in self.categories:
                    if cat.lower() == category_choice.lower():
                        category = cat
                        break
                if not category:
                    self.formatter.print_info("Invalid category name.")
                    return

            results = self.todo_list.get_by_category(category)
            if results:
                self.formatter.print_todo_list(results, f"Todos in Category: {category}")
            else:
                self.formatter.print_info(f"No todos found in category '{category}'.")

        except KeyboardInterrupt:
            self.formatter.print_info("Filter cancelled.")

    def _complete_todo(self):
        """Mark a todo as complete"""
        todos = self.todo_list.get_by_status(TodoStatus.INCOMPLETE)
        if not todos:
            self.formatter.print_info("No incomplete todos to complete.")
            return

        self.formatter.print_todo_list(todos, "Incomplete Todos")

        try:
            todo_id = Prompt.ask("[bold]Enter ID of todo to complete (or 'cancel')[/bold]").strip()
            if todo_id.lower() == 'cancel':
                return

            # Find and update the todo
            if self.todo_list.update(todo_id, status=TodoStatus.COMPLETE):
                self.formatter.print_success("Todo marked as complete!")
            else:
                self.formatter.print_error("Todo not found!")

        except KeyboardInterrupt:
            self.formatter.print_info("Complete todo cancelled.")

    def _mark_incomplete(self):
        """Mark a todo as incomplete"""
        todos = self.todo_list.get_by_status(TodoStatus.COMPLETE)
        if not todos:
            self.formatter.print_info("No completed todos to mark as incomplete.")
            return

        self.formatter.print_todo_list(todos, "Completed Todos")

        try:
            todo_id = Prompt.ask("[bold]Enter ID of todo to mark incomplete (or 'cancel')[/bold]").strip()
            if todo_id.lower() == 'cancel':
                return

            # Find and update the todo
            if self.todo_list.update(todo_id, status=TodoStatus.INCOMPLETE):
                self.formatter.print_success("Todo marked as incomplete!")
            else:
                self.formatter.print_error("Todo not found!")

        except KeyboardInterrupt:
            self.formatter.print_info("Mark incomplete cancelled.")

    def _update_todo(self):
        """Update an existing todo"""
        todos = self.todo_list.get_all()
        if not todos:
            self.formatter.print_info("No todos to update.")
            return

        self.formatter.print_todo_list(todos, "All Todos")

        try:
            todo_id = Prompt.ask("[bold]Enter ID of todo to update (or 'cancel')[/bold]").strip()
            if todo_id.lower() == 'cancel':
                return

            todo = self.todo_list.find_by_id(todo_id)
            if not todo:
                self.formatter.print_error("Todo not found!")
                return

            # Get updated values
            new_title = Prompt.ask(f"[bold]Enter new title (current: {todo.title})[/bold]", default=todo.title)
            new_description = Prompt.ask(f"[bold]Enter new description (current: {todo.description})[/bold]",
                                       default=todo.description)

            # Use regular prompt for category selection
            category_choices = [f"{i+1}. {cat}" for i, cat in enumerate(self.categories)]
            self.formatter.console.print("\n[bold]Available Categories:[/bold]")
            for choice in category_choices:
                self.formatter.console.print(f"  {choice}")

            category_choice = Prompt.ask(
                f"[bold]Enter category number or name (current: {todo.category})[/bold]",
                choices=[str(i) for i in range(1, len(self.categories) + 1)] + self.categories,
                default="1"
            )

            # Determine category based on input
            if category_choice.isdigit():
                idx = int(category_choice) - 1
                if 0 <= idx < len(self.categories):
                    new_category = self.categories[idx]
                else:
                    new_category = todo.category  # Keep current category if invalid number
            else:
                # Check if the input matches a category name (case-insensitive)
                new_category = todo.category  # Default to current category
                for cat in self.categories:
                    if cat.lower() == category_choice.lower():
                        new_category = cat
                        break

            # Validate the updated todo data
            validation_errors = TodoValidationSkill.validate_todo_data(new_title, new_description, new_category)
            if validation_errors:
                for error in validation_errors:
                    self.formatter.print_error(error)
                return

            # Update the todo
            if self.todo_list.update(todo_id, title=new_title, description=new_description, category=new_category):
                self.formatter.print_success("Todo updated successfully!")
            else:
                self.formatter.print_error("Failed to update todo!")

        except KeyboardInterrupt:
            self.formatter.print_info("Update todo cancelled.")

    def _delete_todo(self):
        """Delete a todo"""
        todos = self.todo_list.get_all()
        if not todos:
            self.formatter.print_info("No todos to delete.")
            return

        self.formatter.print_todo_list(todos, "All Todos")

        try:
            todo_id = Prompt.ask("[bold]Enter ID of todo to delete (or 'cancel')[/bold]").strip()
            if todo_id.lower() == 'cancel':
                return

            # Confirm deletion
            confirm = Confirm.ask("Are you sure you want to delete this todo?")
            if not confirm:
                self.formatter.print_info("Deletion cancelled.")
                return

            if self.todo_list.remove(todo_id):
                self.formatter.print_success("Todo deleted successfully!")
            else:
                self.formatter.print_error("Todo not found!")

        except KeyboardInterrupt:
            self.formatter.print_info("Delete todo cancelled.")

    def _undo_last_action(self):
        """Undo the last action"""
        if self.todo_list.undo_last_action():
            self.formatter.print_success("Last action undone!")
        else:
            self.formatter.print_info("No actions to undo.")

    def _show_help(self):
        """Show help information"""
        self.formatter.console.print("\n[bold underline]Help - Interactive Todo Application[/bold underline]")
        self.formatter.console.print("\n[bold]Application Features:[/bold]")
        self.formatter.console.print("• Add, list, search, filter, complete, update, and delete todos")
        self.formatter.console.print("• Interactive menu with arrow-key navigation")
        self.formatter.console.print("• Colorful and user-friendly interface using rich library")
        self.formatter.console.print("• In-memory storage during session (no persistence between runs)")
        self.formatter.console.print("• Undo functionality for the last action")
        self.formatter.console.print("• Category-based organization")
        self.formatter.console.print("\n[bold]How to Use:[/bold]")
        self.formatter.console.print("• Use arrow keys to navigate menus and select options")
        self.formatter.console.print("• Enter the number of your choice at the prompt")
        self.formatter.console.print("• Use 'cancel' at any input prompt to return to the previous menu")
        self.formatter.console.print("• Use Ctrl+C to exit the application at any time")
        self.formatter.console.print("\n[bold]Todo Status:[/bold]")
        self.formatter.console.print("• [red]○[/red] = Incomplete")
        self.formatter.console.print("• [green]✓[/green] = Complete")

    def _exit_app(self):
        """Exit the application"""
        self.formatter.print_info("Exiting the application. Goodbye!")
        self.running = False

    def _add_sample_data(self):
        """Add 3 practice data items to the todo list"""
        # Create 3 sample todos for practice
        sample_todos = [
            Todo(title="Practice coding exercises",
                 description="Complete at least 3 coding problems from LeetCode",
                 category="Work",
                 status=TodoStatus.INCOMPLETE),
            Todo(title="Review project documentation",
                 description="Read and understand the project requirements and architecture",
                 category="Work",
                 status=TodoStatus.INCOMPLETE),
            Todo(title="Plan weekend activities",
                 description="Organize activities for the upcoming weekend with family",
                 category="Personal",
                 status=TodoStatus.INCOMPLETE)
        ]

        # Add the sample todos to the todo list
        for todo in sample_todos:
            self.todo_list.add(todo)

        self.formatter.print_info(f"Added {len(sample_todos)} practice data items to the todo list.")