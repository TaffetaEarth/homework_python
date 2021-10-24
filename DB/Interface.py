import sqlite3


def dbwork(cursor, level, connection):
    if level == 1:
        print("1. Change database")
        print("2. Edit existing database")
        print("0. Exit")
        answ = input()
        if answ.isdigit() and 0 <= int(answ) < 3:
            answ = int(answ)
            if answ == 1:
                dbwork(cursor, 2, connection)
            if answ == 2:
                dbwork(cursor, 3, connection)
            if answ == 0:
                return 0
        else:
            print("Incorrect input!")
            dbwork(cursor, 1, connection)
    if level == 2:
        print("Enter new db name:")
        dbname = input()
        connection = sqlite3.connect(dbname)
        cursor = connection.cursor()
        print("Now db is %s" % dbname)
        dbwork(cursor, 1, connection)
    if level == 3:
        print("Choose action:")
        print("1. Select\n2. Insert\n3. Delete\n4. Update\n0. Exit")
        answ = input()
        if answ.isdigit() and 0 <= int(answ) < 5:
            answ = int(answ)
            if answ == 1:
                dbwork(cursor, 4, connection)
            if answ == 2:
                dbwork(cursor, 5, connection)
            if answ == 3:
                dbwork(cursor, 6, connection)
            if answ == 4:
                dbwork(cursor, 7, connection)
            if answ == 0:
                dbwork(cursor, 1, connection)
        else:
            print("Incorrect input!")
            dbwork(cursor, 3, connection)
    if level == 4:
        print("What do you want to choose?")
        what = input()
        print("From?")
        choose_from = input()
        print("Where?")
        where = input()
        if where == "":
            cursor.execute("SELECT %s FROM %s;" % (what, choose_from))
        else:
            cursor.execute("SELECT %s FROM %s WHERE %s;" % (what, choose_from, where))
        print(cursor.fetchall())
        dbwork(cursor, 3, connection)
    if level == 5:
        where = input()
        values1 = input()
        values2 = input()
        cursor.execute("INSERT INTO %s VALUES (\"%s\", \"%s\");" % (where, values1, values2))
        connection.commit()
        dbwork(cursor, 3, connection)
    if level == 6:
        delete_from = input()
        where = input()
        cursor.execute("DELETE FROM %s WHERE %s;" % (delete_from, where))
        connection.commit()
        dbwork(cursor, 3, connection)
    if level == 7:
        table_name = input()
        set = input()
        where = input()
        cursor.execute("UPDATE %s SET %s WHERE (%s);" % (table_name, set, where))
        connection.commit()
        dbwork(cursor, 3, connection)


print("Choose db")
connection = sqlite3.connect(input())
cursor = connection.cursor()
print("You have activated user interface to connect with database. What would you do?")
if not dbwork(cursor, 1, connection):
    cursor.close()
    connection.close()
