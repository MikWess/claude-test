"""
Flask Web Application Practice
==============================
Learn Flask fundamentals by building a simple web app.

To run:
    pip install flask
    python app.py

Then visit: http://127.0.0.1:5000
"""

from flask import Flask, render_template, request, redirect, url_for, session, flash
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Needed for sessions/flash messages

# In-memory storage (in real apps, use a database!)
todos = []
users = {}

# =============================================================================
# LESSON: Basic Routes
# =============================================================================

@app.route('/')
def index():
    """Home page."""
    return render_template('index.html')


@app.route('/hello')
def hello():
    """Simple hello world."""
    return '<h1>Hello, World!</h1>'


@app.route('/hello/<name>')
def hello_name(name):
    """Dynamic route with URL parameter."""
    return f'<h1>Hello, {name}!</h1>'


# =============================================================================
# EXERCISE 1: Create a greeting route
# =============================================================================
# TODO: Create a route /greet that:
# - Accepts GET requests with a 'name' query parameter
# - Returns a personalized greeting
# - If no name provided, greet "Guest"

# Hint: request.args.get('name', 'Guest')

# @app.route('/greet')
# def greet():
#     pass


# =============================================================================
# LESSON: Templates
# =============================================================================

@app.route('/about')
def about():
    """Render a template."""
    return render_template('about.html', title='About Us', year=2024)


# =============================================================================
# LESSON: Forms - GET and POST
# =============================================================================

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Handle a contact form."""
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        # In real app, you'd save this or send an email
        flash(f'Thank you, {name}! We received your message.', 'success')
        return redirect(url_for('contact'))
    return render_template('contact.html')


# =============================================================================
# EXERCISE 2: Todo List
# =============================================================================
# TODO: Create routes for a todo list app

@app.route('/todos')
def todo_list():
    """Display all todos."""
    return render_template('todos.html', todos=todos)

# TODO: Add a route to add a new todo
# POST /todos/add
# Get 'task' from form data
# Append to todos list
# Redirect back to /todos

# @app.route('/todos/add', methods=['POST'])
# def add_todo():
#     pass


# TODO: Add a route to delete a todo
# POST /todos/delete/<int:index>
# Remove todo at given index
# Redirect back to /todos

# @app.route('/todos/delete/<int:index>', methods=['POST'])
# def delete_todo(index):
#     pass


# TODO: Add a route to mark todo as complete
# You might want to change todos from a list of strings
# to a list of dicts: {'task': '...', 'done': False}


# =============================================================================
# EXERCISE 3: Simple Authentication
# =============================================================================
# TODO: Create login/logout functionality

@app.route('/register', methods=['GET', 'POST'])
def register():
    """User registration."""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # TODO:
        # 1. Check if username already exists
        # 2. If not, add to users dict
        # 3. Flash success message
        # 4. Redirect to login
        flash('Registration not yet implemented!', 'info')
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """User login."""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # TODO:
        # 1. Check if username exists and password matches
        # 2. If yes, set session['user'] = username
        # 3. Redirect to dashboard
        # 4. If no, flash error message
        flash('Login not yet implemented!', 'info')
    return render_template('login.html')


@app.route('/logout')
def logout():
    """User logout."""
    session.pop('user', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))


@app.route('/dashboard')
def dashboard():
    """Protected dashboard page."""
    if 'user' not in session:
        flash('Please log in first.', 'warning')
        return redirect(url_for('login'))
    return render_template('dashboard.html', username=session['user'])


# =============================================================================
# EXERCISE 4: API Endpoint
# =============================================================================
# TODO: Create a simple JSON API

from flask import jsonify

@app.route('/api/todos')
def api_todos():
    """Return todos as JSON."""
    # TODO: Return the todos list as JSON
    # return jsonify({'todos': todos})
    pass


# TODO: Create POST /api/todos to add via JSON
# Hint: request.get_json() to get JSON body


# =============================================================================
# EXERCISE 5: Error Handlers
# =============================================================================

@app.errorhandler(404)
def not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


# TODO: Add a 500 error handler


# =============================================================================
# Run the app
# =============================================================================

if __name__ == '__main__':
    app.run(debug=True)
