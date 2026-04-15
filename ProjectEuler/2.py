num1 = 1
num2 = 1
sum = 0

while num1 < 4000000:
  if num1 % 2 == 0:
    sum += num1
  temp = num1
  num1 = num2
  num2 = temp + num1

print(sum)
