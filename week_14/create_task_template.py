"""
AP CSP Create Task - Program Template
=====================================

This template demonstrates all required elements for the Create Task:
- Input from user
- Use of a list
- A procedure with parameter that includes sequencing, selection, AND iteration

Feel free to use this structure as a starting point for your own program!
"""

# =============================================================================
# Example: Quiz Game (meets all Create Task requirements)
# =============================================================================

# The LIST stores quiz questions and answers
quiz_data = [
    {"question": "What is the capital of France?", "answer": "paris"},
    {"question": "What is 7 × 8?", "answer": "56"},
    {"question": "What planet is known as the Red Planet?", "answer": "mars"},
    {"question": "What is the largest ocean?", "answer": "pacific"},
    {"question": "In what year did WW2 end?", "answer": "1945"},
]


def check_answer(user_response, correct_answer):
    """
    PROCEDURE with PARAMETER that checks if the user's answer is correct.

    This function contains:
    - SEQUENCING: Steps execute in order
    - SELECTION: if/else to determine correctness
    - ITERATION: None in this function (but present in run_quiz)

    Args:
        user_response: The user's answer (string)
        correct_answer: The correct answer (string)

    Returns:
        True if correct, False otherwise
    """
    # SEQUENCING - these steps happen in order
    # Step 1: Clean up the user's response
    cleaned_response = user_response.strip().lower()

    # Step 2: Clean up the correct answer
    cleaned_correct = correct_answer.strip().lower()

    # SELECTION - choose what to return based on comparison
    if cleaned_response == cleaned_correct:
        return True
    else:
        return False


def run_quiz(questions_list, num_questions):
    """
    PROCEDURE with PARAMETERS that runs the quiz.

    Contains SEQUENCING, SELECTION, and ITERATION.

    Args:
        questions_list: List of question dictionaries
        num_questions: How many questions to ask

    Returns:
        The user's score
    """
    # SEQUENCING - initialize score
    score = 0

    # SELECTION - make sure we don't ask more questions than available
    if num_questions > len(questions_list):
        num_questions = len(questions_list)

    # ITERATION - loop through questions
    for i in range(num_questions):
        # Get current question from the LIST
        current_question = questions_list[i]

        # Display question (OUTPUT)
        print(f"\nQuestion {i + 1}: {current_question['question']}")

        # Get user INPUT
        user_answer = input("Your answer: ")

        # Use our procedure to check the answer
        is_correct = check_answer(user_answer, current_question['answer'])

        # SELECTION - respond based on correctness
        if is_correct:
            print("Correct!")
            score = score + 1
        else:
            print(f"Wrong! The answer was: {current_question['answer']}")

    return score


def display_results(final_score, total_questions):
    """
    Display the final quiz results.

    Args:
        final_score: Number of correct answers
        total_questions: Total questions asked
    """
    print("\n" + "=" * 40)
    print("QUIZ RESULTS")
    print("=" * 40)

    percentage = (final_score / total_questions) * 100
    print(f"Score: {final_score} out of {total_questions}")
    print(f"Percentage: {percentage:.1f}%")

    # SELECTION for grade message
    if percentage >= 90:
        print("Grade: A - Excellent!")
    elif percentage >= 80:
        print("Grade: B - Great job!")
    elif percentage >= 70:
        print("Grade: C - Good effort!")
    elif percentage >= 60:
        print("Grade: D - Keep studying!")
    else:
        print("Grade: F - Need more practice!")


def main():
    """Main function to run the quiz program."""
    print("=" * 40)
    print("WELCOME TO THE QUIZ GAME")
    print("=" * 40)

    # INPUT - get user's name
    player_name = input("\nWhat is your name? ")
    print(f"\nHello, {player_name}! Let's test your knowledge.")

    # INPUT - how many questions?
    print(f"\nThere are {len(quiz_data)} questions available.")
    num_q = input("How many questions would you like? ")

    # Convert to integer with error handling
    try:
        num_q = int(num_q)
    except ValueError:
        num_q = len(quiz_data)
        print(f"Invalid input, using {num_q} questions.")

    # Run the quiz using our procedure
    final_score = run_quiz(quiz_data, num_q)

    # Display results
    display_results(final_score, min(num_q, len(quiz_data)))

    # Thank the user
    print(f"\nThanks for playing, {player_name}!")


# =============================================================================
# Run the program
# =============================================================================

if __name__ == "__main__":
    main()


# =============================================================================
# CREATE TASK CHECKLIST
# =============================================================================
"""
This program includes all required elements:

✓ INPUT: Player name, number of questions, answers to quiz questions
✓ LIST: quiz_data stores multiple question/answer dictionaries
✓ LIST USAGE: Accessed with quiz_data[i] in the loop
✓ PROCEDURE: check_answer(user_response, correct_answer)
    - Has PARAMETER: user_response, correct_answer
    - Has SEQUENCING: Steps happen in order
    - Has SELECTION: if/else for correct vs incorrect
✓ PROCEDURE: run_quiz(questions_list, num_questions)
    - Has PARAMETERS
    - Has ITERATION: for loop through questions
    - Has SELECTION: if statements

For your Create Task video:
1. Show the program starting
2. Demonstrate entering your name
3. Answer a few questions (get some right, some wrong)
4. Show the final score display

For written responses:
- Explain the PURPOSE (quiz game to test knowledge)
- Explain how your ALGORITHM works (step by step)
- Explain how your LIST is used (stores questions, accessed by index)
- Describe a bug you found and fixed during development
"""
