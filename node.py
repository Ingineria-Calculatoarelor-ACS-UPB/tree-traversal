class Node:
    """ Node class for binary tree """

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def __eq__ (self, __value: object) -> bool:
        """
        Method for compare two nodes
        """
        return self.data == __value.data