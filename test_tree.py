import pytest
from tree import Tree
from node import Node

@pytest.fixture
def tree():
    tree = Tree()
    tree.add(1)
    tree.add(2)
    tree.add(4)
    tree.add(3)
    tree.add(7)
    tree.add(5)
    tree.add(6)
    return tree


def test_find_1(tree):
    assert tree._find(3, tree.getRoot()) == Node(3)

def test_find_2(tree):
    assert tree._find(10, tree.getRoot()) == None