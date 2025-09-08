from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(values):
    if not values or values[0] == "null":
        return None
    
    root = TreeNode(int(values[0]))
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        if i < len(values) and values[i] != "null":
            node.left = TreeNode(int(values[i]))
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] != "null":
            node.right = TreeNode(int(values[i]))
            queue.append(node.right)
        i += 1

    return root

def isValidBST(root, low=float("-inf"), high=float("inf")):
    if not root:
        return True
    
    if not (low < root.val < high):
        return False
    
    return (isValidBST(root.left, low, root.val) and
            isValidBST(root.right, root.val, high))

if __name__ == "__main__":
    inp = input("Enter tree as list (e.g., [2,1,3]): ")
    inp = inp.strip("[]").replace(" ", "").split(",")

    root = buildTree(inp)

    print(isValidBST(root))
