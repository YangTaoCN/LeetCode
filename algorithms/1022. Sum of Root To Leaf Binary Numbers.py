This is a dfs problem.

From the root to the leaf, each layer we need to use the result * 2 and add the value of this node.

Start from the 0 at the root of the tree.

if not root, we do not need to add anything we just need to add number at the leaf.



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(node,cur):
            if not node:
                return 
            if not node.left and not node.right:
                cur = 2 * cur + node.val
                self.res += cur
                # return
            dfs(node.left,2 * cur + node.val)
            dfs(node.right,2 * cur + node.val)
        dfs(root,0)
        return self.res
