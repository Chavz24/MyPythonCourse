import sqlite3

connection = sqlite3.connect('AA_Test_database.db')
cursor = connection.cursor()
query = "Select datetime('now','localtime')"  # Returns a tuple with the localtime.
time = cursor.execute(query).fetchone()[0]
connection.close()

# Same example using with statement.

with sqlite3.connect('AA_Test_database.db') as connection:
    cursor = connection.cursor()
    query = "Select datetime('now','localtime')"
    time = cursor.execute(query).fetchone()[0]

# Creating tables an inserting values to them in a database.

with sqlite3.connect('AA_Test_database.db') as connection:
    cursor = connection.cursor()
    cursor.execute("""DROP TABLE IF EXISTS People;""")
    cursor.execute(
        """CREATE TABLE People(
                FirstName TEXT,
                LastName TEXT,
                Age INT
            );"""
    )
    cursor.execute(
        """INSERT INTO People VALUES(
                'Mikolas',
                'Rhevrara',
                50
            );"""
    )

cursor.execute("SELECT * FROM People;")
name, last_name, age = cursor.fetchone()

# Executing multiple SQL statements.

with sqlite3.connect("AA_Test_database.db") as connection:
    cursor = connection.cursor()
    cursor.executescript(
        """DROP TABLE IF EXISTS People;
            CREATE TABLE People(
                FirstName TEXT,
                Lastname TEXT,
                Age INT
            );
            INSERT INTO People VALUES(
                'Michel',
                'Elbuenon',
                '45'
            );"""
    )
cursor.execute("SELECT * FROM People;")
# name, last_name, age = cursor.fetchone()


# Inserting many values at once

people_values = (
    ("Michel", "Elbuenon", 45),
    ("Ros", "Weon", 50),
    ("Raquel", "Laquez", 24)
)
with sqlite3.connect("AA_Test_database.db") as connection:
    cursor = connection.cursor()
    cursor.executescript(
        """DROP TABLE IF EXISTS People;
            CREATE TABLE People(
                    FirstName TEXT,
                    LastName TEXT,
                    Age
            );"""
    )
    # Inserting all the values in the tuple 'people_values'
    cursor.executemany(
        "INSERT INTO People VALUES(?,?,?);",
        people_values
    )
    # Updating a value in the table
    cursor.execute(
        "UPDATE People SET Age=? WHERE FirstName=? AND LastName=?",
        (100, 'Michel', 'Elbuenon')
    )

# Retrieving data from db

people = (
    ("Michel", "Elbuenon", 45),
    ("Ros", "Weon", 50),
    ("Raquel", "Laquez", 24),
    ("Michelito", "Elbuenon", 20),
    ("Rosy", "Weon", 10),
    ("Raquelita", "Laquez", 24)
)

with sqlite3.connect("AA_Test_database.db") as connection:
    cursor = connection.cursor()
    cursor.executescript(
        """DROP TABLE IF EXISTS People;
            CREATE TABLE People(
                FirstName TEXT,
                LastName TEXT,
                Age INT
            );"""
    )
    cursor.executemany(
        "INSERT INTO People VALUES(?,?,?);",
        people
    )
    cursor.execute(
        "SELECT FirstName,LastName FROM People WHERE Age<35"
    )
    for cursor in cursor.fetchall():
        print(cursor)
