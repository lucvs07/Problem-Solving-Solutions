# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #Solving by recursion
        def depthFirstSearch(root):
            if not root:
                return 0, None
            left = depthFirstSearch(root.left)
            right = depthFirstSearch(root.right)

            if left[0] > right[0]:
                return left[0] + 1, left[1]
            if left[0] < right [0]:
                return right[0] + 1, right[1]
            return left[0] + 1, root
        return depthFirstSearch(root)[1]
            
