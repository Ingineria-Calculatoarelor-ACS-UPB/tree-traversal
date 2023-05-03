from node import Node
import unittest


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
        """Method for find data in the tree

        Args:
            data (int): data to find

        Returns:
            Node: node with data
        """
        if data == node.data:
            return node
        elif (data < node.data and node.left is not None):
            return self._find(data, node.left)
        elif (data > node.data and node.right is not None):
            return self._find(data, node.right)

    def deleteTree(self):
        """Method for find data in the tree

        Args:
            data (int): data to find

        Returns:
            Node: node with data
        """
        self.root = None

    def printTree(self):
        """Method for find data in the tree

        Args:
            data (int): data to find

        Returns:
            Node: node with data
        """
        if self.root is not None:
            self._printInorderTree(self.root)

    def _printInorderTree(self, node):
        """Method for find data in the tree

        Args:
            data (int): data to find

        Returns:
            Node: node with data
        """
        if node is not None:
            self._printInorderTree(node.left)
            print(str(node.data) + ' ')
            self._printInorderTree(node.right)

    def _printPreorderTree(self, node):
        # TODO 2
        """Method for find data in the tree

        Args:
            data (int): data to find

        Returns:
            Node: node with data
        """
        if node is not None:
            print(str(node.data) + ' ')
            self._printInorderTree(node.left)
            self._printInorderTree(node.right)

    def _printPostorderTree(self, node):
        # TODO 2
        """Met/rizeuscu/tree-traversal/actionshod for find data in the tree

        Args:
            data (int): data to find

        Returns:
            Node: node with data
        """
        if node is not None:
            self._printInorderTree(node.left)
            self._printInorderTree(node.right)
            print(str(node.data) + ' ')

class TestTree(unittest.TestCase):
    """ Test class for Tree class """
    
    def test__find(self):
        """ Method for test find method """
        tree = Tree()
        tree.add(3)
        tree.add(4)
        tree.add(0)
        tree.add(8)
        tree.add(2)
        assert tree._find(3, tree.root).data == 3
        assert tree._find(4, tree.root).data == 4
        assert tree._find(0, tree.root).data == 0
        assert tree._find(8, tree.root).data == 8
        assert tree._find(2, tree.root).data == 2
    
    def test__find_2(self):
        """ Method for test find method """
        tree = Tree()
        tree.add(2)
        tree.add(1)
        tree.add(4)
        tree.add(5)
        tree.add(0)
        assert tree._find(2, tree.root).data == 2
        assert tree._find(1, tree.root).data == 1
        assert tree._find(4, tree.root).data == 4
        assert tree._find(5, tree.root).data == 5
        assert tree._find(0, tree.root).data == 0


