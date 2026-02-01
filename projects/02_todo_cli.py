"""
Mini Project 2: Todo List CLI Application
==========================================
Combines: Lists, Dictionaries, File I/O (JSON), Functions, Error Handling

Build a command-line todo list with persistence.
"""

import json
import os
from datetime import datetime

# File to store todos
TODO_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'todos.json')

# =============================================================================
# Data Structure
# =============================================================================
# Each todo is a dictionary:
# {
#     "id": 1,
#     "task": "Buy groceries",
#     "done": False,
#     "priority": "medium",  # low, medium, high
#     "created_at": "2024-01-15 10:30:00",
#     "due_date": "2024-01-20",  # optional
#     "tags": ["shopping", "home"]  # optional
# }

# =============================================================================
# TODO: Implement Storage Functions
# =============================================================================

def load_todos():
    """
    Load todos from the JSON file.
    Returns an empty list if file doesn't exist.
    """
    # TODO: Implement
    pass


def save_todos(todos):
    """Save todos to the JSON file."""
    # TODO: Implement
    pass


def get_next_id(todos):
    """Get the next available todo ID."""
    # TODO: Return max id + 1, or 1 if list is empty
    pass


# =============================================================================
# TODO: Implement CRUD Operations
# =============================================================================

def add_todo(task, priority="medium", due_date=None, tags=None):
    """
    Add a new todo.

    Args:
        task: The task description
        priority: "low", "medium", or "high"
        due_date: Optional due date string (YYYY-MM-DD)
        tags: Optional list of tags

    Returns:
        The created todo dict
    """
    # TODO: Implement
    # 1. Load existing todos
    # 2. Create new todo with all fields
    # 3. Append and save
    # 4. Return the new todo
    pass


def list_todos(show_done=True, filter_priority=None, filter_tag=None):
    """
    List todos with optional filters.

    Args:
        show_done: Whether to include completed todos
        filter_priority: Only show todos with this priority
        filter_tag: Only show todos with this tag

    Returns:
        Filtered list of todos
    """
    # TODO: Implement
    pass


def get_todo(todo_id):
    """Get a single todo by ID."""
    # TODO: Implement
    pass


def update_todo(todo_id, task=None, priority=None, due_date=None, tags=None):
    """
    Update a todo's fields.
    Only update fields that are not None.
    """
    # TODO: Implement
    pass


def mark_done(todo_id):
    """Mark a todo as completed."""
    # TODO: Implement
    pass


def mark_undone(todo_id):
    """Mark a todo as not completed."""
    # TODO: Implement
    pass


def delete_todo(todo_id):
    """Delete a todo by ID."""
    # TODO: Implement
    pass


def clear_done():
    """Delete all completed todos."""
    # TODO: Implement
    pass


# =============================================================================
# TODO: Implement Display Functions
# =============================================================================

def format_todo(todo, show_details=False):
    """
    Format a todo for display.

    Basic: [x] 1. Buy groceries (high)
    Detailed: Includes due date, tags, created date
    """
    # TODO: Implement
    pass


def display_todos(todos, title="Todo List"):
    """Display a list of todos nicely formatted."""
    # TODO: Implement
    # Show count, then each todo formatted
    pass


def display_stats():
    """Display statistics about todos."""
    # TODO: Implement
    # Show: total, done, pending, by priority
    pass


# =============================================================================
# TODO: Implement CLI Interface
# =============================================================================

def show_help():
    """Display help message."""
    print("""
Todo List Commands:
==================
  add <task>           Add a new todo
  list [all]           List pending todos (or all)
  done <id>            Mark todo as done
  undone <id>          Mark todo as not done
  delete <id>          Delete a todo
  edit <id>            Edit a todo
  priority <id> <p>    Set priority (low/medium/high)
  tag <id> <tags>      Set tags (comma-separated)
  due <id> <date>      Set due date (YYYY-MM-DD)
  clear                Clear all completed todos
  stats                Show statistics
  help                 Show this help
  quit                 Exit the program
    """)


def parse_command(input_str):
    """
    Parse user input into command and arguments.
    Returns: (command, args_list)
    """
    parts = input_str.strip().split(maxsplit=1)
    command = parts[0].lower() if parts else ""
    args = parts[1] if len(parts) > 1 else ""
    return command, args


def main():
    """Main function to run the todo CLI."""
    print("=" * 40)
    print("   TODO LIST APPLICATION")
    print("=" * 40)
    print("Type 'help' for available commands.\n")

    while True:
        try:
            user_input = input("todo> ").strip()

            if not user_input:
                continue

            command, args = parse_command(user_input)

            if command == "quit" or command == "exit":
                print("Goodbye!")
                break

            elif command == "help":
                show_help()

            elif command == "add":
                if not args:
                    print("Usage: add <task>")
                else:
                    # TODO: Add the todo and display confirmation
                    pass

            elif command == "list":
                # TODO: List todos (all if args == "all")
                pass

            elif command == "done":
                # TODO: Mark todo as done
                pass

            elif command == "undone":
                # TODO: Mark todo as undone
                pass

            elif command == "delete":
                # TODO: Delete todo
                pass

            elif command == "edit":
                # TODO: Edit todo task
                pass

            elif command == "priority":
                # TODO: Set priority
                # Parse: <id> <priority>
                pass

            elif command == "tag":
                # TODO: Set tags
                pass

            elif command == "due":
                # TODO: Set due date
                pass

            elif command == "clear":
                # TODO: Clear completed todos
                pass

            elif command == "stats":
                display_stats()

            else:
                print(f"Unknown command: {command}")
                print("Type 'help' for available commands.")

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")


# =============================================================================
# Tests
# =============================================================================

def run_tests():
    """Test the todo functions."""
    # Clean start
    if os.path.exists(TODO_FILE):
        os.remove(TODO_FILE)

    print("Running tests...")

    # Test add
    todo1 = add_todo("Buy milk", priority="high")
    assert todo1["id"] == 1, "First todo should have id 1"
    assert todo1["done"] == False, "New todo should not be done"
    print(f"✓ Added todo: {todo1['task']}")

    # Test add another
    todo2 = add_todo("Walk the dog", priority="medium", tags=["pets"])
    assert todo2["id"] == 2, "Second todo should have id 2"
    print(f"✓ Added todo: {todo2['task']}")

    # Test list
    todos = list_todos()
    assert len(todos) == 2, "Should have 2 todos"
    print(f"✓ Listed {len(todos)} todos")

    # Test mark done
    mark_done(1)
    todo = get_todo(1)
    assert todo["done"] == True, "Todo should be marked done"
    print("✓ Marked todo as done")

    # Test filter
    pending = list_todos(show_done=False)
    assert len(pending) == 1, "Should have 1 pending todo"
    print("✓ Filtered pending todos")

    # Test delete
    delete_todo(2)
    todos = list_todos()
    assert len(todos) == 1, "Should have 1 todo after delete"
    print("✓ Deleted todo")

    # Cleanup
    os.remove(TODO_FILE)
    print("\nAll tests passed!")


if __name__ == "__main__":
    # Uncomment to run tests:
    # run_tests()

    # Run the main program:
    main()
