# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
            values = []
            def dfs(node):
                if node:
                    dfs(node.left)
                    values.append(node.val)
                    dfs(node.right)
            dfs(root)
            return values[k - 1]