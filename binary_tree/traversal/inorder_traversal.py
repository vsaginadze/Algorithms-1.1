from typing import Optional, List
from tree_node import TreeNode


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        
        result = []
        
        if root.left:
            result.extend(self.inorderTraversal(root.left))
        if root:
            result.append(root.val)
        if root.right:
            result.extend(self.inorderTraversal(root.right))
        
        
        
        return result