# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sum = 0
        stack = []
        current = root

        while current:
            if (
                current.left and 
                current.val >= low
            ):
                stack.append(current.left)
            if (
                current.right and
                current.val <= high
            ):
                stack.append(current.right)
            
            if current.val in range(low, high+1):
                sum += current.val

            if stack:
                current = stack.pop()
            else:
                break
        return sum

        