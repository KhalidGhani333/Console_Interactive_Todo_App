"""
Todo model with unique ID, title (required), description (optional), category, and completion status
"""

import uuid
from datetime import datetime
from typing import Optional
from enum import Enum


class TodoStatus(Enum):
    """Enum for todo completion status"""
    INCOMPLETE = "incomplete"
    COMPLETE = "complete"


class Todo:
    """Todo item with unique ID, title, description, category, and completion status"""

    def __init__(self, title: str, description: str = "", category: str = "General",
                 status: TodoStatus = TodoStatus.INCOMPLETE, todo_id: Optional[str] = None):
        if not title.strip():
            raise ValueError("Title is required")

        if todo_id:
            # Use provided custom ID if valid
            self.id = todo_id.strip()
        else:
            # Generate UUID if no custom ID provided
            self.id = str(uuid.uuid4())
        self.title = title.strip()
        self.description = description.strip()
        self.category = category.strip()
        self.status = status
        self.created_at = datetime.now()

    def to_dict(self) -> dict:
        """Convert todo to dictionary for serialization"""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "category": self.category,
            "status": self.status.value,
            "created_at": self.created_at.isoformat()
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Todo':
        """Create todo from dictionary"""
        status_value = data.get("status", "incomplete")
        # Use the TodoStatus enum defined in this same file
        if status_value == "complete":
            status = TodoStatus.COMPLETE
        else:
            status = TodoStatus.INCOMPLETE
        todo = cls(
            title=data["title"],
            description=data.get("description", ""),
            category=data.get("category", "General"),
            status=status,
            todo_id=data.get("id")
        )
        if "created_at" in data:
            todo.created_at = datetime.fromisoformat(data["created_at"])
        return todo

    def __str__(self):
        status_symbol = "✓" if self.status == TodoStatus.COMPLETE else "○"
        return f"[{status_symbol}] {self.title} ({self.category})"