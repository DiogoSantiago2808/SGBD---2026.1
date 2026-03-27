class Node:

    def __init__(self, keys=None):
        self.keys = keys or []
        self.children = []

    def find_child(self, key):
        if len(self.keys) == 1:
            if key < self.keys[0]:
                return self.children[0]
            else:
                return self.children[1]

        elif len(self.keys) == 2:
            if key < self.keys[0]:
                return self.children[0]
            elif key < self.keys[1]:
                return self.children[1]
            else:
                return self.children[2]