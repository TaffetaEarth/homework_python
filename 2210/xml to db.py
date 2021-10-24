import xml.etree.ElementTree as et
import sqlite3


connection = sqlite3.connect("xmlmenu.db")
cursor = connection.cursor()
tree = et.ElementTree(file='menu.xml')
root = tree.getroot()
for child in root:
    cursor.execute("CREATE TABLE %s (price TEXT, name TEXT);" % child.tag)
    for grandchild in child:
        cursor.execute("INSERT INTO %s (price, name) VALUES (\"%s\", \"%s\");" % (child.tag, grandchild.attrib["price"], grandchild.text))
connection.commit()
cursor.close()
connection.close()

