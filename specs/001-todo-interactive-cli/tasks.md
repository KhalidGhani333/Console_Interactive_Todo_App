# Tasks: In-Memory and JSON-Persistent Python Command-Line Todo Application with Interactive Menus

**Feature**: In-Memory and JSON-Persistent Python Command-Line Todo Application with Interactive Menus
**Feature Branch**: `001-todo-interactive-cli`
**Generated**: 2026-01-02
**Spec**: [specs/001-todo-interactive-cli/spec.md](spec.md)
**Plan**: [specs/001-todo-interactive-cli/plan.md](plan.md)

## Implementation Strategy

Implement a Python console-based todo application with interactive menu navigation using arrow keys. The application supports in-memory operations during runtime only, with no persistence between sessions. The solution will utilize Python with rich for UI components and prompt_toolkit for interactive menus and arrow-key navigation.

**Approach**: MVP-first with incremental delivery. Start with core functionality (add/list todos) and build up to full feature set.

## Dependencies

- User Stories dependencies: US2 (List todos) must be completed before US3 (Complete/Update) and US4 (Search/Filter)
- All stories depend on foundational setup and core models/services

## Parallel Execution Examples

- [P] T003-T006: Core models and services can be developed in parallel
- [P] US3 tasks: Complete, Update, Delete functionality can be developed in parallel after US1/US2
- [P] US4 tasks: Search and Filter functionality can be developed in parallel after US1/US2

---

## Phase 1: Setup (Project Initialization)

**Goal**: Initialize project structure and install required dependencies

- [X] T001 Set up project directory structure with models/, services/, cli/, utils/, skills/ directories
- [X] T002 Create requirements.txt with rich and prompt_toolkit dependencies
- [X] T003 Create main.py as the entry point for the application
- [X] T004 Install dependencies using pip install -r requirements.txt

## Phase 2: Foundational (Blocking Prerequisites)

**Goal**: Implement core models and services that all user stories depend on

- [X] T005 [P] Create Todo model in main.py with unique ID, title (required), description (optional), category, and completion status
- [X] T006 [P] Create TodoList model in main.py as collection of Todo entities stored in memory
- [X] T007 [P] Implement TodoDomainAgent (todo_service.py) - manages domain-level rules and lifecycle behavior for Todo items
- [X] T008 [P] Implement InMemoryStateSubagent (storage_service.py) - handles in-memory storage/retrieval of Todo items
- [X] T009 [P] Create TodoValidationSkill (validators.py) - reusable validation logic for Todo data
- [X] T010 [P] Create CliOutputFormattingSkill (cli_formatting.py) - professional CLI output formatting
- [X] T011 [P] Implement basic menu navigation structure using prompt_toolkit

## Phase 3: User Story 1 - Add Todo Item (Priority: P1)

**Story Goal**: Enable users to add new todo items to their list with a title, optional description, and category

**Independent Test Criteria**: Application can be tested by adding a todo item and verifying it appears in the list

- [X] T012 [US1] Implement "Add todo" menu option in main.py
- [X] T013 [US1] Create user-friendly prompts for collecting title, description, and category when adding todo
- [X] T014 [US1] Implement validation to ensure title is provided when adding a todo
- [X] T015 [US1] Generate unique ID for each new todo item
- [X] T016 [US1] Add new todo to in-memory storage
- [X] T017 [US1] Display confirmation message after successful todo addition
- [X] T018 [US1] Handle invalid inputs gracefully when adding todo with appropriate error messages

## Phase 4: User Story 2 - View and Manage Todo List (Priority: P1)

**Story Goal**: Enable users to see all their todos in a clearly formatted list that shows completion status and category

**Independent Test Criteria**: Application can be tested by adding multiple todos and then listing them to verify they display correctly with status indicators

- [X] T019 [US2] Implement "List all todos" menu option in main.py
- [X] T020 [US2] Create formatted list display using rich library showing completion status and category
- [X] T021 [US2] Implement visual indicators for completed/incomplete status
- [X] T022 [US2] Handle case when no todos exist with appropriate message
- [X] T023 [US2] Ensure proper formatting of todo list with rich tables and status indicators

## Phase 5: User Story 3 - Complete and Update Todos (Priority: P2)

**Story Goal**: Enable users to mark todos as complete when finished, update existing todos, or delete todos that are no longer needed

**Independent Test Criteria**: Application can be tested by completing a todo and verifying its status changes

- [X] T024 [US3] Implement "Complete todo" menu option in main.py
- [X] T025 [US3] Create functionality to select and mark a specific todo as complete
- [X] T026 [US3] Implement "Mark todo as incomplete" menu option in main.py
- [X] T027 [US3] Create functionality to select and mark a completed todo as incomplete
- [X] T028 [US3] Implement "Update todo" menu option in main.py
- [X] T029 [US3] Create prompts for updating title, description, or category of existing todo
- [X] T030 [US3] Implement "Delete todo" menu option in main.py
- [X] T031 [US3] Create functionality to select and remove a specific todo from the list
- [X] T032 [US3] Add confirmation prompts for delete operations

## Phase 6: User Story 4 - Search and Filter Todos (Priority: P2)

**Story Goal**: Enable users to find specific todos by searching through titles/descriptions or filter by category when they have many items in their list

**Independent Test Criteria**: Application can be tested by searching for a specific todo and verifying the correct results are returned

- [X] T033 [US4] Implement "Search todos" menu option in main.py
- [X] T034 [US4] Create search functionality that searches through titles and descriptions
- [X] T035 [US4] Display search results in formatted list with rich
- [X] T036 [US4] Implement "Filter todos by category" menu option in main.py
- [X] T037 [US4] Create filter functionality that shows only todos from selected category
- [X] T038 [US4] Display filtered results in formatted list with rich

## Phase 7: User Story 5 - In-Memory Session Management (Priority: P1)

**Story Goal**: Ensure proper in-memory management and session handling for todos during the application session

**Independent Test Criteria**: Application can be tested by adding todos during a session and verifying they exist until the application exits

- [X] T039 [US5] Implement in-memory storage that maintains todos during application session
- [X] T040 [US5] Ensure todos are available in memory for all operations during the session
- [X] T041 [US5] Implement proper cleanup to clear all todos from memory when application exits
- [X] T042 [US5] Handle application lifecycle to start with empty todo list

## Phase 8: Additional Menu Options and Features

**Goal**: Implement remaining menu options and features as specified in the requirements

- [X] T043 Implement "Undo last action" menu option in main.py
- [X] T044 Create functionality to track and undo the last action performed
- [X] T045 Implement "Help" menu option in main.py
- [X] T046 Create help information about using the application
- [X] T047 Implement "Exit" menu option in main.py
- [X] T048 Ensure application properly exits and clears all todos from memory

## Phase 9: Polish & Cross-Cutting Concerns

**Goal**: Complete the application with error handling, user experience improvements, and final features

- [X] T049 Implement comprehensive error handling for all user inputs with clear, friendly messages
- [X] T050 Ensure application never crashes due to user input with appropriate fallback behavior
- [X] T051 Add clear confirmation messages after each successful action
- [X] T052 Implement graceful handling of invalid user inputs with clear error messages
- [X] T053 Test that application handles edge cases (non-existent todos, invalid inputs, etc.)
- [X] T054 Perform final testing of all menu options and functionality
- [X] T055 Ensure responsive menu navigation with <200ms response time
- [X] T056 Verify search and filter functionality returns accurate results in under 1 second for up to 1000 todos