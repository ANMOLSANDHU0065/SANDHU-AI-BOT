import sqlite3
from pathlib import Path
from flask import current_app

def get_connection():
    db_path = Path(current_app.config["DATABASE_PATH"])
    db_path.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(db_path)
    connection.row_factory = sqlite3.Row
    return connection

def init_db():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT NOT NULL,
                role TEXT NOT NULL CHECK(role IN ('user', 'assistant')),
                message TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.execute("""
            CREATE INDEX IF NOT EXISTS idx_messages_session
            ON messages(session_id, id)
        """)

def save_message(session_id, role, message):
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO messages (session_id, role, message) VALUES (?, ?, ?)",
            (session_id, role, message),
        )

def get_messages(session_id, limit=50):
    with get_connection() as conn:
        rows = conn.execute(
            """SELECT role, message, created_at FROM messages
               WHERE session_id = ? ORDER BY id DESC LIMIT ?""",
            (session_id, limit),
        ).fetchall()
    return [dict(row) for row in reversed(rows)]

def clear_messages(session_id):
    with get_connection() as conn:
        conn.execute("DELETE FROM messages WHERE session_id = ?", (session_id,))
