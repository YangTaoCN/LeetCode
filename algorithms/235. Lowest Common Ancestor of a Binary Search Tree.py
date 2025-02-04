# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        
        if p.val > q.val:
            p,q = q,p
         
        if p.val <= root.val <= q.val:
            return root
        elif root.val < p.val:
            return self.lowestCommonAncestor(root.right,p,q)
        elif root.val > p.val:
            return self.lowestCommonAncestor(root.left,p,q)
