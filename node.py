class Node:
    """ Node class for binary tree """

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def __eq__(self, __value: object) -> bool:
        return self.data == __value.data

