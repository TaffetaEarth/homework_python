import xml.etree.ElementTree as et
import matplotlib.pyplot as plt

tree = et.ElementTree(file='menu.xml')
root = tree.getroot()
x = []
fig = plt.figure()
plt.ylabel("Prices")
plt.xlabel("Dishes")
for child in root:
    for grandchild in child:
        x.append([child.tag, float(grandchild.attrib['price'][1:]), grandchild.text])
print(x)
barlist = plt.bar([value[2] for value in x],
                  [value[1] for value in x])
for i in range(len(barlist)):
    if x[i][0] == "breakfast":
        barlist[i].set_color('r')
    if x[i][0] == "lunch":
        barlist[i].set_color('g')
    if x[i][0] == "dinner":
        barlist[i].set_color('b')
plt.title("Menu")
plt.grid(True)
plt.show()

