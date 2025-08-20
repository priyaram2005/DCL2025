def find_zero_sum_subarrays(arr):
    n = len(arr)
    prefix_sum = 0
    hashmap = {}
    result = []

    for i in range(n):
        prefix_sum += arr[i]

        if prefix_sum == 0:
            result.append((0, i))

        if prefix_sum in hashmap:
            for start in hashmap[prefix_sum]:
                result.append((start + 1, i))

        if prefix_sum in hashmap:
            hashmap[prefix_sum].append(i)
        else:
            hashmap[prefix_sum] = [i]

    return result


if __name__ == "__main__":
    arr = list(map(int, input("Enter the array elements separated by space: ").split()))
    result = find_zero_sum_subarrays(arr)

    if result:
        print("Zero-sum subarrays (start_index, end_index):")
        print(result)
    else:
        print("No zero-sum subarray found.")
