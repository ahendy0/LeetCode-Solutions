# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        
        while root:
            if not root.left:
                root = root.right
            else:
                l = root.left
                while l.right:
                    l = l.right
                l.right = root.right
                root.right = root.left
                root.left = None
                
                
            