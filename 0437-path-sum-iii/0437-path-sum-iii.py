# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        self.sum = 0
        self.res = 0
        def helper(node):
            if not node:
                return
            self.sum += node.val
            if self.sum == targetSum:
                self.res += 1

            helper(node.left)
            helper(node.right)

            self.sum -= node.val




        def dfs(node):
            if not node:
                return
            helper(node)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return self.res