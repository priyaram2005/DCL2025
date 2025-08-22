def reverseWords(s):
    words = s.strip().split()
    words.reverse()
    return " ".join(words)


s = input("Enter a string: ")
print(reverseWords(s))
