"""
TodoValidationSkill - reusable validation logic for Todo data
"""

from typing import List
from models.todo import Todo


class TodoValidationSkill:
    """
    Provide reusable validation logic for Todo data.

    Capabilities:
    - Validate required fields
    - Enforce length and format constraints
    - Generate clear validation error messages

    Reusability:
    - Can be used by any domain or service agent
    """

    @staticmethod
    def validate_title(title: str) -> List[str]:
        """
        Validate the title field

        Args:
            title: Title to validate

        Returns:
            List of validation errors, empty if valid
        """
        errors = []

        if not title or not title.strip():
            errors.append("Title is required")
        elif len(title.strip()) > 200:
            errors.append("Title must be 200 characters or less")

        return errors

    @staticmethod
    def validate_description(description: str) -> List[str]:
        """
        Validate the description field

        Args:
            description: Description to validate

        Returns:
            List of validation errors, empty if valid
        """
        errors = []

        if description and len(description) > 1000:
            errors.append("Description must be 1000 characters or less")

        return errors

    @staticmethod
    def validate_category(category: str) -> List[str]:
        """
        Validate the category field

        Args:
            category: Category to validate

        Returns:
            List of validation errors, empty if valid
        """
        errors = []

        if not category or not category.strip():
            errors.append("Category is required")
        elif len(category.strip()) > 50:
            errors.append("Category must be 50 characters or less")

        return errors

    @staticmethod
    def validate_todo(todo: Todo) -> List[str]:
        """
        Validate a complete Todo entity

        Args:
            todo: Todo entity to validate

        Returns:
            List of validation errors, empty if valid
        """
        errors = []

        # Validate individual fields
        errors.extend(TodoValidationSkill.validate_title(todo.title))
        errors.extend(TodoValidationSkill.validate_description(todo.description))
        errors.extend(TodoValidationSkill.validate_category(todo.category))

        return errors

    @staticmethod
    def validate_todo_data(title: str, description: str = "", category: str = "") -> List[str]:
        """
        Validate raw todo data

        Args:
            title: Title to validate
            description: Description to validate
            category: Category to validate

        Returns:
            List of validation errors, empty if valid
        """
        errors = []

        errors.extend(TodoValidationSkill.validate_title(title))
        errors.extend(TodoValidationSkill.validate_description(description))
        errors.extend(TodoValidationSkill.validate_category(category))

        return errors