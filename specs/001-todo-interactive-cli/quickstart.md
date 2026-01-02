# Quickstart Guide: Todo Interactive CLI Application

## Prerequisites

- Python 3.8 or higher
- pip package manager

## Setup

1. **Install dependencies**:
   ```bash
   pip install rich prompt_toolkit
   ```

2. **Create project structure**:
   ```
   todo-app/
   ├── main.py
   ├── todo_app/
   │   ├── __init__.py
   │   ├── models/
   │   │   ├── __init__.py
   │   │   ├── todo.py
   │   │   └── todo_list.py
   │   ├── services/
   │   │   ├── __init__.py
   │   │   ├── todo_service.py
   │   │   └── storage_service.py
   │   ├── cli/
   │   │   ├── __init__.py
   │   │   ├── menu.py
   │   │   └── input_handler.py
   │   └── utils/
   │       ├── __init__.py
   │       └── validators.py
   └── requirements.txt
   ```

3. **Create requirements.txt**:
   ```
   rich>=13.0.0
   prompt_toolkit>=3.0.0
   ```

## Running the Application

1. **Execute the main application**:
   ```bash
   python main.py
   ```

2. **Navigate the menu**:
   - Use arrow keys (up/down) to navigate options
   - Press Enter to select an option
   - Follow the on-screen prompts for input

## Basic Usage

1. **Add a todo**:
   - Navigate to "Add todo" option
   - Enter title (required)
   - Enter description (optional)
   - Enter category (optional)

2. **View todos**:
   - Navigate to "List all todos" option
   - Todos will display with completion status and category

3. **Complete a todo**:
   - Navigate to "Complete todo" option
   - Select the todo from the list
   - Status will update to completed

4. **Search and filter**:
   - Use "Search todos" to find by title/description
   - Use "Filter todos by category" to narrow results

## Configuration

The application stores all data in memory during the session. No configuration files are created.

## Troubleshooting

- If the application fails to start, ensure all dependencies are installed
- If menu navigation doesn't work, check terminal compatibility
- Note that all data is lost when the application exits