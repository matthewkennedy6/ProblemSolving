with open("2.inp") as f:
    lines = f.readlines()

numValues = int(lines[0])
values = lines[1].strip().split()
sum = 0
for i in range(numValues):
    sum += int(values[i])

print(sum)
