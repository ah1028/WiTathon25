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
def add_activity(title, descript, pic, expen, tod, time, loc,  min, max, tags):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    x , y = loc #loc = tuple of location long/latitude

    # takes picture location and creates BLOB
    with open(pic, "rb") as image_file:
        pic_blob = image_file.read()

    cursor.execute("INSERT INTO activities (title,description, picture, expense, time_of_day, duration, longitude, latitude, min_people, max_people) VALUES (?,?,?,?,?,?,?,?,?,?);"
                   ,(title,descript,pic_blob, expen, tod, time, x,y , min, max))


def image_to_blob(pic):
    try:
        with open(pic, "rb") as image_file:
            image_blob = image_file.read()

        return True
    except:
        return False


