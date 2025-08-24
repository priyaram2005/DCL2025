from collections import defaultdict

def groupAnagrams(strs):
    anagram_map = defaultdict(list)
    
    for word in strs:
        key = ''.join(sorted(word))
        anagram_map[key].append(word)
    
    return list(anagram_map.values())

n = int(input("Enter number of strings: "))
strs = []
print("Enter the strings:")
for _ in range(n):
    strs.append(input().strip())

result = groupAnagrams(strs)
print("\nGrouped Anagrams:", result)
