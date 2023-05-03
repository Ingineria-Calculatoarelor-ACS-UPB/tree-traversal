from node import Node


class Tree:
    """ Tree class for binary tree """

    def __init__(self):
        """ Constructor for Tree class """
        self.root = None

    def getRoot(self):
        """ Method for get root of the tree """
        return self.root

    def add(self, data):
        """ Method for add data to the tree """
        if self.root is None:
            self.root = Node(data)
        else:
            self._add(data, self.root)

    def _add(self, data, node):
        """Method for add data to the tree

        Args:
            data (int): data to add

        Returns:
            None
        """
        if data < node.data:
            if node.left is not None:
                self._add(data, node.left)
            else:
                node.left = Node(data)
        else:
            if node.right is not None:
                self._add(data, node.right)
            else:
                node.right = Node(data)

    def find(self, data):
        """Method for find data in the tree

        Args:
            data (int): data to find

        Returns:
            Node: node with data
        """
        if self.root is not None:
            return self._find(data, self.root)
        else:
            return None

    def _find(self, data, node):
        if data == node.data:
            return node
        elif (data < node.data and node.left is not None):
            return self._find(data, node.left)
        elif (data > node.data and node.right is not None):
            return self._find(data, node.right)

    def deleteTree(self):
        """ Method for deleting tree """
        self.root = None

    def printTree(self):
        """ Method for printing tree """
        if self.root is not None:
            self.printInorderTree(self.root)

    def printInorderTree(self, node):
        """Prints inordered traversal of the tree

        Args:
            node (Node): root node of the tree

        Returns:
            None
        """
        if node is not None:
            self.printInorderTree(node.left)
            print(str(node.data) + ' ')
            self.printInorderTree(node.right)

    def printPreorderTree(self, node):
        """Prints preorder traversal of the tree

        Args:
            node (Node): root node of the tree

        Returns:
            None
        """
        if node is not None:
            print(str(node.data) + ' ')
            self.printPreorderTree(node.left)
            self.printPreorderTree(node.right)

    def printPostorderTree(self, node):
        """Prints postorder traversal of the tree

        Args:
            node (Node): root node of the tree

        Returns:
            None
        """
        if node is not None:
            self.printPostorderTree(node.left)
            self.printPostorderTree(node.right)
            print(str(node.data) + ' ')


from random import randint
NUM_ITERATIONS = 100

def test_find():
    tree = Tree()
    for i in range(NUM_ITERATIONS):
        tree.add(i)

    for i in range(NUM_ITERATIONS):
        assert tree.find(i) is not None

    for i in range(NUM_ITERATIONS):
        assert tree.find(i + NUM_ITERATIONS) is None

def test_find_random():
    tree = Tree()
    values = []
    for i in range(NUM_ITERATIONS):
        values.append(randint(1, 100))
        tree.add(values[i])

    for i in range(len(values)):
        assert tree.find(values[i]) is not None