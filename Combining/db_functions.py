import sqlite3
import bcrypt

## HASH PW w/bcrypt ## 
def hash_password(password):
    salt = bcrypt.gensalt()  # Generate a salt
    hashed = bcrypt.hashpw(password.encode(), salt)  # Hash the password
    return hashed

## LOGIN ## 
def login(username_input, password_input):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Fetch the hashed password for the given username
    cursor.execute("SELECT password FROM users WHERE username = ?", (username_input,))
    user = cursor.fetchone()

    conn.close()

    # check user exists
    if user is None:
        return False  

    # compare passwords
    hashed_pw = user[0]
    return bcrypt.checkpw(password_input.encode(), hashed_pw)

### SIGN UP ### 
def signup(email_input, username_input, password_input):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? OR user_email = ?", (username_input, email_input))

    user = cursor.fetchone()

    if user is None:
        hashed_pw = hash_password(password_input)

        cursor.execute("INSERT INTO users (user_email, username, password) VALUES (?, ?, ?);", (email_input,username_input,hashed_pw))
        
        conn.commit()
        conn.close()
        return True
    
    conn.close()
    return False # Username/Email already exists



