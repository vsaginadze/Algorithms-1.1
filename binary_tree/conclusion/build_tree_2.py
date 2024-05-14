class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        parent_nodes =  []
        parents = []
        parent = preorder[0]
        parent_node = TreeNode(parent)
        parent_nodes.append(parent_node)

        for node in preorder[1:]:
            tree_node = TreeNode(node)

            parent_idx = inorder.index(parent)
            node_idx = inorder.index(node)
            parents.append(parent_idx)

            if node_idx < parent_idx:
                parent_node.left = tree_node
            if node_idx > parent_idx:
                parents = sorted(parents)[::-1]
                for i in range(len(parents)):
                    if node_idx > parents[i]:
                        parent_idx = parents[i]
                        break

                for node_tree in parent_nodes:
                    if node_tree.val == inorder[parent_idx]:
                        parent_node = node_tree
                        break
                parent_node.right = tree_node
            parent = node
            if parent_node not in parent_nodes:
                parent_nodes.append(parent_node)
            parent_node = tree_node


        return parent_nodes[0]
