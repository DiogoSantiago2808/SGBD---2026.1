class Node:

    def __init__(self, keys=None):
        self.keys = keys or []
        self.children = []

    def find_child(self, key):
        # lógica de navegação (opcional refinar)
        pass