import unittest
from node import Node
from tree import Tree

class TestTree(unittest.TestCase):
    def test_find_data_in_tree(self):
        tree = Tree()
        tree.add(5)
        tree.add(3)
        tree.add(7)
        node = tree.find(3)
        self.assertEqual(node.data, 3)

    def test_find_data_not_in_tree(self):
        tree = Tree()
        tree.add(5)
        tree.add(3)
        tree.add(7)
        node = tree.find(10)
        self.assertIsNone(node)

if __name__ == '__main__':
    unittest.main()
