# Week 14: Create Task Prep and Final Review

**Big Ideas:** ALL (CRD, DAT, AAP, CSN, IOC)

---

## Learning Objectives

By the end of this week, you should be able to:
- Complete the Create Performance Task requirements
- Review all 5 Big Ideas
- Practice with AP-style multiple choice questions
- Feel confident for the AP exam!

---

## The Create Performance Task

### Overview
- **30% of your AP score**
- **12 hours of in-class time**
- Submit through AP Digital Portfolio by deadline

### Requirements

**1. Program Code**
Your program must include:
- **Input** from user, device, file, or other source
- **Use of a list** (or similar collection)
- **A procedure (function)** that you wrote with:
  - At least one parameter
  - An algorithm with sequencing, selection, AND iteration

**2. Video**
- Maximum 1 minute
- Show your program running
- Demonstrate input, output, and one main feature
- No voice narration required

**3. Written Responses**
Answer questions about:
- Your program's purpose and function
- How your algorithm works
- How your list is used
- Testing and debugging

### Create Task Tips

**DO:**
- Start with a clear, manageable idea
- Plan your program before coding
- Include meaningful user input
- Use a list that stores multiple elements
- Write a function with a parameter
- Comment your code
- Test thoroughly

**DON'T:**
- Make it too complex
- Use only one element in your list
- Forget to include all required elements
- Wait until the last minute
- Copy code from others

---

## Create Task Ideas

| Idea | List Usage | Function Example |
|------|------------|------------------|
| Quiz Game | Store questions/answers | `check_answer(user_input, correct)` |
| To-Do App | Store tasks | `add_task(task_list, new_task)` |
| Grade Calculator | Store grades | `calculate_average(grades)` |
| Number Guessing | Store past guesses | `give_hint(guess, target)` |
| Simple Game | Store game state | `move_player(position, direction)` |

---

## Final Review: 5 Big Ideas

### CRD: Creative Development
- How programs are designed and developed
- Collaboration and documentation
- Testing and debugging
- Using iteration in development

### DAT: Data
- Binary representation (bits, bytes)
- Data compression
- Using data to gain insight
- Metadata and data visualization

### AAP: Algorithms and Programming
- Variables and data types
- Selection (if/else) and iteration (loops)
- Lists and list operations
- Procedures and parameters
- Algorithm efficiency

### CSN: Computing Systems and Networks
- The Internet (packets, protocols, routing)
- Fault tolerance and redundancy
- Parallel and distributed computing

### IOC: Impact of Computing
- Beneficial and harmful effects
- Digital divide
- Privacy and security
- Bias in algorithms
- Legal and ethical issues

---

## Exam Format

### Multiple Choice (70%)
- **70 questions** in 2 hours
- Single-select and multiple-select
- Includes pseudocode questions
- Reference sheet provided

### Pseudocode Reminders
```
a ← b          Assignment
a = b          Equality comparison
DISPLAY(x)     Output
INPUT()        Get user input
RANDOM(a, b)   Random number a to b
list[i]        Access element (1-indexed!)
LENGTH(list)   List length
APPEND(list, x) Add to end
FOR EACH item IN list   Iterate
REPEAT n TIMES          Loop n times
REPEAT UNTIL condition  While loop
```

---

## Practice Test Strategy

1. **Read carefully** - especially pseudocode
2. **Watch for 1-indexing** - AP uses 1, Python uses 0
3. **Trace through code** - write down variable values
4. **Eliminate wrong answers**
5. **Manage time** - ~1.7 minutes per question

---

## AP-Style Practice Questions (Mixed)

### Question 1 (AAP)
```python
def mystery(lst):
    result = []
    for item in lst:
        if item % 2 == 0:
            result.append(item * 2)
    return result

print(mystery([1, 2, 3, 4, 5]))
```
What is output?
- A) [2, 4, 6, 8, 10]
- B) [4, 8]
- C) [1, 4, 3, 8, 5]
- D) [2, 4]

<details>
<summary>Answer</summary>
B) [4, 8] — Only even numbers (2, 4) are doubled
</details>

### Question 2 (DAT)
How many bits are needed to represent 26 different letters?
- A) 4
- B) 5
- C) 26
- D) 32

<details>
<summary>Answer</summary>
B) 5 — 2⁵ = 32 which is enough for 26 letters (2⁴ = 16 is not enough)
</details>

### Question 3 (CSN)
What is the main purpose of the Domain Name System (DNS)?
- A) Encrypt web traffic
- B) Translate domain names to IP addresses
- C) Compress data for faster transfer
- D) Authenticate users

<details>
<summary>Answer</summary>
B) Translate domain names to IP addresses
</details>

### Question 4 (IOC)
A company's algorithm for loan approval was found to reject applications from certain zip codes more often. This is an example of:
- A) A security vulnerability
- B) Algorithm bias
- C) Data compression
- D) Parallel processing

<details>
<summary>Answer</summary>
B) Algorithm bias — The algorithm discriminates based on location
</details>

### Question 5 (AAP)
Which algorithm has the best efficiency for searching a sorted list?
- A) Linear search O(n)
- B) Binary search O(log n)
- C) Random search O(n²)
- D) They are all the same

<details>
<summary>Answer</summary>
B) Binary search O(log n) — Much faster than linear for sorted data
</details>

---

## Final Checklist

- [ ] Understand all 5 Big Ideas
- [ ] Can write and trace Python code
- [ ] Comfortable with AP pseudocode
- [ ] Know binary/data representation
- [ ] Understand Internet protocols
- [ ] Can analyze computing impacts
- [ ] Create Task complete and submitted
- [ ] Practiced with timed multiple choice

---

## You've Got This!

You've spent 14 weeks preparing. Trust your preparation:
- Read each question carefully
- Don't spend too long on any one question
- Use process of elimination
- Stay calm and focused

Good luck on the AP CSP exam!
