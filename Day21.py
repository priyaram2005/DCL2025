def insert_at_bottom(stack, item):
    if not stack:
        stack.append(item)
        return
    top = stack.pop()
    insert_at_bottom(stack, item)
    stack.append(top)


def reverse_stack(stack):
    if not stack:
        return
    top = stack.pop()
    reverse_stack(stack)
    insert_at_bottom(stack, top)

elements = input("Enter stack elements separated by space: ").split()
stack = [int(x) for x in elements]

print("Original Stack:", stack)
reverse_stack(stack)
print("Reversed Stack:", stack)
