"""
Mini Project 3: Quiz Game
=========================
Combines: Dictionaries, Lists, Random, Loops, File I/O (JSON), Functions

Build an interactive quiz game with multiple categories and score tracking.
"""

import json
import random
import os
from datetime import datetime

# =============================================================================
# Sample Quiz Data
# =============================================================================

SAMPLE_QUIZZES = {
    "python": {
        "name": "Python Basics",
        "questions": [
            {
                "question": "What is the output of print(2 ** 3)?",
                "options": ["6", "8", "9", "5"],
                "correct": 1,  # index of correct answer (0-based)
                "explanation": "** is the exponentiation operator. 2^3 = 8"
            },
            {
                "question": "Which of these is NOT a valid Python data type?",
                "options": ["list", "tuple", "array", "dict"],
                "correct": 2,
                "explanation": "Python has lists, tuples, and dicts built-in. Arrays require numpy."
            },
            {
                "question": "What does len('hello') return?",
                "options": ["4", "5", "6", "Error"],
                "correct": 1,
                "explanation": "len() returns the number of characters: h-e-l-l-o = 5"
            },
            {
                "question": "Which keyword is used to define a function?",
                "options": ["function", "def", "func", "define"],
                "correct": 1,
                "explanation": "In Python, functions are defined using 'def'"
            },
            {
                "question": "What is the result of 10 // 3?",
                "options": ["3.33", "3", "4", "3.0"],
                "correct": 1,
                "explanation": "// is floor division, which returns an integer"
            }
        ]
    },
    "html": {
        "name": "HTML Fundamentals",
        "questions": [
            {
                "question": "What does HTML stand for?",
                "options": [
                    "Hyper Text Markup Language",
                    "Home Tool Markup Language",
                    "Hyperlinks and Text Markup Language",
                    "Hyperlinking Text Management Language"
                ],
                "correct": 0,
                "explanation": "HTML = HyperText Markup Language"
            },
            {
                "question": "Which tag is used for the largest heading?",
                "options": ["<head>", "<h6>", "<heading>", "<h1>"],
                "correct": 3,
                "explanation": "<h1> is the largest heading, <h6> is the smallest"
            },
            {
                "question": "What is the correct HTML element for a line break?",
                "options": ["<break>", "<lb>", "<br>", "<newline>"],
                "correct": 2,
                "explanation": "<br> creates a line break in HTML"
            },
            {
                "question": "Which attribute specifies an image's source?",
                "options": ["href", "src", "link", "source"],
                "correct": 1,
                "explanation": "The src attribute specifies the image URL"
            },
            {
                "question": "What tag creates a hyperlink?",
                "options": ["<link>", "<a>", "<href>", "<url>"],
                "correct": 1,
                "explanation": "The <a> (anchor) tag creates hyperlinks"
            }
        ]
    },
    "javascript": {
        "name": "JavaScript Basics",
        "questions": [
            {
                "question": "How do you declare a variable in modern JavaScript?",
                "options": ["var x", "let x", "int x", "variable x"],
                "correct": 1,
                "explanation": "'let' and 'const' are the modern ways to declare variables"
            },
            {
                "question": "What does '===' mean in JavaScript?",
                "options": [
                    "Assignment",
                    "Equality (value only)",
                    "Strict equality (value and type)",
                    "Not equal"
                ],
                "correct": 2,
                "explanation": "=== checks both value AND type (strict equality)"
            },
            {
                "question": "How do you select an element by ID?",
                "options": [
                    "document.querySelector('#id')",
                    "document.getElementById('id')",
                    "Both A and B",
                    "document.getElement('id')"
                ],
                "correct": 2,
                "explanation": "Both querySelector('#id') and getElementById('id') work"
            },
            {
                "question": "What is the output of typeof []?",
                "options": ["'array'", "'list'", "'object'", "'undefined'"],
                "correct": 2,
                "explanation": "In JavaScript, arrays are technically objects"
            },
            {
                "question": "Which method adds an element to the end of an array?",
                "options": ["append()", "push()", "add()", "insert()"],
                "correct": 1,
                "explanation": "push() adds elements to the end of an array"
            }
        ]
    }
}

# =============================================================================
# File paths
# =============================================================================

QUIZ_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'quizzes.json')
SCORES_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'quiz_scores.json')


# =============================================================================
# TODO: Implement Quiz Storage Functions
# =============================================================================

def load_quizzes():
    """Load quizzes from file, or return sample if file doesn't exist."""
    # TODO: Implement
    # Return SAMPLE_QUIZZES if file doesn't exist
    pass


def save_quizzes(quizzes):
    """Save quizzes to file."""
    # TODO: Implement
    pass


def load_scores():
    """Load score history from file."""
    # TODO: Implement
    # Return empty list if file doesn't exist
    pass


def save_score(category, score, total, player_name="Player"):
    """Save a quiz score."""
    # TODO: Implement
    # Append to scores list with timestamp
    pass


# =============================================================================
# TODO: Implement Quiz Functions
# =============================================================================

def list_categories():
    """List all available quiz categories."""
    # TODO: Implement
    pass


def get_quiz(category):
    """Get a quiz by category name."""
    # TODO: Implement
    pass


def shuffle_questions(questions, count=None):
    """
    Shuffle questions and optionally limit count.

    Args:
        questions: List of question dicts
        count: Optional max number of questions

    Returns:
        Shuffled (and optionally limited) list of questions
    """
    # TODO: Implement
    pass


def display_question(question, question_num, total):
    """
    Display a question with its options.

    Format:
    Question 1 of 5
    ----------------
    What is 2 + 2?

    1. 3
    2. 4
    3. 5
    4. 22
    """
    # TODO: Implement
    pass


def get_answer(num_options):
    """
    Get user's answer choice.
    Validate input (must be 1 to num_options).
    Returns the 0-based index.
    """
    # TODO: Implement
    pass


def check_answer(question, user_answer):
    """
    Check if the answer is correct.

    Returns:
        tuple: (is_correct, correct_answer_text, explanation)
    """
    # TODO: Implement
    pass


# =============================================================================
# TODO: Implement Game Functions
# =============================================================================

def run_quiz(category, num_questions=5):
    """
    Run a quiz session.

    Args:
        category: Quiz category to run
        num_questions: Number of questions to ask

    Returns:
        tuple: (score, total)
    """
    # TODO: Implement
    # 1. Get the quiz
    # 2. Shuffle and limit questions
    # 3. For each question:
    #    - Display it
    #    - Get answer
    #    - Check and show result
    #    - Update score
    # 4. Return final score
    pass


def display_results(score, total, category):
    """Display quiz results with feedback."""
    # TODO: Implement
    # Show percentage, grade, and encouraging message
    pass


def display_leaderboard(category=None, top_n=10):
    """Display top scores."""
    # TODO: Implement
    # Show top scores, optionally filtered by category
    pass


# =============================================================================
# TODO: Implement Main Menu
# =============================================================================

def show_menu():
    """Display the main menu."""
    print("\n" + "=" * 40)
    print("        QUIZ GAME")
    print("=" * 40)
    print("1. Take a Quiz")
    print("2. View Categories")
    print("3. View Leaderboard")
    print("4. Add Custom Question")
    print("5. Exit")
    print("=" * 40)


def select_category():
    """Let user select a quiz category."""
    # TODO: Implement
    # Display categories with numbers
    # Get user choice
    # Return category key
    pass


def add_custom_question():
    """Allow user to add a custom question."""
    # TODO: Implement
    # 1. Select category (or create new)
    # 2. Enter question text
    # 3. Enter 4 options
    # 4. Select correct answer
    # 5. Enter explanation
    # 6. Save to quizzes
    pass


def main():
    """Main game loop."""
    print("\n" + "*" * 40)
    print("*     WELCOME TO THE QUIZ GAME!      *")
    print("*" * 40)

    player_name = input("\nEnter your name: ").strip() or "Player"
    print(f"\nHello, {player_name}! Let's test your knowledge!\n")

    while True:
        show_menu()
        choice = input("Select option (1-5): ").strip()

        if choice == "1":
            # Take a quiz
            category = select_category()
            if category:
                num_q = input("How many questions? (default 5): ").strip()
                num_q = int(num_q) if num_q.isdigit() else 5

                score, total = run_quiz(category, num_q)
                display_results(score, total, category)

                # Save score
                save_score(category, score, total, player_name)

        elif choice == "2":
            # View categories
            list_categories()

        elif choice == "3":
            # View leaderboard
            display_leaderboard()

        elif choice == "4":
            # Add custom question
            add_custom_question()

        elif choice == "5":
            print(f"\nThanks for playing, {player_name}! Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


# =============================================================================
# Setup and Tests
# =============================================================================

def setup():
    """Initialize quiz data if needed."""
    if not os.path.exists(QUIZ_FILE):
        save_quizzes(SAMPLE_QUIZZES)
        print("Quiz data initialized!")


def run_tests():
    """Test quiz functions."""
    print("Running tests...")

    # Setup
    quizzes = SAMPLE_QUIZZES

    # Test list categories
    print(f"✓ Categories: {list(quizzes.keys())}")

    # Test get quiz
    python_quiz = quizzes.get("python")
    assert python_quiz is not None, "Python quiz should exist"
    print(f"✓ Python quiz has {len(python_quiz['questions'])} questions")

    # Test shuffle
    shuffled = list(python_quiz["questions"])
    random.shuffle(shuffled)
    shuffled = shuffled[:3]
    assert len(shuffled) == 3, "Should have 3 questions"
    print("✓ Shuffled questions")

    # Test check answer
    q = python_quiz["questions"][0]  # 2**3 = 8
    is_correct, correct_text, _ = True, q["options"][q["correct"]], q["explanation"]
    assert correct_text == "8", "Correct answer should be 8"
    print("✓ Answer checking works")

    print("\nAll tests passed!")


if __name__ == "__main__":
    # Uncomment to run tests:
    # run_tests()

    # Setup and run game
    setup()
    main()
