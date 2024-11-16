# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        def dfs(node, level):
            if not node:
                return
            if level == len(rights):
                rights.append(node.val)
            
            dfs(node.right, level + 1)
            
            dfs(node.left, level + 1)
        
        rights = []
        dfs(root, 0)
        return rights
