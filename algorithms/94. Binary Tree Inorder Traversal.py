# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversalRe(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def helper(root,res):
            if not root:
                return 
            helper(root.left,res)
            res.append(root.val)
            helper(root.right,res)
            
        helper(root,res)
        return res
        
    def inorderTraversalIt(self, root):
        stack, res = [],[]
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res
            
