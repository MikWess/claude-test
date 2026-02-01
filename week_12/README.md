# Week 12: Databases and Web Applications

**Big Ideas:** CSN (Computing Systems and Networks), DAT (Data)

---

## Learning Objectives

By the end of this week, you should be able to:
- Understand what databases are and why they're used
- Write basic SQL queries
- Build a simple web application with Flask
- Connect a database to a web application

---

## AP CSP Concepts

### DAT-2: Databases
A **database** is an organized collection of data stored electronically.

**Why use databases?**
- Store large amounts of data efficiently
- Query and filter data quickly
- Multiple users can access simultaneously
- Data persists even when program stops

### SQL Basics
**SQL** (Structured Query Language) is used to interact with databases.

```sql
-- Create a table
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    grade INTEGER,
    gpa REAL
);

-- Insert data
INSERT INTO students (name, grade, gpa)
VALUES ('Alice', 11, 3.8);

-- Query data
SELECT * FROM students;                      -- All rows
SELECT name, gpa FROM students;              -- Specific columns
SELECT * FROM students WHERE grade = 11;     -- Filter rows
SELECT * FROM students ORDER BY gpa DESC;    -- Sort results

-- Update data
UPDATE students SET gpa = 3.9 WHERE name = 'Alice';

-- Delete data
DELETE FROM students WHERE id = 1;
```

### CRUD Operations
| Operation | SQL | Description |
|-----------|-----|-------------|
| **C**reate | INSERT | Add new records |
| **R**ead | SELECT | Retrieve records |
| **U**pdate | UPDATE | Modify records |
| **D**elete | DELETE | Remove records |

### Web Applications
A **web application** is software that runs in a web browser.

**Components:**
- **Frontend**: HTML, CSS, JavaScript (what users see)
- **Backend**: Server-side code (Python/Flask)
- **Database**: Data storage (SQLite, PostgreSQL)

### Flask Basics
```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form['name']
    return f"Hello, {name}!"

if __name__ == '__main__':
    app.run(debug=True)
```

### Connecting Flask to a Database
```python
import sqlite3

def get_students():
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    conn.close()
    return students
```

---

## Practice Files

1. **app.py** - Flask web application
2. **01_sql_basics.py** - SQL with Python
3. **02_sql_exercises.sql** - SQL practice queries
4. **templates/** - HTML templates

---

## AP-Style Practice Questions

### Question 1
Which SQL command retrieves data from a database?
- A) INSERT
- B) UPDATE
- C) SELECT
- D) DELETE

<details>
<summary>Answer</summary>
C) SELECT — SELECT queries data from tables
</details>

### Question 2
```sql
SELECT name FROM students WHERE gpa > 3.5 ORDER BY gpa DESC;
```
What does this query return?
- A) All student information
- B) Names of students with GPA above 3.5, sorted highest to lowest
- C) All students sorted by GPA
- D) The number of students with high GPAs

<details>
<summary>Answer</summary>
B) Names of students with GPA above 3.5, sorted highest to lowest
</details>

### Question 3
In a web application, which component directly interacts with the database?
- A) HTML
- B) CSS
- C) JavaScript (client-side)
- D) Server-side code (like Flask)

<details>
<summary>Answer</summary>
D) Server-side code (like Flask) — Backend code handles database operations
</details>

### Question 4
Why is it better to store user data in a database than in a text file?
- A) Text files are larger
- B) Databases allow efficient querying, filtering, and concurrent access
- C) Text files cannot store numbers
- D) Databases don't require any code to use

<details>
<summary>Answer</summary>
B) Databases allow efficient querying, filtering, and concurrent access
</details>

---

## Key Takeaways

1. Databases efficiently store and organize data
2. SQL is the language for interacting with relational databases
3. CRUD operations: Create, Read, Update, Delete
4. Web apps have frontend (browser) and backend (server) components
5. Backends handle business logic and database interactions
