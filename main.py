from tree import Tree
from node import Node
import pytest

tree = Tree()

tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)
tree.printTree()

'''
bhadgshdash
'''
def test_add():
	assert 0 == 0