with open("3.inp") as f:
    lines = f.readlines()

numValues = int(lines[0])

for i in range(1, numValues):
    a, b = int(lines[i].split()[0]), int(lines[i].split()[1])
    print(a+b, " ", end="")
