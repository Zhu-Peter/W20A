import mariadb
import dbcreds

# Create a function that will:
# Ask the user for their username and password
# Check with the DB a user with that username / password combo exist.
# Return the id of the client if they do exist
# Return None (pythons version of undefined) if they do not exist

def get_client_id():
    print("Please enter your username and password")
    username = input("Username: ")
    password = input("Password: ")
    conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password,host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
    cursor = conn.cursor()
    cursor.execute("CALL get_user(%s, %s)", (username, password))
    result = cursor.fetchone()
    conn.close()
    if result is None:
        return None
    else:
        return result
    
# Create a function that will:
# Accept a client id as an argument
# Prompt the user to type a title and content for a post
# Put that new post into the DB

def create_post(client_id):
    print("Please enter your post contnet")
    title = input("Title: ")
    content = input("Content: ")
    conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password,host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
    cursor = conn.cursor()
    cursor.execute("CALL create_post(%s, %s, %s)", (client_id, content, title))
    conn.commit()
    conn.close()

# Create a function that will:
# Retrieve all posts from the DB
# Print out each posts title and content to the console

def get_posts():
    conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password,host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
    cursor = conn.cursor()
    cursor.execute("CALL get_posts")
    result = cursor.fetchall()
    conn.close()
    for row in result:
        print(f"{row[2]}: {row[1]}")

# Create a function that will:
# Attempt to log the user in
# Loop infinitely
# Ask the user if they would like to insert a new post, read all posts or quit (select 1, 2 or 3)
# Call the correct function based on their choice

def login():
    while True:
        print("Please enter your username and password")
        username = input("Username: ")
        password = input("Password: ")
        conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password,host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()
        cursor.execute("CALL get_user(%s, %s)", (username, password))
        result = cursor.fetchone()
        conn.close()
        if result is not None:
            print("Welcome back " + username)
            
            while True:
                choice = input("Would you like to insert a new post, read all posts or quit (select 1, 2 or 3)? ")
                if choice == "1":
                    print(result)
                    create_post(result[0])
                elif choice == "2":
                    get_posts()
                elif choice == "3":
                    break
                else:
                    print("Invalid choice")
        else:
            print("Incorrect username or password")
        


login()