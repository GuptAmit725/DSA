class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
        else:
            temp = self.root
            while (True):
                if new_node.value == temp.value:
                    return False
                if new_node.value < temp.value:
                    if temp.left == None:
                        temp.left = new_node
                        return True
                    temp = temp.left
                else:
                    if temp.right == None:
                        temp.right = new_node
                        return True
                    temp = temp.right

    def contains(self, value):
        new_node = Node(value)
        if self.root is None:
            return False
        else:
            temp = self.root
            while temp is not None:
                if new_node.value < temp.value:
                    temp = temp.left
                elif new_node.value > temp.value:
                    temp = temp.right
                else:
                    return True
            return False
            

                


tree = BinarySearchTree()

tree.insert(345)
tree.insert(100)
tree.insert(400)

print(f'Left node value: {tree.root.left.value}')
print(f'Root node value: {tree.root.value}')
print(f'Right node value: {tree.root.right.value}')

print(tree.contains(1000))