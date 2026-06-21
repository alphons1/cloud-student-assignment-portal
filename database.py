import sqlite3

def init_db():
    conn = sqlite3.connect("uploads.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS uploads (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT,
        size INTEGER,
        upload_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()

def log_upload(filename, size):
    conn = sqlite3.connect("uploads.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO uploads(filename, size)
        VALUES (?, ?)
        """,
        (filename, size)
    )

    conn.commit()
    conn.close()