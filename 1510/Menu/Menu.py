import xml.etree.ElementTree as et

tree = et.ElementTree(file='menu.xml')
root = tree.getroot()
for child in root:
    print('tag:', child.tag, 'attributes:', child.attrib)
for grandchild in child:

