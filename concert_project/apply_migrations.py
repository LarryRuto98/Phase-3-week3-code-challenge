import sqlite3
import os

DB_NAME = "concerts.db"
MIGRATIONS_DIR = "migrations"

def apply_migrations():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    for filename in sorted(os.listdir(MIGRATIONS_DIR)):
        if filename.endswith(".sql"):
            with open(os.path.join(MIGRATIONS_DIR, filename), "r") as f:
                sql = f.read()
                cur.executescript(sql)
                print(f"Applied migration: {filename}")

    conn.commit()
    conn.close()
    print("All migrations applied.")

if __name__ == "__main__":
    apply_migrations()
