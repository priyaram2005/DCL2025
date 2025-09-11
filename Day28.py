class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        def isMirror(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            return a.val == b.val and isMirror(a.left, b.right) and isMirror(a.right, b.left)
        return isMirror(root.left, root.right)

def build_tree(values):
    if not values:
        return None
    nodes = [TreeNode(v) if v is not None else None for v in values]
    for i in range(len(values)):
        node = nodes[i]
        if node is not None:
            li = 2*i + 1
            ri = 2*i + 2
            if li < len(values):
                node.left = nodes[li]
            if ri < len(values):
                node.right = nodes[ri]
    return nodes[0]

sol = Solution()
print(sol.isSymmetric(build_tree([1, 2, 2, 3, 4, 4, 3])))
print(sol.isSymmetric(build_tree([1, 2, 2, None, 3, None, 3])))
print(sol.isSymmetric(build_tree([1])))
print(sol.isSymmetric(build_tree([])))
print(sol.isSymmetric(build_tree([1, 2, 2, 3, None, None, 3])))
