from typing import Optional
from tree_node import TreeNode

class Solution:
    def calcDepth(self, root, depth, depths):
        if root is None: return
        depth += 1
        
        depths.append(depth)
        
        if root.left:
            self.calcDepth(root.left, depth, depths)
        if root.right:
            self.calcDepth(root.right, depth, depths)
        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        
        depths = []
        if root.left:
            self.calcDepth(root.left, 0, depths)
        if root.right:
            self.calcDepth(root.right, 0, depths)
        
        return max(depths) + 1 if len(depths) else 1