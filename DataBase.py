import sqlite3

# Initialize database and create table if it doesn't exist
def initialize_db():
    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS conversations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            user_message TEXT,
            bot_response TEXT
        )
    """)
    conn.commit()
    conn.close()

# Save user input and bot response to the database
def save_to_db(user_message, bot_response):
    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO conversations (user_message, bot_response) VALUES (?, ?)",
                   (user_message, bot_response))
    conn.commit()
    conn.close()

# Fetch all conversations from the database
def get_all_conversations():
    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()
    cursor.execute("SELECT timestamp, user_message, bot_response FROM conversations ORDER BY timestamp")
    rows = cursor.fetchall()
    conn.close()
    return rows
