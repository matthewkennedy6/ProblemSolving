#Return a list of primes up to n
def prime_list(n):
  primes = [1, 2, 3]

  for i in range(4, int(n)+1):
    flag = 0
    for j in range(2, int(i/2.0)+1):
      if i % j == 0:
        flag = 1
        break
    if flag == 0:
      #print("I found a new prime ", i)
      primes.append(i)

  return primes
