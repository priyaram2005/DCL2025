def findLeaders(arr):
    n = len(arr)
    leaders = []
    max_from_right = arr[-1]
    leaders.append(max_from_right)

    for i in range(n-2, -1, -1):
        if arr[i] >= max_from_right:
            leaders.append(arr[i])
            max_from_right = arr[i]

    leaders.reverse()
    return leaders

n = int(input("Enter size of array: "))
arr = list(map(int, input("Enter array elements: ").split()))

result = findLeaders(arr)
print("Leaders:", result)
