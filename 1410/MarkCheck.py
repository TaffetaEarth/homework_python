f = open("Marks.txt", 'r')
n = int(input())
lines = f.readlines()
for line in lines:
    if line.split()[-1].isdigit():
        if int(line.split()[-1]) >= n:
            print(line[:-2:1])
    else:
        print("Incorrect data!")
