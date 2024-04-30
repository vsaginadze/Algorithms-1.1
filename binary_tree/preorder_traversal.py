from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
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