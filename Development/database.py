import sqlite3

# Connect to SQLite database 
conn = sqlite3.connect("database.db")

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Define the SQL statements
create_activities_table = """
CREATE TABLE IF NOT EXISTS activities (
    activity_id INTEGER PRIMARY KEY,
    title TEXT CHECK (LENGTH(title) <= 30),
    description TEXT,
    tags TEXT CHECK (LENGTH(tags) <= 20),
    expense REAL,
    duration INTEGER,
    location REAL,
    min_people INTEGER,
    max_people INTEGER CHECK (max_people = -1 OR max_people > 0)
);
"""

create_users_table = """
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);
"""

# Table to store activities a user has completed
user_compeleted = """
CREATE TABLE user_activities_done (
    user_id INTEGER,
    activity_id INTEGER,
    PRIMARY KEY (user_id, activity_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (activity_id) REFERENCES activities(activity_id) ON DELETE CASCADE
); 
"""

# Table to store a user's favorite activities
user_faves = """
CREATE TABLE user_favorites (
    user_id INTEGER,
    activity_id INTEGER,
    PRIMARY KEY (user_id, activity_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (activity_id) REFERENCES activities(activity_id) ON DELETE CASCADE
);
"""


# Execute the SQL commands
cursor.execute(create_activities_table)
cursor.execute(create_users_table)

# Commit changes and close connection
conn.commit()
conn.close()


