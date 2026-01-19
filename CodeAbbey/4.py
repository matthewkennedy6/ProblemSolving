with open("4.inp") as f:
    lines = f.readlines()

numValues = int(lines[0])

for i in range(1, numValues+1):
    a, b = int(lines[i].split()[0]), int(lines[i].split()[1])
    print(min(a, b), end=" ")
