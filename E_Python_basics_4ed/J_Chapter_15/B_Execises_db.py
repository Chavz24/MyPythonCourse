"""Review Exercises 15.1"""

import sqlite3

# Create a new database with a table named Roster that has three
# fields: Name, Species and IQ. The Name and Species columns should
# be text fields, and the IQ column should be an integer field.

values = (
    ('Jean-Baptiste Zorg', 'Human', 122),
    ('Korben Dallas', 'Meat Popsicle', 100),
    ('Ak’not', 'Mangalore', -5)
)

with sqlite3.connect("BB_New_database.db") as connection:
    cursor = connection.cursor()
    cursor.executescript(
        """DROP TABLE IF EXISTS Roster;
            CREATE TABLE Roster(
                    Name TEXT,
                    Species TEXT,
                    IQ INT
            );"""
    )

# Populate your new table with the tuple values.

    cursor.executemany(
        "INSERT INTO Roster VALUES(?,?,?)",
        values
    )

# Update the Species of Korben Dallas to be Human.

    cursor.execute(
        "UPDATE Roster SET Species=? WHERE Name=?",
        ('Human', 'Korben Dallas')
    )
#  Display the names and IQs of everyone in the table classified as Human.

    cursor.execute(
        "SELECT Name,IQ FROM Roster WHERE Species=='Human'"
    )
    for name,iq in cursor.fetchall():
        print(f'{name} has an IQ of {iq}.')