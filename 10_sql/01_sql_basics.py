"""
SQL Basics with Python
======================
Learn SQL fundamentals using SQLite and Python.
"""

import sqlite3
import os

# Database file path
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'practice.db')

# =============================================================================
# LESSON: Connecting to a Database
# =============================================================================

def get_connection():
    """Create a connection to the SQLite database."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # Access columns by name
    return conn


# =============================================================================
# LESSON: Creating Tables
# =============================================================================

def create_tables():
    """Create the database tables."""
    conn = get_connection()
    cursor = conn.cursor()

    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Create posts table with foreign key
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            content TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    ''')

    conn.commit()
    conn.close()
    print("Tables created successfully!")


# =============================================================================
# LESSON: INSERT - Adding Data
# =============================================================================

def add_user(username, email):
    """Insert a new user into the database."""
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            'INSERT INTO users (username, email) VALUES (?, ?)',
            (username, email)
        )
        conn.commit()
        print(f"User '{username}' added with id {cursor.lastrowid}")
        return cursor.lastrowid
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}")
        return None
    finally:
        conn.close()


# =============================================================================
# EXERCISE 1: Insert function
# =============================================================================
# TODO: Create a function to add a post

def add_post(user_id, title, content):
    """
    Insert a new post into the database.
    Returns the post id on success, None on failure.
    """
    # TODO:
    # 1. Get connection
    # 2. Execute INSERT statement
    # 3. Commit and return the lastrowid
    # 4. Handle errors
    pass


# =============================================================================
# LESSON: SELECT - Reading Data
# =============================================================================

def get_all_users():
    """Retrieve all users from the database."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM users ORDER BY created_at DESC')
    users = cursor.fetchall()

    conn.close()
    return users


def get_user_by_id(user_id):
    """Retrieve a single user by id."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
    user = cursor.fetchone()

    conn.close()
    return user


# =============================================================================
# EXERCISE 2: Select queries
# =============================================================================
# TODO: Create functions to query data

def get_all_posts():
    """Retrieve all posts."""
    # TODO
    pass


def get_posts_by_user(user_id):
    """Retrieve all posts by a specific user."""
    # TODO
    pass


def search_posts(keyword):
    """
    Search for posts containing a keyword in title or content.
    Hint: Use LIKE '%keyword%'
    """
    # TODO
    pass


# =============================================================================
# LESSON: UPDATE - Modifying Data
# =============================================================================

def update_user_email(user_id, new_email):
    """Update a user's email address."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        'UPDATE users SET email = ? WHERE id = ?',
        (new_email, user_id)
    )
    conn.commit()

    updated = cursor.rowcount > 0
    conn.close()

    if updated:
        print(f"User {user_id} email updated to {new_email}")
    else:
        print(f"User {user_id} not found")

    return updated


# =============================================================================
# EXERCISE 3: Update function
# =============================================================================
# TODO: Create a function to update a post

def update_post(post_id, title=None, content=None):
    """
    Update a post's title and/or content.
    Only update fields that are provided (not None).
    """
    # TODO:
    # 1. Build the UPDATE query dynamically
    # 2. Only include fields that are not None
    # Hint: You can build a list of "field = ?" parts
    pass


# =============================================================================
# LESSON: DELETE - Removing Data
# =============================================================================

def delete_user(user_id):
    """Delete a user from the database."""
    conn = get_connection()
    cursor = conn.cursor()

    # First delete their posts (due to foreign key)
    cursor.execute('DELETE FROM posts WHERE user_id = ?', (user_id,))
    # Then delete the user
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))

    conn.commit()
    deleted = cursor.rowcount > 0
    conn.close()

    return deleted


# =============================================================================
# EXERCISE 4: Delete function
# =============================================================================
# TODO: Create a function to delete a post

def delete_post(post_id):
    """Delete a post by id. Returns True if deleted, False if not found."""
    # TODO
    pass


# =============================================================================
# LESSON: JOIN Queries
# =============================================================================

def get_posts_with_authors():
    """Get all posts with their author information."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT posts.*, users.username
        FROM posts
        JOIN users ON posts.user_id = users.id
        ORDER BY posts.created_at DESC
    ''')

    posts = cursor.fetchall()
    conn.close()
    return posts


# =============================================================================
# EXERCISE 5: Complex queries
# =============================================================================
# TODO: Write more complex queries

def get_user_post_count():
    """
    Get all users with their post count.
    Return: [(username, post_count), ...]
    Hint: Use GROUP BY and COUNT()
    """
    # TODO
    pass


def get_recent_posts(limit=5):
    """
    Get the most recent posts with author info.
    Include: post title, content preview (first 50 chars), username
    """
    # TODO
    pass


# =============================================================================
# LESSON: Aggregate Functions
# =============================================================================

def get_statistics():
    """Get database statistics."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT COUNT(*) FROM users')
    user_count = cursor.fetchone()[0]

    cursor.execute('SELECT COUNT(*) FROM posts')
    post_count = cursor.fetchone()[0]

    conn.close()

    return {
        'users': user_count,
        'posts': post_count,
        'avg_posts_per_user': post_count / user_count if user_count > 0 else 0
    }


# =============================================================================
# Interactive Demo
# =============================================================================

def demo():
    """Run a demo of the database functions."""
    print("=" * 50)
    print("SQL Practice Demo")
    print("=" * 50)

    # Create tables
    create_tables()

    # Add sample users
    print("\n--- Adding Users ---")
    add_user("alice", "alice@example.com")
    add_user("bob", "bob@example.com")
    add_user("charlie", "charlie@example.com")

    # Show all users
    print("\n--- All Users ---")
    for user in get_all_users():
        print(f"  {user['id']}: {user['username']} ({user['email']})")

    # Get specific user
    print("\n--- Get User by ID ---")
    user = get_user_by_id(1)
    if user:
        print(f"  Found: {user['username']}")

    # Update email
    print("\n--- Update Email ---")
    update_user_email(1, "alice.new@example.com")

    # Statistics
    print("\n--- Statistics ---")
    stats = get_statistics()
    print(f"  Users: {stats['users']}")
    print(f"  Posts: {stats['posts']}")


def reset_database():
    """Delete the database file to start fresh."""
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
        print(f"Database deleted: {DB_PATH}")
    else:
        print("No database to delete.")


if __name__ == "__main__":
    demo()

    print("\n" + "=" * 50)
    print("Complete the TODO exercises in this file!")
    print("Run reset_database() to start fresh.")
    print("=" * 50)
