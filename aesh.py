import sqlite3

conn = sqlite3.connect('aesh.db')

def insertdata(col1):
    query = "INSERT INTO abc(task) VALUES(?);"
    conn.execute(query, (col1,))
    conn.commit()

def deletebyid(xyz):
    query = "DELETE FROM abc WHERE id =?;"
    conn.execute(query, (xyz,))
    conn.commit()

def updatedata(xyz, adt):
    query = "UPDATE abc SET task = ? WHERE id = ?;"
    conn.execute(query,(adt, xyz))
    conn.commit


conn.execute('''CREATE TABLE IF NOT EXISTS abc(
    id INTEGER PRIMARY KEY,
    task TEXT NOT NULL
);''')

#query = "INSERT INTO abc(col1) VALUES('Aesha Shah');"
#conn.execute(query)
#conn.commit()

insertdata("MSC in CS")
deletebyid(2)
updatedata(3, "python")

query = 'SELECT * FROM abc;'
for rows in conn.execute(query):
    print(rows)

print("Database Connected")
conn.close()