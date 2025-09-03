def insert_sorted(stack, element):
    if not stack or element >= stack[-1]:
        stack.append(element)
    else:
        temp = stack.pop()
        insert_sorted(stack, element)
        stack.append(temp)


def sort_stack(stack):
    if stack:
        temp = stack.pop()
        sort_stack(stack)
        insert_sorted(stack, temp)


if __name__ == "__main__":
    data = input("Enter stack elements separated by space: ").strip()
    if data:
        stack = list(map(int, data.split()))
    else:
        stack = []

    print("Original Stack:", stack)
    sort_stack(stack)
    print("Sorted Stack:", stack)
