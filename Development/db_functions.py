import sqlite3

# Connect to the database
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# # Execute the query
# cursor.execute("SELECT * FROM users")

# # Fetch all rows
# users = cursor.fetchall()

# Print results

users_data = [
    ("alice@example.com", "AliceWonder", "password123"),
    ("bob@example.com", "BobBuilder", "securePass"),
    ("charlie@example.com", "CharlieBrown", "charliePass"),
    ("diana@example.com", "DianaPrince", "wonderWoman99"),
    ("eve@example.com", "EveOnline", "evePass456"),
    ("frank@example.com", "FrankCastle", "punisher001"),
    ("grace@example.com", "GraceHopper", "codingQueen"),
    ("harry@example.com", "HarryPotter", "quidditch123"),
    ("isabel@example.com", "IsabelJones", "isa2025"),
    ("jack@example.com", "JackSparrow", "blackPearl"),
]

# Execute the insert statements
for user in users_data:
    cursor.execute("INSERT INTO users (user_email, username, password) VALUES (?, ?, ?);", user)

# Commit changes
conn.commit()

# Close the connection
conn.close()
