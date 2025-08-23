def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    prefix = strs[0]
    for s in strs[1:]:
        while s[:len(prefix)] != prefix:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

n = int(input("Enter number of strings: "))
strs = []

for i in range(n):
    strs.append(input(f"Enter string {i+1}: "))

result = longestCommonPrefix(strs)
print(f'Output: "{result}"')
