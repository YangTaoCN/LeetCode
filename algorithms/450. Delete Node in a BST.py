#recursive to find a node
#replace it with the right mini one

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root: 
            return root
        if root.val > key: #
            root.left = self.deleteNode(root.left, key)
        elif root.val < key: 
            root.right= self.deleteNode(root.right, key)
        else: 
            if not root.right: 
                return root.left
            if not root.left: 
                return root.right

            temp = root.right
            mini = temp.val
            while temp.left:
                temp = temp.left
                mini = temp.val
            root.val = mini # replace value
            root.right = self.deleteNode(root.right,root.val) # delete the minimum node in right subtree
        return root
