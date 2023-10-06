def generate_primes():
    primes = []
    for i in range(2,1000):
        if (i == 2 or i == 3 or i == 5 or i == 7) or (i%2 != 0 and i%3 != 0 and i%5 != 0 and i%7 != 0):
            primes.append(i)
    return primes

def is_prime(num):
    return (num == 2 or num == 3 or num == 5 or num == 7) or (num%2 != 0 and num%3 != 0 and num%5 != 0 and num%7 != 0)

def base4(num, numerals = ("0123")):
    return ((num == 0) and numerals[0]) or (base4(num // 4, numerals).lstrip(numerals[0]) + numerals[num % 4])

def print_result(primes):
    for i in primes:
        print(f"Prime: {i}\tBase 4: {base4(i)}\tIs base4 a prime? {is_prime(int(base4(i)))}")

primes = generate_primes()
print_result(primes)
