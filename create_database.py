
import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('music_recommender.db')
cursor = conn.cursor()

# Create the artists table
cursor.execute('''
CREATE TABLE IF NOT EXISTS artists (
    artist_id INTEGER PRIMARY KEY,
    artist_name TEXT NOT NULL
)
''')

# Create the songs table
cursor.execute('''
CREATE TABLE IF NOT EXISTS songs (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    mood TEXT,
    artist_id INTEGER,
    duration_ms INTEGER,
    FOREIGN KEY (artist_id) REFERENCES artists (artist_id)
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database and tables created successfully.")