# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_depth = 1
        depth = 1
        stack = []
        node = root

        while node:
            if node.left:
                stack.append((depth+1, node.left))
            if node.right:
                stack.append((depth+1, node.right))

            if stack:
                depth, node = stack.pop()
                if depth > max_depth:
                    max_depth = depth
            else:
                break
        return max_depth
        