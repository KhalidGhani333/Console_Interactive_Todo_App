# Interactive CLI Todo Application

A feature-rich, interactive command-line interface todo application built with Python. This application provides a user-friendly interface with arrow-key navigation and comprehensive todo management capabilities.

## Features

- ✅ **Interactive Menu**: Navigate with arrow keys and number selection
- ✅ **Full CRUD Operations**: Create, read, update, delete todos
- ✅ **Search & Filter**: Find todos by title, description, or category
- ✅ **Status Management**: Mark todos as complete/incomplete
- ✅ **Categories**: Organize todos with categories (Work, Personal, Shopping, etc.)
- ✅ **Custom IDs**: Option to use custom IDs or auto-generated UUIDs
- ✅ **Undo Functionality**: Revert the last action
- ✅ **Colorful UI**: Rich, colorful output using the `rich` library
- ✅ **Sample Data**: Pre-loaded with 3 practice data items
- ✅ **Input Validation**: Comprehensive validation for all inputs

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Clone the repository or download the source code
2. Navigate to the project directory:
   ```bash
   cd todo-inmemory-app
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Setup

### Virtual Environment (Recommended)

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application:
```bash
python main.py
```

The application will start with 3 pre-loaded practice data items and display an interactive menu with the following options:

1. **Add todo** - Create a new todo item
2. **List all todos** - Display all todos
3. **Search todos** - Find todos by title or description
4. **Filter todos by category** - Show todos in a specific category
5. **Complete todo** - Mark a todo as complete
6. **Mark todo as incomplete** - Change a completed todo back to incomplete
7. **Update todo** - Modify an existing todo
8. **Delete todo** - Remove a todo
9. **Undo last action** - Revert the last operation
10. **Help** - Show help information
11. **Exit** - Close the application

## Project Structure

```
todo-inmemory-app/
├── main.py                 # Main application entry point
├── requirements.txt        # Python dependencies
├── cli/
│   └── menu.py            # Interactive menu implementation
├── models/
│   ├── todo.py            # Todo data model
│   └── todo_list.py       # Todo list management
├── services/
│   ├── todo_service.py    # Business logic
│   └── storage_service.py # Storage operations
├── skills/
│   └── cli_formatting.py  # UI formatting utilities
├── utils/
│   └── validators.py      # Input validation utilities
├── specs/                 # Project specifications
└── history/               # Prompt history records
```

## Sample Data

The application starts with 3 pre-loaded practice data items:
1. "Practice coding exercises" - Work category
2. "Review project documentation" - Work category
3. "Plan weekend activities" - Personal category

## Dependencies

- `prompt_toolkit` - For interactive command-line interface
- `rich` - For rich text and beautiful formatting
- `pydantic` - For data validation (if used)

## License

This project is available as-is without any warranty or specific license terms.

## Contributing

Feel free to fork this repository and submit pull requests for improvements. All contributions are welcome!