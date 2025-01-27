import sqlite3

DB_NAME = "concerts.db"

def get_connection():
    """Returns a connection to the database with row_factory enabled."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # Makes rows behave like dictionaries
    return conn

def execute_query(query, params=()):
    """Executes a query that modifies the database."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(query, params)
    conn.commit()
    conn.close()

def fetch_all(query, params=()):
    """Fetches all rows for a given query."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(query, params)
    rows = cur.fetchall()
    conn.close()
    return [dict(row) for row in rows]  # Convert rows to dictionaries

def fetch_one(query, params=()):
    """Fetches a single row for a given query."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(query, params)
    row = cur.fetchone()
    conn.close()
    return dict(row) if row else None  # Convert row to dictionary or return None
