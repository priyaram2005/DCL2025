def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    dp = [0] * (n + 1)
    dp[0], dp[1] = 0, 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


if __name__ == "__main__":
    n = int(input('Enter limit: ').strip())
    result = fibonacci(n)

    if n > 20:  
        print(f"{float(result):.15e}")
    else:
        print(result)
