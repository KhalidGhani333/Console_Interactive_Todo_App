# Todo API Contract

## Overview
This document defines the internal API contracts for the Todo Interactive CLI application, specifying the interface between different components.

## Todo Service Interface

### Create Todo
```
Method: POST /todos
Input:
  - title (string, required): Title of the todo
  - description (string, optional): Description of the todo
  - category (string, optional): Category for the todo
Output:
  - todo (object): Created todo object with all fields
```

### Get All Todos
```
Method: GET /todos
Input: None
Output:
  - todos (array): Array of all todo objects
```

### Get Todo by ID
```
Method: GET /todos/{id}
Input:
  - id (string): Unique identifier of the todo
Output:
  - todo (object): Todo object matching the ID
```

### Update Todo
```
Method: PUT /todos/{id}
Input:
  - id (string): Unique identifier of the todo
  - updates (object): Fields to update (title, description, category)
Output:
  - todo (object): Updated todo object
```

### Delete Todo
```
Method: DELETE /todos/{id}
Input:
  - id (string): Unique identifier of the todo
Output:
  - success (boolean): Whether deletion was successful
```

### Mark Todo Complete
```
Method: PATCH /todos/{id}/complete
Input:
  - id (string): Unique identifier of the todo
Output:
  - todo (object): Updated todo object with completed status
```

### Mark Todo Incomplete
```
Method: PATCH /todos/{id}/incomplete
Input:
  - id (string): Unique identifier of the todo
Output:
  - todo (object): Updated todo object with incomplete status
```

### Search Todos
```
Method: GET /todos/search
Input:
  - query (string): Search term to match against title/description
Output:
  - todos (array): Array of matching todo objects
```

### Filter Todos by Category
```
Method: GET /todos/filter
Input:
  - category (string): Category to filter by
Output:
  - todos (array): Array of todos matching the category
```

### Undo Last Action
```
Method: POST /todos/undo
Input: None
Output:
  - success (boolean): Whether undo was successful
  - previous_state (object): State before the undone action
```

## Storage Service Interface

### Initialize In-Memory Store
```
Method: POST /storage/init
Input: None
Output:
  - success (boolean): Whether initialization was successful
```

### Clear In-Memory Store
```
Method: POST /storage/clear
Input: None
Output:
  - success (boolean): Whether clearing was successful
```

## CLI Input Handler Interface

### Get User Input
```
Method: GET /input/prompt
Input:
  - prompt (string): Message to display to user
  - input_type (string): Type of input expected (text, number, boolean, etc.)
Output:
  - value (any): Value entered by the user
```

### Display Menu
```
Method: POST /output/menu
Input:
  - options (array): Array of menu options to display
  - title (string): Title for the menu
Output:
  - selected_option (string): Option selected by user
```