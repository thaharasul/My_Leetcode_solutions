# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nodes = []
        def dfs(node):
            if node:
                dfs(node.left)
                nodes.append(node)
                dfs(node.right)
        dfs(root)
        vals = sorted(n.val for n in nodes)
        for node, v in zip(nodes, vals):
            node.val = v