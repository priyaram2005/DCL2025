import math

def count_divisors(n):
    count = 0
    root = int(math.isqrt(n))
    for i in range(1, root + 1):
        if n % i == 0:
            if i * i == n:
                count += 1
            else:
                count += 2
    return count

if __name__ == "__main__":
    N = int(input("Enter a number: "))
    print(count_divisors(N))
