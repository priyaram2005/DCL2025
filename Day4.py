def merge(arr1, arr2):
    import math
    m, n = len(arr1), len(arr2)
    gap = math.ceil((m + n) / 2)

    while gap > 0:
        i = 0
        j = gap

        while j < (m + n):
            if i < m:
                a = arr1
                ai = i
            else:
                a = arr2
                ai = i - m

            if j < m:
                b = arr1
                bj = j
            else:
                b = arr2
                bj = j - m

            if a[ai] > b[bj]:
                a[ai], b[bj] = b[bj], a[ai]

            i += 1
            j += 1

        if gap == 1:
            gap = 0
        else:
            gap = math.ceil(gap / 2)

m = int(input("Enter size of arr1: "))
arr1 = list(map(int, input("Enter elements of arr1 (space-separated): ").split()))

n = int(input("Enter size of arr2: "))
arr2 = list(map(int, input("Enter elements of arr2 (space-separated): ").split()))

merge(arr1, arr2)

print("arr1 =", arr1)
print("arr2 =", arr2)
