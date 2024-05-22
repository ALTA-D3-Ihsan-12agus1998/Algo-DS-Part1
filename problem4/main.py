def is_prime(num) :
    if num < 2 :
        return False
    for i in range(2, int(num**0.5) + 1) :
        if num % i == 0 :
            return False
    return True

def generate_primes_grid(width, height, start) :
    primes = []
    num = start
    while len(primes) < width * height :
        if is_prime(num) :
            primes.append(num)
        num += 1

    result = "\n"

    for row in range(height) :
        for col in range(width) :
            result += str(primes[row * width + col])
            if col < width - 1 :
                result += " "
        result += "\n"

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

