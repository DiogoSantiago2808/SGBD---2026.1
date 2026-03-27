from node import Node
from page import LeafPage


class ISAM:

    def __init__(self):
        self.root = None
        self.metrics = []

    #Estrutura fixa
    def build_initial_structure(self):

        self.root = Node(keys=[40])

        left = Node(keys=[20, 33])
        right = Node(keys=[51, 63])

        self.root.children = [left, right]

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

        leaves = left.children + right.children

        for i in range(len(leaves) - 1):
            leaves[i].next_leaf = leaves[i + 1]

    def find_leaf(self, key):
        node = self.root
        path = []

        while isinstance(node, Node):
            path.append(node)

            if len(node.keys) == 1:
                if key < node.keys[0]:
                    node = node.children[0]
                else:
                    node = node.children[1]

            else:
                if key < node.keys[0]:
                    node = node.children[0]
                elif key < node.keys[1]:
                    node = node.children[1]
                else:
                    node = node.children[2]

        return node, path


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

    def delete(self, key):
        leaf, _ = self.find_leaf(key)
        leaf.remove(key)


    def search(self, key):
        leaf, path = self.find_leaf(key)
        found = leaf.search(key)

        self.calculate_cost(path)
        return found

    def range_search(self, start, end):
        leaf, path = self.find_leaf(start)
        results = self.range_scan(leaf, start, end)

        self.calculate_cost(path)
        return results

    def range_scan(self, leaf, start, end):
        results = []
        current_leaf = leaf

        while current_leaf:
        
            for key in current_leaf.records:
                if start <= key <= end:
                    results.append(key)

            
            overflow = current_leaf.overflow
            while overflow:
                for key in overflow.records:
                    if start <= key <= end:
                        results.append(key)
                overflow = overflow.next_overflow

            
            if current_leaf.records and current_leaf.records[0] > end:
                break

            current_leaf = current_leaf.next_leaf

        return sorted(results)

    def calculate_cost(self, path):
        cost = len(path)
        self.metrics.append(cost)

    def show_metrics(self):
        print("Custos:", self.metrics)

    def print_structure(self):
        print("\n======= ÁRVORE ISAM =======")

        
        print(f"\nRaiz: {self.root.keys}")

       
        left = self.root.children[0]
        right = self.root.children[1]

        print(f"\nNível 1:")
        print(f"  Esquerda: {left.keys}")
        print(f"  Direita: {right.keys}")

        print("\nFolhas:")

        
        for i, leaf in enumerate(left.children):
            print(f"  F{i+1}: {leaf.records}", end="")

            if leaf.overflow:
                print(" -> Overflow:", self._print_overflow(leaf.overflow), end="")

            print()

       
        for i, leaf in enumerate(right.children):
            print(f"  F{i+4}: {leaf.records}", end="")

            if leaf.overflow:
                print(" -> Overflow:", self._print_overflow(leaf.overflow), end="")

            print()

        print("\n============================\n")

    def _print_overflow(self, overflow):
        chain = []
        current = overflow

        while current:
            chain.append(current.records)
            current = current.next_overflow

        return " -> ".join(str(c) for c in chain)