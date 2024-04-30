from typing import Optional, List
from tree_node import TreeNode

class Solution:
    def level_order_traversal(self, root, level, result):
        if root is None: return
        
        if len(result) == level:
            result.append([])
        
        result[level].append(root.val)
        
        self.level_order_traversal(root.left, level + 1, result)
        self.level_order_traversal(root.right, level + 1, result)
        
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        self.level_order_traversal(root, 0, result)
        
        return result