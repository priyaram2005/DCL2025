def prime_factorization(N):
    factors = []
    
    while N % 2 == 0:
        factors.append(2)
        N //= 2

    i = 3
    while i * i <= N:
        while N % i == 0:
            factors.append(i)
            N //= i
        i += 2

    if N > 2:
        factors.append(N)

    return factors

if __name__ == "__main__":
    N = int(input("Enter a number (≥2): "))
    print("Prime Factorization:", prime_factorization(N))
