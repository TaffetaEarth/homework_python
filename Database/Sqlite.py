import sqlite3

connection = sqlite3.connect("/home/sirius/homework_python/newdb.sqlite")
cursor = connection.cursor()
for i in range(5):
    cursor.execute('INSERT INTO Pycharm VALUES (' + str(i) + ");")
connection.commit()
cursor.close()
connection.close()
