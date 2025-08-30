import math

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

N, M = map(int, input("Enter two integers (N M): ").split())

print(lcm(N, M))
