"""
TodoDomainAgent - manages domain-level rules and lifecycle behavior for Todo items
"""

from typing import List, Optional
from enum import Enum
import uuid
from datetime import datetime

from models.todo import Todo, TodoStatus


class TodoDomainAgent:
    """
    Manages all domain-level rules and lifecycle behavior for Todo items.

    Inputs:
    - Raw Todo input data
    - Requests to update Todo state

    Outputs:
    - Validated Todo entities
    - Domain operation results or domain-level error messages
    """

    def __init__(self):
        pass

    def create_todo(self, title: str, description: str = "", category: str = "General",
                    status: TodoStatus = TodoStatus.INCOMPLETE) -> Todo:
        """
        Create a new validated Todo entity

        Args:
            title: Required title for the todo
            description: Optional description
            category: Category for the todo (defaults to "General")
            status: Status for the todo (defaults to INCOMPLETE)

        Returns:
            Validated Todo entity

        Raises:
            ValueError: If validation fails
        """
        if not title or not title.strip():
            raise ValueError("Title is required")

        if not category or not category.strip():
            raise ValueError("Category is required")

        return Todo(
            title=title.strip(),
            description=description.strip(),
            category=category.strip(),
            status=status
        )

    def validate_todo(self, todo: Todo) -> List[str]:
        """
        Validate a todo entity and return list of validation errors

        Args:
            todo: Todo entity to validate

        Returns:
            List of validation error messages, empty if valid
        """
        errors = []

        if not todo.title or not todo.title.strip():
            errors.append("Title is required")

        if not todo.category or not todo.category.strip():
            errors.append("Category is required")

        return errors

    def update_todo(self, todo: Todo, title: Optional[str] = None,
                   description: Optional[str] = None,
                   category: Optional[str] = None,
                   status: Optional[TodoStatus] = None) -> List[str]:
        """
        Update todo properties with validation

        Args:
            todo: Todo entity to update
            title: New title (optional)
            description: New description (optional)
            category: New category (optional)
            status: New status (optional)

        Returns:
            List of validation error messages, empty if update is valid
        """
        if title is not None:
            todo.title = title.strip()

        if description is not None:
            todo.description = description.strip()

        if category is not None:
            todo.category = category.strip()

        if status is not None:
            todo.status = status

        # Validate the updated todo
        return self.validate_todo(todo)

    def can_complete_todo(self, todo: Todo) -> bool:
        """
        Check if a todo can be marked as complete

        Args:
            todo: Todo entity to check

        Returns:
            True if todo can be completed, False otherwise
        """
        # For now, any todo can be completed
        # In the future, we might have business rules here
        return True

    def can_delete_todo(self, todo: Todo) -> bool:
        """
        Check if a todo can be deleted

        Args:
            todo: Todo entity to check

        Returns:
            True if todo can be deleted, False otherwise
        """
        # For now, any todo can be deleted
        # In the future, we might have business rules here
        return True

    def get_todos_by_status(self, todos: List[Todo], status: TodoStatus) -> List[Todo]:
        """
        Filter todos by status

        Args:
            todos: List of todos to filter
            status: Status to filter by

        Returns:
            List of todos with the specified status
        """
        return [todo for todo in todos if todo.status == status]

    def get_todos_by_category(self, todos: List[Todo], category: str) -> List[Todo]:
        """
        Filter todos by category

        Args:
            todos: List of todos to filter
            category: Category to filter by

        Returns:
            List of todos in the specified category
        """
        return [todo for todo in todos if todo.category.lower() == category.lower()]

    def search_todos(self, todos: List[Todo], query: str) -> List[Todo]:
        """
        Search todos by title or description

        Args:
            todos: List of todos to search
            query: Search query

        Returns:
            List of matching todos
        """
        query = query.lower()
        results = []

        for todo in todos:
            if query in todo.title.lower() or query in todo.description.lower():
                results.append(todo)

        return results