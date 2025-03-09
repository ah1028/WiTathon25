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


## ACTIVITIES ## 
## ADD ##
def add_activity(title, descript, pic, expen, tod, time, long, lat,  min, max, tags):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    x , y = loc #loc = tuple of location long/latitude

    cursor.execute("INSERT INTO activities (title,description, picture, expense, time_of_day, duration, longitude, latitude, min_people, max_people) VALUES (?,?,?,?,?,?,?,?,?,?);"
                   ,(title, descript, pic, expen, tod, time, long ,lat , min, max))
    conn.commit()
    conn.close()
    
    if tags is not None: ## !! FIX THIS ##
        activ_ID = cursor.lastrowid

        for tag in tags:
            connect_tag(tag, activ_ID)


## RETURN PIC ##
def activity_pic(activ_ID):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT picture FROM activities WHERE activity_id = ?", (activ_ID,))
    picture = cursor.fetchone()
    conn.close()

    return picture # could potentially return NULL


## TAGS ##
# Connect tags
def connect_tag(tag, activ_id):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT tag_id FROM tags WHERE tag_name = ?;", (tag,))
    tag_id = cursor.fetchone()

    if tag_id is None:
        cursor.execute("INSERT INTO tags (tag_name) VALUES (?);", (tag,))
        tag_id = cursor.lastrowid
    
    cursor.execute("INSERT INTO activity_tags (activity_id, tag_id) VALUES (?, ?);", tag_id, activ_id)

# Return tags
def return_tags():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Fetch all tag names
    cursor.execute("SELECT tag_name FROM tags")
    tags = [row[0] for row in cursor.fetchall()]  

    conn.close()

    return tags


