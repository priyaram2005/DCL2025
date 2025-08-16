def missingNumber(arr):
    n = len(arr) + 1
    total_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return total_sum - actual_sum
    
arr = list(map(int, input('Enter an array:- ').split()))
print(missingNumber(arr))
