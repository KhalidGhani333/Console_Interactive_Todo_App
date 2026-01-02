"""
InMemoryStateSubagent - handles in-memory storage and retrieval of Todo items during runtime
"""

from typing import List, Optional, Dict, Any
from datetime import datetime
import json

from models.todo import Todo


class InMemoryStateSubagent:
    """
    Handle in-memory storage and retrieval of Todo items during runtime.

    Inputs:
    - Create, update, delete, and lookup requests

    Outputs:
    - Stored Todo items or operation results

    Usage rules:
    - Used by domain or service-level logic
    - Must not perform validation or user interaction
    """

    def __init__(self):
        self.todos: Dict[str, Todo] = {}
        self.history: List[Dict[str, Any]] = []  # For undo functionality

    def create(self, todo: Todo) -> bool:
        """
        Store a new todo in memory

        Args:
            todo: Todo entity to store

        Returns:
            True if successful, False otherwise
        """
        self._save_state_for_undo("create", todo)
        self.todos[todo.id] = todo
        return True

    def get_by_id(self, todo_id: str) -> Optional[Todo]:
        """
        Retrieve a todo by its ID

        Args:
            todo_id: ID of the todo to retrieve

        Returns:
            Todo entity if found, None otherwise
        """
        return self.todos.get(todo_id)

    def get_all(self) -> List[Todo]:
        """
        Retrieve all todos

        Returns:
            List of all Todo entities
        """
        return list(self.todos.values())

    def update(self, todo_id: str, updated_todo: Todo) -> bool:
        """
        Update an existing todo

        Args:
            todo_id: ID of the todo to update
            updated_todo: Updated Todo entity

        Returns:
            True if successful, False if todo doesn't exist
        """
        if todo_id not in self.todos:
            return False

        self._save_state_for_undo("update", self.todos[todo_id])
        self.todos[todo_id] = updated_todo
        return True

    def delete(self, todo_id: str) -> bool:
        """
        Delete a todo by its ID

        Args:
            todo_id: ID of the todo to delete

        Returns:
            True if successful, False if todo doesn't exist
        """
        if todo_id not in self.todos:
            return False

        self._save_state_for_undo("delete", self.todos[todo_id])
        del self.todos[todo_id]
        return True

    def clear_all(self) -> None:
        """
        Clear all todos from memory
        """
        self.todos.clear()

    def count(self) -> int:
        """
        Get the count of todos in memory

        Returns:
            Number of todos stored in memory
        """
        return len(self.todos)

    def _save_state_for_undo(self, action: str, todo: Todo) -> None:
        """
        Save state for undo functionality

        Args:
            action: The action being performed
            todo: The todo being affected
        """
        # Keep only the last 10 actions for memory efficiency
        if len(self.history) >= 10:
            self.history.pop(0)

        self.history.append({
            "action": action,
            "todo_data": todo.__dict__.copy(),  # Store a copy of the todo's data
            "timestamp": datetime.now().isoformat()
        })

    def undo_last_action(self) -> bool:
        """
        Undo the last action

        Returns:
            True if undo was successful, False otherwise
        """
        if not self.history:
            return False

        last_action = self.history.pop()
        action = last_action["action"]
        todo_data = last_action["todo_data"]

        # Reconstruct the todo from saved data
        from models.todo import Todo, TodoStatus
        todo = Todo(
            title=todo_data.get('title', ''),
            description=todo_data.get('description', ''),
            category=todo_data.get('category', 'General'),
            status=todo_data.get('status', TodoStatus.INCOMPLETE),
            todo_id=todo_data.get('id')
        )

        if action == "create":
            # Remove the created todo
            return self.delete(todo.id)
        elif action == "update":
            # Restore the previous version of the todo
            return self.update(todo.id, todo)
        elif action == "delete":
            # Add back the deleted todo
            return self.create(todo)

        return False