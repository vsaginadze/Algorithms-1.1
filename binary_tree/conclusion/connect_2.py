class Solution:
    def level_order_traversal(self, root, level, result):
        if root is None: return

        if len(result) == level:
            result.append([])

        result[level].append(root)

        self.level_order_traversal(root.left, level + 1, result)
        self.level_order_traversal(root.right, level + 1, result)

    def connect(self, root: 'Node') -> 'Node':
        if root is None: return None
        result = []
        self.level_order_traversal(root, 0, result)

        for lst in result:
            for i in range(len(lst)):
                if i+1 != len(lst):
                    lst[i].next = lst[i+1]
                else:
                    lst[i].next = None

        return result[0][0]
