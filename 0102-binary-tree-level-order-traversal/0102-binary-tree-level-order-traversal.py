# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        lo = []
        q = []
        if root: q.append(root)


        while q:
            nl = []
            for _ in range(len(q)):
                node = q.pop(0)
                nl.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            lo.append(nl)
        return lo

