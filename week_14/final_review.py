"""
Week 14: Final Review - Practice Questions
==========================================

A comprehensive collection of AP-style practice questions
covering all 5 Big Ideas.
"""

import random

# =============================================================================
# Practice Question Bank
# =============================================================================

QUESTIONS = [
    # AAP - Algorithms and Programming
    {
        "category": "AAP",
        "question": """
What is the output of this code?
```
x = 10
y = 3
print(x // y)
```""",
        "options": ["3.33", "3", "4", "10"],
        "answer": 1,
        "explanation": "// is floor division, which returns an integer. 10 // 3 = 3"
    },
    {
        "category": "AAP",
        "question": """
How many times does "Hi" print?
```
for i in range(2):
    for j in range(3):
        print("Hi")
```""",
        "options": ["2", "3", "5", "6"],
        "answer": 3,
        "explanation": "Outer loop runs 2 times, inner loop runs 3 times. 2 × 3 = 6"
    },
    {
        "category": "AAP",
        "question": "Which search algorithm requires a sorted list?",
        "options": ["Linear search", "Binary search", "Random search", "Sequential search"],
        "answer": 1,
        "explanation": "Binary search eliminates half the list each step, but only works on sorted lists"
    },
    {
        "category": "AAP",
        "question": """
What is the value of result?
```
nums = [1, 2, 3, 4, 5]
result = nums[2]
```""",
        "options": ["1", "2", "3", "4"],
        "answer": 2,
        "explanation": "Index 2 is the third element (0-based indexing). nums[2] = 3"
    },
    {
        "category": "AAP",
        "question": "Which time complexity is considered 'unreasonable'?",
        "options": ["O(n)", "O(n²)", "O(n log n)", "O(2^n)"],
        "answer": 3,
        "explanation": "O(2^n) is exponential and becomes impractical very quickly"
    },

    # DAT - Data
    {
        "category": "DAT",
        "question": "What is the decimal value of binary 1010?",
        "options": ["5", "8", "10", "12"],
        "answer": 2,
        "explanation": "1010 = (1×8) + (0×4) + (1×2) + (0×1) = 8 + 0 + 2 + 0 = 10"
    },
    {
        "category": "DAT",
        "question": "How many values can be represented with 4 bits?",
        "options": ["4", "8", "16", "32"],
        "answer": 2,
        "explanation": "2^4 = 16 different values (0 through 15)"
    },
    {
        "category": "DAT",
        "question": "What is lossy compression?",
        "options": [
            "Compression that can be perfectly reversed",
            "Compression that permanently removes some data",
            "Compression that only works on text",
            "Compression that increases file size"
        ],
        "answer": 1,
        "explanation": "Lossy compression (like JPEG, MP3) permanently removes data to achieve smaller size"
    },

    # CSN - Computing Systems and Networks
    {
        "category": "CSN",
        "question": "What does DNS stand for?",
        "options": [
            "Digital Network System",
            "Domain Name System",
            "Data Network Service",
            "Direct Name Server"
        ],
        "answer": 1,
        "explanation": "DNS translates domain names (like google.com) to IP addresses"
    },
    {
        "category": "CSN",
        "question": "What makes the Internet fault tolerant?",
        "options": [
            "All data is encrypted",
            "There is a central server",
            "Multiple paths exist between devices",
            "Data never gets lost"
        ],
        "answer": 2,
        "explanation": "Redundant paths mean data can be rerouted if one path fails"
    },
    {
        "category": "CSN",
        "question": "What protocol encrypts web traffic?",
        "options": ["HTTP", "HTTPS", "FTP", "TCP"],
        "answer": 1,
        "explanation": "HTTPS (HTTP Secure) encrypts data between browser and server"
    },

    # IOC - Impact of Computing
    {
        "category": "IOC",
        "question": "What is the digital divide?",
        "options": [
            "The difference between 0s and 1s in binary",
            "The gap between those with and without technology access",
            "The process of converting analog to digital",
            "The separation of data into packets"
        ],
        "answer": 1,
        "explanation": "Digital divide refers to unequal access to computing technology"
    },
    {
        "category": "IOC",
        "question": "Which is an example of PII (Personally Identifiable Information)?",
        "options": [
            "The current temperature",
            "A social security number",
            "A company's stock price",
            "The current time"
        ],
        "answer": 1,
        "explanation": "PII is data that can identify a specific individual"
    },
    {
        "category": "IOC",
        "question": "What is algorithm bias?",
        "options": [
            "When an algorithm runs slowly",
            "When an algorithm produces unfair outcomes for certain groups",
            "When an algorithm crashes",
            "When an algorithm uses too much memory"
        ],
        "answer": 1,
        "explanation": "Bias occurs when algorithms discriminate, often due to biased training data"
    },

    # CRD - Creative Development
    {
        "category": "CRD",
        "question": "What is the purpose of documentation in programming?",
        "options": [
            "To make programs run faster",
            "To explain how code works for future reference",
            "To reduce file size",
            "To encrypt the code"
        ],
        "answer": 1,
        "explanation": "Documentation helps developers understand and maintain code"
    },
    {
        "category": "CRD",
        "question": "What is iterative development?",
        "options": [
            "Writing all code at once",
            "Developing in repeated cycles of design, implement, test",
            "Only testing at the end",
            "Writing code without planning"
        ],
        "answer": 1,
        "explanation": "Iterative development builds programs through repeated cycles of improvement"
    },
]


# =============================================================================
# Quiz Functions
# =============================================================================

def run_practice_quiz(num_questions=10):
    """Run a practice quiz with random questions."""
    questions = random.sample(QUESTIONS, min(num_questions, len(QUESTIONS)))
    score = 0

    print("\n" + "="*50)
    print("AP CSP PRACTICE QUIZ")
    print("="*50)

    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i} [{q['category']}]")
        print(q["question"])
        print()
        for j, option in enumerate(q["options"]):
            print(f"  {j+1}. {option}")

        while True:
            try:
                answer = int(input("\nYour answer (1-4): ")) - 1
                if 0 <= answer <= 3:
                    break
            except ValueError:
                pass
            print("Please enter 1, 2, 3, or 4")

        if answer == q["answer"]:
            print("✓ Correct!")
            score += 1
        else:
            print(f"✗ Wrong. The answer was: {q['options'][q['answer']]}")

        print(f"Explanation: {q['explanation']}")
        input("(Press Enter to continue)")

    # Results
    percentage = (score / len(questions)) * 100
    print("\n" + "="*50)
    print("QUIZ COMPLETE")
    print("="*50)
    print(f"Score: {score}/{len(questions)} ({percentage:.0f}%)")

    if percentage >= 80:
        print("Great job! You're ready for the exam!")
    elif percentage >= 60:
        print("Good progress! Review the topics you missed.")
    else:
        print("Keep studying! Focus on areas where you struggled.")


def quiz_by_category(category):
    """Run a quiz for a specific Big Idea."""
    category_questions = [q for q in QUESTIONS if q["category"] == category]

    if not category_questions:
        print(f"No questions found for {category}")
        return

    print(f"\nQuiz for {category}")
    run_practice_quiz_with_questions(category_questions)


def run_practice_quiz_with_questions(questions):
    """Run quiz with provided questions."""
    score = 0

    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}")
        print(q["question"])
        print()
        for j, option in enumerate(q["options"]):
            print(f"  {j+1}. {option}")

        while True:
            try:
                answer = int(input("\nYour answer (1-4): ")) - 1
                if 0 <= answer <= 3:
                    break
            except ValueError:
                pass

        if answer == q["answer"]:
            print("✓ Correct!")
            score += 1
        else:
            print(f"✗ Wrong. Answer: {q['options'][q['answer']]}")
        print(f"Explanation: {q['explanation']}")

    print(f"\nScore: {score}/{len(questions)}")


# =============================================================================
# Main
# =============================================================================

if __name__ == "__main__":
    print("="*50)
    print("AP CSP Final Review Quiz")
    print("="*50)
    print("\nOptions:")
    print("1. Run full practice quiz (10 random questions)")
    print("2. Quiz by category")
    print("3. Exit")

    choice = input("\nSelect option (1-3): ")

    if choice == "1":
        run_practice_quiz()
    elif choice == "2":
        print("\nCategories:")
        print("  AAP - Algorithms and Programming")
        print("  DAT - Data")
        print("  CSN - Computing Systems and Networks")
        print("  IOC - Impact of Computing")
        print("  CRD - Creative Development")
        cat = input("Enter category: ").upper()
        quiz_by_category(cat)
    else:
        print("Good luck on the exam!")
