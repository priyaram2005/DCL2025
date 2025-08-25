def permute_unique(s: str):
    res = []
    chars = sorted(list(s))
    used = [False] * len(chars)

    def backtrack(path):
        if len(path) == len(chars):
            res.append("".join(path))
            return
        for i in range(len(chars)):
            if used[i]:
                continue
            if i > 0 and chars[i] == chars[i - 1] and not used[i - 1]:
                continue
            used[i] = True
            path.append(chars[i])
            backtrack(path)
            path.pop()
            used[i] = False

    backtrack([])
    return res

s = input("Enter a string: ")
result = permute_unique(s)
print("All unique permutations:")
print(result)
