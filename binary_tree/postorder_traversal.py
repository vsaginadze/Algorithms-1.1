from typing import Optional, List
from tree_node import TreeNode
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        
        result = []
        
        if root.left:
            result.extend(self.postorderTraversal(root.left))
        if root.right:
            result.extend(self.postorderTraversal(root.right))
        if root:
            result.append(root.val)
        
        
        
        
        return result