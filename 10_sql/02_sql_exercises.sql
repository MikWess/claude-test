-- =============================================================================
-- SQL Practice Exercises
-- =============================================================================
-- These exercises use pure SQL syntax.
-- You can run them in:
--   1. Python using sqlite3
--   2. The sqlite3 command line tool
--   3. A SQL GUI tool like DB Browser for SQLite
-- =============================================================================


-- =============================================================================
-- SETUP: Create sample tables with data
-- =============================================================================

-- Drop tables if they exist (for clean start)
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS customers;

-- Create customers table
CREATE TABLE customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    city TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create products table
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    stock INTEGER DEFAULT 0,
    category TEXT
);

-- Create orders table (junction table with extra data)
CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    product_id INTEGER,
    quantity INTEGER NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);

-- Insert sample customers
INSERT INTO customers (name, email, city) VALUES
    ('Alice Johnson', 'alice@email.com', 'Boston'),
    ('Bob Smith', 'bob@email.com', 'New York'),
    ('Charlie Brown', 'charlie@email.com', 'Boston'),
    ('Diana Ross', 'diana@email.com', 'Chicago'),
    ('Eve Wilson', 'eve@email.com', 'New York');

-- Insert sample products
INSERT INTO products (name, price, stock, category) VALUES
    ('Laptop', 999.99, 50, 'Electronics'),
    ('Phone', 699.99, 100, 'Electronics'),
    ('Headphones', 149.99, 200, 'Electronics'),
    ('Keyboard', 79.99, 150, 'Accessories'),
    ('Mouse', 49.99, 200, 'Accessories'),
    ('Monitor', 299.99, 75, 'Electronics'),
    ('USB Cable', 9.99, 500, 'Accessories'),
    ('Webcam', 89.99, 100, 'Electronics');

-- Insert sample orders
INSERT INTO orders (customer_id, product_id, quantity) VALUES
    (1, 1, 1),  -- Alice bought 1 Laptop
    (1, 3, 2),  -- Alice bought 2 Headphones
    (2, 2, 1),  -- Bob bought 1 Phone
    (2, 4, 1),  -- Bob bought 1 Keyboard
    (2, 5, 2),  -- Bob bought 2 Mice
    (3, 1, 1),  -- Charlie bought 1 Laptop
    (3, 6, 2),  -- Charlie bought 2 Monitors
    (4, 2, 2),  -- Diana bought 2 Phones
    (5, 7, 10), -- Eve bought 10 USB Cables
    (5, 8, 1);  -- Eve bought 1 Webcam


-- =============================================================================
-- EXERCISE 1: Basic SELECT queries
-- =============================================================================

-- TODO: Select all customers
-- Expected: 5 rows with all customer information


-- TODO: Select only name and email from customers


-- TODO: Select products that cost more than $100


-- TODO: Select products in the 'Electronics' category


-- =============================================================================
-- EXERCISE 2: Filtering with WHERE
-- =============================================================================

-- TODO: Find customers from Boston


-- TODO: Find products with stock less than 100


-- TODO: Find products between $50 and $200 (inclusive)
-- Hint: Use BETWEEN or >= and <=


-- TODO: Find customers whose name contains 'son'
-- Hint: Use LIKE '%son%'


-- =============================================================================
-- EXERCISE 3: Sorting and Limiting
-- =============================================================================

-- TODO: Select all products sorted by price (highest first)


-- TODO: Select the 3 cheapest products


-- TODO: Select products sorted by category, then by price within each category


-- =============================================================================
-- EXERCISE 4: Aggregate Functions
-- =============================================================================

-- TODO: Count total number of products


-- TODO: Find the average product price


-- TODO: Find the most expensive product price


-- TODO: Find total stock across all products


-- TODO: Count products in each category
-- Hint: Use GROUP BY


-- TODO: Find the average price for each category


-- =============================================================================
-- EXERCISE 5: JOIN Queries
-- =============================================================================

-- TODO: List all orders with customer names
-- Show: order_id, customer_name, order_date


-- TODO: List all orders with customer names AND product names
-- Show: order_id, customer_name, product_name, quantity


-- TODO: List all orders with total price (price * quantity)
-- Show: order_id, customer_name, product_name, quantity, total_price


-- =============================================================================
-- EXERCISE 6: Complex Queries
-- =============================================================================

-- TODO: Find customers who have placed orders
-- (Only show each customer once)
-- Hint: Use DISTINCT


-- TODO: Find customers who have NOT placed any orders
-- Hint: Use LEFT JOIN and check for NULL


-- TODO: Find the total amount spent by each customer
-- Show: customer_name, total_spent
-- Hint: Use SUM(price * quantity) with GROUP BY


-- TODO: Find the top 3 customers by total spending


-- TODO: Find products that have never been ordered


-- =============================================================================
-- EXERCISE 7: Subqueries
-- =============================================================================

-- TODO: Find products that are more expensive than average


-- TODO: Find customers who bought the most expensive product


-- TODO: Find the category with the highest total sales
-- (sales = sum of price * quantity for all orders)


-- =============================================================================
-- EXERCISE 8: Data Modification
-- =============================================================================

-- TODO: Update the price of 'Laptop' to $899.99


-- TODO: Increase stock of all 'Accessories' by 50


-- TODO: Delete all orders with quantity less than 2


-- TODO: Add a new customer named 'Frank Miller' from 'Miami'


-- =============================================================================
-- BONUS: Advanced Queries
-- =============================================================================

-- TODO: Rank products by number of times ordered


-- TODO: Find the most popular product (most ordered)


-- TODO: Calculate the percentage of total sales for each product


-- =============================================================================
-- Verify your work
-- =============================================================================

-- Run these to check the current state of the database:
-- SELECT * FROM customers;
-- SELECT * FROM products;
-- SELECT * FROM orders;
