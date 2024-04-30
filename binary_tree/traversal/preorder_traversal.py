from typing import Optional, List
from tree_node import TreeNode

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        
        result = []
        
        if root:
            result.append(root.val)
        if root.right:
            result.extend(self.preorderTraversal(root.right))
        if root.left:
            result.extend(self.preorderTraversal(root.left))
        
        
        return result