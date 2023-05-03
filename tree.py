from node import Node
import pytest


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
        """Method for delete tree """
        # TODO 1
        self.root = None

    def printTree(self):
        """Method for print inorder tree"""
        if self.root is not None:
            self._printInorderTree(self.root)

    def _printInorderTree(self, node):
        """Method for print inorder tree"""
        if node is not None:
            self._printInorderTree(node.left)
            print(str(node.data) + ' ')
            self._printInorderTree(node.right)

    def _printPreorderTree(self, node):
        """Method for print preorder tree"""
        if node is not None:
            print(str(node.data) + ' ')
            self._printPreorderTree(node.left)
            self._printPreorderTree(node.right)

    def _printPostorderTree(self, node):
        """Method for print postorder tree"""
        if node is not None:
            self._printPostorderTree(node.left)
            self._printPostorderTree(node.right)
            print(str(node.data) + ' ')


def test_find_existing_data():
    tree = Tree()
    tree.add(5)
    tree.add(3)
    tree.add(8)
    node = tree._find(3, tree.root)
    assert node is not None
    assert node.data == 3

def test_find_nonexistent_data():
    tree = Tree()
    tree.add(10)
    tree.add(9)
    tree.add(11)
    node = tree._find(7, tree.root)
    assert node is None
