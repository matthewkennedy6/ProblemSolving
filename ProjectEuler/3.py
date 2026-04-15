from eulerFunctions import *

num1 = 13195
num2 = 600851475143
primes = prime_list(10000)
#print(primes)

num1High = 0
num2High = 0

for prime in primes:
  if num1 % prime == 0:
    num1High = prime
  if num2 % prime == 0:
    num2High = prime


print(num1High)
print(num2High)
