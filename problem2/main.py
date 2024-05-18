def primeX(x) :
  if x <= 0 :
    return 0
  primes = [2]
  prime1 = 3
  while len(primes) < x :
    is_prime = True
    for prime in primes :
      if prime1 % prime == 0 :
        is_prime = False
        break
    if is_prime :
      primes.append(prime1)
    prime1 += 2
  return primes[x - 1]

if __name__ == "__main__":
  print(primeX(1))  # 2
  print(primeX(5))  # 11
  print(primeX(8))  # 19
  print(primeX(9))  # 23
  print(primeX(10))  # 29