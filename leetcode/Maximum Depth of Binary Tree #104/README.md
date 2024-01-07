Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:
![visual](./_images/tmp-tree.jpg)

Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 

Constraints:

* The number of nodes in the tree is in the range [0, 104].
* -100 <= Node.val <= 100

## explanation
if root is not None it means the max_depth is 1 by defult, now check if the current node have left or right, we add them both to the stack with depth+1, then we pop the last added item from the stack (if we have any), and we check if this node have a higher depth then the max_depth, if we don't have anything in our stack it means we cheked all nodes
