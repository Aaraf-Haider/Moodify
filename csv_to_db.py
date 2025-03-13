import sqlite3
import csv

# Connect to the SQLite database
conn = sqlite3.connect('music_recommender.db')
cursor = conn.cursor()

# Function to import CSV data into a specified table
def import_csv_to_table(csv_file, table_name):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Skip the header row
        for row in reader:
            cursor.execute(f'INSERT INTO {table_name} ({", ".join(header)}) VALUES ({", ".join("?" for _ in header)})', row)

# Import data from CSV files
import_csv_to_table('songs.csv', 'songs')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Data imported successfully into the SQLite database.")