""" 
If node > parent -> node insert right
IF node < parent -> node insert left

if search > node -> look on the right node
if search < node -> look on the left node
 """


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert_node(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert_node(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert_node(data)
        else:
            self.data = data

    def searchFor(self, data):
        if data < self.data:
            if self.left is None:
                return str(data) + ' not found'
            return self.left.searchFor(data)
        elif data > self.data:
            if self.right is None:
                return str(data) + ' not found'
            return self.right.searchFor(data)
        else:
            return str(self.data) + ' is found'

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()


if __name__ == '__main__':
    root = Node(27)
    root.insert_node(14)
    root.insert_node(35)
    root.insert_node(31)
    root.insert_node(10)
    root.insert_node(19)
    root.print_tree()

    print(root.searchFor(32))
    print(root.searchFor(35))
