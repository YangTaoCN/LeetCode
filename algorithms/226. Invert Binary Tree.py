# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        root.left ,root.right = self.invertTree(root.right),self.invertTree(root.left)
        return root
        
    # BFS
    def invertTree2(self, root):
        queue = collections.deque([(root)])
        while queue:
            node = queue.popleft()
            if node:
                node.left, node.right = node.right, node.left
                queue.append(node.left)
                queue.append(node.right)
        return root

      # DFS
      def invertTree(self, root):
          stack = [root]
          while stack:
              node = stack.pop()
              if node:
                  node.left, node.right = node.right, node.left
                  stack.extend([node.right, node.left])
          return root    
        
        

        
