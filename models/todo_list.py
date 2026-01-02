"""
TodoList model - Collection of Todo entities stored in memory
"""

from typing import List, Optional
from datetime import datetime
from .todo import Todo, TodoStatus


class TodoList:
    """Collection of Todo entities stored in memory"""

    def __init__(self):
        self.todos: List[Todo] = []
        self.history: List[dict] = []  # For undo functionality

    def add(self, todo: Todo) -> None:
        """Add a todo to the list"""
        # Check if a todo with this ID already exists (if it's a custom ID)
        if self.find_by_id(todo.id) is not None:
            raise ValueError(f"A todo with ID '{todo.id}' already exists")

        self._save_state_for_undo("add", todo)
        self.todos.append(todo)

    def remove(self, todo_id: str) -> bool:
        """Remove a todo by ID (supports both full ID and truncated ID)"""
        for i, todo in enumerate(self.todos):
            if todo.id == todo_id or todo.id.startswith(todo_id):
                self._save_state_for_undo("remove", todo)
                del self.todos[i]
                return True
        return False

    def update(self, todo_id: str, **kwargs) -> bool:
        """Update a todo by ID (supports both full ID and truncated ID)"""
        for todo in self.todos:
            if todo.id == todo_id or todo.id.startswith(todo_id):
                self._save_state_for_undo("update", todo)

                if "title" in kwargs:
                    todo.title = kwargs["title"].strip()
                if "description" in kwargs:
                    todo.description = kwargs["description"].strip()
                if "category" in kwargs:
                    todo.category = kwargs["category"].strip()
                if "status" in kwargs:
                    todo.status = kwargs["status"]

                return True
        return False

    def find_by_id(self, todo_id: str) -> Optional[Todo]:
        """Find a todo by ID (supports both full ID and truncated ID)"""
        for todo in self.todos:
            if todo.id == todo_id or todo.id.startswith(todo_id):
                return todo
        return None

    def get_all(self) -> List[Todo]:
        """Get all todos"""
        return self.todos.copy()

    def get_by_status(self, status: TodoStatus) -> List[Todo]:
        """Get todos by status"""
        return [todo for todo in self.todos if todo.status == status]

    def get_by_category(self, category: str) -> List[Todo]:
        """Get todos by category"""
        return [todo for todo in self.todos if todo.category.lower() == category.lower()]

    def search(self, query: str) -> List[Todo]:
        """Search todos by title or description"""
        query = query.lower()
        results = []
        for todo in self.todos:
            if query in todo.title.lower() or query in todo.description.lower():
                results.append(todo)
        return results

    def _save_state_for_undo(self, action: str, todo: Todo) -> None:
        """Save state for undo functionality"""
        # Keep only the last 10 actions for memory efficiency
        if len(self.history) >= 10:
            self.history.pop(0)

        # Save action and the todo state before the action
        self.history.append({
            "action": action,
            "todo": todo.to_dict(),
            "timestamp": datetime.now().isoformat()
        })

    def undo_last_action(self) -> bool:
        """Undo the last action"""
        if not self.history:
            return False

        last_action = self.history.pop()
        action = last_action["action"]
        todo_data = last_action["todo"]
        todo = Todo.from_dict(todo_data)

        if action == "add":
            # Remove the added todo
            return self.remove(todo.id)
        elif action == "remove":
            # Add back the removed todo
            self.todos.append(todo)
            return True
        elif action == "update":
            # Restore the todo to its previous state
            # Find the current version and revert to the saved one
            for i, current_todo in enumerate(self.todos):
                if current_todo.id == todo.id:
                    # Replace with the previous state
                    self.todos[i] = todo
                    return True

        return False