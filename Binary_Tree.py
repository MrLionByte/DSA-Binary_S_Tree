class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.right = None
        self.left = None

class Binary_tree:
    def __init__(self, root=None) -> None:
        self.root = root

    def pre_orderTransverse(self, node, result = None):
        if result is None:
            result = []
        if node:
            result.append(node.data)
            self.pre_orderTransverse(node.left, result)
            self.pre_orderTransverse(node.right, result)
        return result
    
    def In_orderTraversal(self, node, result=None):
        if result is None:
            result = []
        if node:
            self.In_orderTraversal(node.left, result)
            result.append(node.data)
            self.In_orderTraversal(node.right, result)
        return result

    def post_orderTravesal(self, node, result=None):
        if result is None:
            result = []
        if node:
            self.post_orderTravesal(node.left, result)
            self.post_orderTravesal(node.right, result)
            result.append(node.data)
        return result

root = TreeNode('R')
Na = TreeNode('A')
Nb = TreeNode('B')
Nc = TreeNode('C')
Nd = TreeNode('D')
Ne = TreeNode('E')
Nf = TreeNode('F')
Ng = TreeNode('G')
root.left = Na
root.right = Nb
Na.left = Nc
Na.right = Nd

print("             ",root.data,"       ")
print("     ",root.left.data,"           ", root.right.data)
print(root.left.left.data, '         ',root.left.right.data,"                   ")

tree = Binary_tree(root)
print(tree.pre_orderTransverse(tree.root))
print(tree.In_orderTraversal(tree.root))
print(tree.post_orderTravesal(tree.root))

