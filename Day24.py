from collections import deque

class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

def build_tree(values):
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root

def lowestCommonAncestor(root, p, q):
    if root is None or root.val == p or root.val == q:
        return root

    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    if left and right:
        return root
    return left if left else right
    
values = input("Enter tree in level order (use 'null' for empty): ").split()
values = [int(x) if x != "null" else None for x in values]

p = int(input("Enter node p: "))
q = int(input("Enter node q: "))

root = build_tree(values)

lca = lowestCommonAncestor(root, p, q)
print("Lowest Common Ancestor:", lca.val if lca else None)
