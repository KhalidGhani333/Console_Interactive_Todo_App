# Data Model: Todo Interactive CLI Application

## Todo Entity

**Fields**:
- `id` (str): Unique identifier for the todo item (UUID string)
- `title` (str): Required title of the todo item (min length: 1 character)
- `description` (str): Optional description of the todo item (can be empty/null)
- `category` (str): Category for organizing the todo (default: "General")
- `completed` (bool): Status indicating if the todo is completed (default: False)
- `created_at` (datetime): Timestamp when the todo was created
- `updated_at` (datetime): Timestamp when the todo was last updated

**Validation Rules**:
- Title must be provided and not empty
- Title must not exceed 200 characters
- Description, if provided, must not exceed 1000 characters
- Category must not exceed 50 characters
- ID must be unique within the todo list

**State Transitions**:
- `incomplete` → `completed` (when marked complete)
- `completed` → `incomplete` (when marked incomplete)

## TodoList Collection

**Fields**:
- `todos` (list[Todo]): Collection of Todo entities
- `last_action` (str): Track the last action for undo functionality

**Operations**:
- `add(todo: Todo)`: Add a new todo to the list
- `get_by_id(id: str)`: Retrieve a todo by its ID
- `update(id: str, updates: dict)`: Update a todo's properties
- `delete(id: str)`: Remove a todo from the list
- `list_all()`: Return all todos
- `filter_by_category(category: str)`: Return todos matching a category
- `search(query: str)`: Return todos matching the search query in title or description
- `mark_complete(id: str)`: Mark a todo as completed
- `mark_incomplete(id: str)`: Mark a todo as incomplete

## In-Memory Storage Format

**Structure**:
- Todos are stored in a Python list in memory
- Each todo is a Python object/dictionary with the specified fields
- All data is lost when the application exits

**Validation**:
- All todos exist in application memory
- Each todo must conform to Todo entity structure
- Memory usage should be monitored for performance