# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        def dfs(node):
            if not node: return True,0
            Lflag,lh = dfs(node.left)
            Rflag,rh = dfs(node.right)

            flag = Lflag and Rflag and abs(lh-rh) <= 1

            return flag, 1 + max(lh,rh)
        return dfs(root)[0]

