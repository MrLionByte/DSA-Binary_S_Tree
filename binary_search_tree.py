class Tree:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

class Binary_search_tree:
    def __init__(self, root) -> None:
        self.root = root

    def inOrderTravesal(self, node, result = None):
        if result is None:
            result = []
        if node:
            self.inOrderTravesal(node.left, result)
            result.append(node.data)
            self.inOrderTravesal(node.right, result)
        return result

    def search_in_tree(self,node, target):
        if node is None:
            return None
        if node.data == target:
            return node.data
        elif node.data > target:
            return self.search_in_tree(node.left,target)
        else:
           return self.search_in_tree(node.right, target)
        
    def insert_new_node(self, node, Val):
        if node is None:
            node = Tree(Val)
            return  node
    
        else:
            if Val > node.data:
                print(node.right, "RIGHT")
                node.right = self.insert_new_node(node.right, Val)
                
            elif Val < node.data:
                print(node.left, "LEFT")
                node.left = self.insert_new_node(node.left, Val)
        return node
    
    def lowest(self, node):
        if node is None:
            return None
        while node.left:
            node = node.left
        return node
    
    def highest(self, node):
        if node is None:
            return None
        while node.right:
            node = node.right
        return node.data
    
    def delete_node(self, node, del_val):
        if node is None:
            return None
        if del_val < node.data:
            node.left = self.delete_node(node.left, del_val)
        elif del_val > node.data:
            node.right = self.delete_node(node.right, del_val)
        else:
            if not node.left:
                temp = node.right
                node = None
                return temp
            elif not node.right:
                temp = node.left
                node = None
                return temp
            
            node.data = self.lowest(node.right).data
            node.right = self.delete_node(node.right, node.data)
        return node
        
root = Tree(13)
node7 = Tree(7)
node15 = Tree(15)
node3 = Tree(3)
node8 = Tree(8)
node14 = Tree(14)
node19 = Tree(19)
node18 = Tree(18)

root.left = node7
root.right = node15
node7.left = node3
node7.right = node8

node15.left = node14
node15.right = node19

node19.left = node18

BST = Binary_search_tree(root)
print(BST.inOrderTravesal(BST.root))
print(BST.search_in_tree(BST.root, 18))
print(BST.insert_new_node(BST.root, 11))
print(BST.inOrderTravesal(BST.root))
print(BST.lowest(BST.root))
print(BST.highest(BST.root))
BST.delete_node(BST.root, 13)
print(BST.inOrderTravesal(BST.root))