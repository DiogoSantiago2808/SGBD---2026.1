from node import Node
from page import LeafPage

class ISAM:

    def __init__(self):
        self.root = None
        self.metrics = []

    # 🌳 Estrutura fixa (OBRIGATÓRIA DO PDF)
    def build_initial_structure(self):

        # Nível 0 (raiz)
        self.root = Node(keys=[40])

        # Nível 1
        left = Node(keys=[20, 33])
        right = Node(keys=[51, 63])

        self.root.children = [left, right]

        # Nível 2 (apontando para folhas)
        left.children = [
            LeafPage([10, 15]),
            LeafPage([20, 27]),
            LeafPage([33, 35])
        ]

        right.children = [
            LeafPage([40, 46]),
            LeafPage([51, 55]),
            LeafPage([63, 70])
        ]

    # 🔍 Navegação
    def find_leaf(self, key):
        node = self.root
        path = []

        while isinstance(node, Node):
            path.append(node)

            if key < node.keys[0]:
                node = node.children[0]
            else:
                node = node.children[1]

        return node, path

    # ➕ Inserção
    def insert(self, key):
        leaf, path = self.find_leaf(key)
        self.insert_into_leaf(leaf, key)

    def insert_into_leaf(self, leaf, key):
        if not leaf.is_full():
            leaf.insert(key)
        else:
            self.insert_overflow(leaf, key)

    def insert_overflow(self, leaf, key):
        leaf.insert_overflow(key)

    # ➖ Remoção
    def delete(self, key):
        leaf, _ = self.find_leaf(key)
        leaf.remove(key)

    # 🔎 Busca
    def search(self, key):
        leaf, path = self.find_leaf(key)
        found = leaf.search(key)

        self.calculate_cost(path)
        return found

    # 🔎 Intervalo
    def range_search(self, start, end):
        leaf, path = self.find_leaf(start)
        results = self.range_scan(leaf, start, end)

        self.calculate_cost(path)
        return results

    def range_scan(self, leaf, start, end):
        # percorrer folhas + overflow
        pass

    # 📊 Métricas
    def calculate_cost(self, path):
        cost = len(path)
        self.metrics.append(cost)

    def show_metrics(self):
        print("Custos:", self.metrics)

    # 🖨️ Debug
    def print_structure(self):
        print("Estrutura ISAM (simplificada)")