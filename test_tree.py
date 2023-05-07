import pytest 
from tree import Tree
from node import Node

@pytest.fixture
def tree():
    tree = Tree()
    tree.add(5)
    tree.add(3)
    tree.add(8)
    tree.add(1)
    tree.add(2)
    tree.add(6)
    tree.add(7)
    tree.add(9)
    return tree

def test_find1(tree):
    assert tree._find(8, tree.getRoot()) == Node(8)

def test_find2(tree):
    assert tree._find(12, tree.getRoot()) == None

