#a program that return prime numbers in a certain range
def generate_prime(n):
    primes = []
    is_prime = [False, False] + [True]*(n-1)
    for p in range(2,n):
        for i in range(p,n+1,p):
            is_prime[i]=False
        if is_prime[p]:
            primes.append(p)

    return primes

print(generate_prime(9))
