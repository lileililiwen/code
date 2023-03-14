import sqlite3

conn = sqlite3.connect('example.db')
#mysql
#oracle
#pgsql
#sqlserver
conn.execute('''CREATE TABLE IF NOT EXISTS Users
                (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                 Name TEXT NOT NULL,
                 Age INTEGER NOT NULL,
                 Email TEXT NOT NULL);''')

conn.execute("INSERT INTO Users (Name, Age, Email) VALUES (?, ?, ?)",
             ('Alice', 23, 'alice@example.com'))
conn.execute("DELETE FROM Users WHERE Name=?", ('Alice',))
conn.execute("UPDATE Users SET Age=? WHERE Name=?", (24, 'Bob'))
result = conn.execute("SELECT * FROM Users WHERE Age >= ?", (20,))
for row in result:
    print(row)

page_size = 10
page_number = 1
result = conn.execute("SELECT * FROM Users LIMIT ? OFFSET ?",
                      (page_size, (page_number - 1) * page_size))
for row in result:
    print(row)                 
