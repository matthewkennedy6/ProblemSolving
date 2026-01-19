with open("5.inp") as f:
    lines = f.readlines()

numValues = int(lines[0])

for i in range(1, numValues+1):
    a, b, c = int(lines[i].split()[0]), int(lines[i].split()[1]), int(lines[i].split()[2])
    print(min(min(a, b), c), end=" ")
