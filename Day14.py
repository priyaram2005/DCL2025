from collections import defaultdict

def at_most_k_distinct(s, k):
    count = defaultdict(int)
    left = 0
    res = 0
    
    for right in range(len(s)):
        count[s[right]] += 1
        
        while len(count) > k:
            count[s[left]] -= 1
            if count[s[left]] == 0:
                del count[s[left]]
            left += 1
        
        res += (right - left + 1)
    
    return res

def substrings_with_exactly_k_distinct(s, k):
    if k > len(s):
        return 0
    return at_most_k_distinct(s, k) - at_most_k_distinct(s, k - 1)


if __name__ == "__main__":
    s = input("Enter the string: ").strip()
    k = int(input("Enter value of k: ").strip())
    result = substrings_with_exactly_k_distinct(s, k)
    print("Output: ", result)
