f = open('1.txt', 'w')
f.write("New first string!\n")
f = open('1.txt', 'a')
f.write("New second string!")
f = open('1.txt', 'r')
print(f.read())
print(f.readline())
f = open('2.txt', 'w')
f.write('Yay, new file!!!')
f = open('2.txt', 'r')
print(f.readlines())
f = open('1.txt', 'r')
while True:
    line = f.readline()
    print(line)
    if not line:
        break
lines = f.readlines()
for i in lines:
    print(i)
for line in f:

