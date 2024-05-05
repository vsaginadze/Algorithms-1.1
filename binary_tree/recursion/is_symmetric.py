class Solution:
    def compare_subtrees(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if not left and not right: return True

        if not left or not right: return False

        if left.val != right.val: return False

        return self.compare_subtrees(left.left, right.right) and self.compare_subtrees(left.right, right.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        return self.compare_subtrees(root.left, root.right)
