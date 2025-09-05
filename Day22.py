from collections import Counter

def first_element_k_times(arr, k):
    freq = Counter(arr)
    
    for num in arr:
        if freq[num] == k:
            return num
    return -1

arr = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter k: "))

result = first_element_k_times(arr, k)
print(result)
