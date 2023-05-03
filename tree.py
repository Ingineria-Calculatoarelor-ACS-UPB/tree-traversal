<<<<<<< Updated upstream
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
        # TODO 1
        self.root = None

    def printTree(self):
        # TODO 1
        if self.root is not None:
            self._printInorderTree(self.root)

    def _printInorderTree(self, node):
        # TODO 1
        if node is not None:
            self._printInorderTree(node.left)
            print(str(node.data) + ' ')
            self._printInorderTree(node.right)

    def _printPreorderTree(self, node):
        # TODO 2
        pass

    def _printPostorderTree(self, node):
        # TODO 2
        pass


=======
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
        """ Method for find data in the tree

        Args:
            data (int): data to find
            node (Node): node in the tree

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
        """ Method to delete the entire tree """
        self.root = None

    def printTree(self):
        """ Method to print the entire tree """
        if self.root is not None:
            self._printInorderTree(self.root)

    def _printInorderTree(self, node):
        """ Method to print the tree in order

        Args:
            node (Node): node in the tree

        Returns:
            None
        """
        if node is not None:
            self._printInorderTree(node.left)
            print(str(node.data) + ' ')
            self._printInorderTree(node.right)

    def _printPreorderTree(self, node):
        """ Method to print the tree in pre-order

        Args:
            node (Node): node in the tree

        Returns:
            None
        """
        pass

    def _printPostorderTree(self, node):
        """ Method to print the tree in post-order

        Args:
            node (Node): node in the tree

        Returns:
            None
        """
        pass

class TestFindMethod(unittest.TestCase):

    def test_find_existing_value(self):
        tree = Tree()
        tree.add(5)
        tree.add(3)
        tree.add(7)
        tree.add(1)
        tree.add(4)
        tree.add(6)
        tree.add(8)

        found_node = tree.find(6)
        self.assertIsNotNone(found_node)
        self.assertEqual(found_node.data, 6)

    def test_find_non_existing_value(self):
        tree = Tree()
        tree.add(5)
        tree.add(3)
        tree.add(7)
        tree.add(1)
        tree.add(4)
        tree.add(6)
        tree.add(8)

        found_node = tree.find(10)
        self.assertIsNone(found_node)

if __name__ == "__main__":
    unittest.main()
>>>>>>> Stashed changes
