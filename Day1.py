def sorting(arr):
    l, m, h = 0, 0, len(arr) - 1
    
    while m <= h:
        if arr[m] == 0:
            arr[l], arr[m] = arr[m], arr[l]
            l += 1
            m += 1
        elif arr[m] == 1:
            m += 1
        else:
            arr[m], arr[h] = arr[h], arr[m]
            h -= 1
    
    return arr

arr = list(map(int, input("Enter elements (only 0, 1, 2) separated by space: ").split()))
print(sorting(arr))
