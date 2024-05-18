def is_prime(numb) :
    if numb <= 1 :
        return False
    if numb <= 3 :
        return True
    if numb % 2 == 0 or numb % 3 == 0 :
        return False
    i = 5
    while i * i <= numb :
        if numb % i == 0 or numb % (i + 2) == 0 :
            return False
        i += 6
    return True

def nextprimrime(start) :
    nextprim = start + 1
    while not is_prime(nextprim) :
        nextprim += 1
    return nextprim

def generate_primes_grid(width, height, start) :
    primes = []
    current = start
    while len(primes) < width * height :
        current = nextprimrime(current)
        primes.append(current)
    
    result = ""
    for row in range(height) :
        row_primes = " ".join(f"{primes[row * width + column]:2}".strip() for column in range(width))
        result += row_primes + "\n"
    
    return result

if __name__ == "__main__":
    print(generate_primes_grid(2, 3, 13))
    """
    17 19
    23 29
    31 37
    """
    print(generate_primes_grid(5, 2, 1))
    """
    2  3  5  7 11
    13 17 19 23 29
    """