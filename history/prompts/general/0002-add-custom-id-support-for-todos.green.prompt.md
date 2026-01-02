---
id: 0002
title: Add Custom ID Support for Todos
stage: green
date: 2026-01-03
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: master
user: khalid ghani
command: manual
labels: ["feature", "custom-id", "user-input", "todo-app"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - models/todo.py
  - cli/menu.py
  - models/todo_list.py
  - skills/cli_formatting.py
tests:
  - test_custom_id.py
---

## Prompt

User requested to modify the todo application so that users can provide their own custom IDs for todos instead of using auto-generated UUIDs. The user wanted to be able to assign their own IDs to todos.

## Response snapshot

Successfully implemented custom ID functionality for the todo application. Users can now provide their own custom IDs when adding todos, with the option to fall back to auto-generated IDs. The implementation includes: 1) Updated Todo model to accept custom IDs, 2) Modified CLI menu to prompt for custom IDs, 3) Added duplicate ID prevention in TodoList model, 4) Updated UI to show full IDs (no longer truncated), and 5) Comprehensive testing to verify all functionality works correctly.

## Outcome

- ✅ Impact: Users can now provide custom IDs when creating todos, with fallback to auto-generated IDs
- 🧪 Tests: Created comprehensive tests verifying custom ID functionality works properly
- 📁 Files: Modified 4 files (models/todo.py, cli/menu.py, models/todo_list.py, skills/cli_formatting.py)
- 🔁 Next prompts: none
- 🧠 Reflection: Feature enhances user experience by allowing meaningful IDs for better organization

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): All tests passed showing the feature works correctly
- Prompt variant (if applicable): none
- Next experiment (smallest change to try): none