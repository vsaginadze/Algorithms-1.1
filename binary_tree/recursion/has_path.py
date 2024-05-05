from tree_node import TreeNode
from typing import Optional

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int, sum=0) -> bool:
        if not root: return False
        
        if not root.right and not root.left: # if node is leaf check condition
            if root.val+sum == targetSum: return True
            
        return self.hasPathSum(root.right, targetSum, root.val+sum) or self.hasPathSum(root.left, targetSum, root.val+sum)
