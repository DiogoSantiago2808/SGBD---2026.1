from node import Node
from page import LeafPage


class ISAM:

    def __init__(self):
        self.root = None
        self.metrics = []
        self.removidos_count = 0

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
        if leaf.remove(key):
            self.removidos_count += 1


    def search(self, key):
        leaf, path = self.find_leaf(key)
        found = leaf.search(key)
        
        # Na busca simples, acessamos a folha (+1) 
        # e percorremos os overflows até achar ou acabar a lista
        extra_cost = 1
        current_ov = leaf.overflow
        while current_ov:
            extra_cost += 1
            if key in current_ov.records:
                break
            current_ov = current_ov.next_overflow
            
        self.calculate_cost(path, extra=extra_cost)
        return found

    def range_search(self, start, end):
        leaf, path = self.find_leaf(start)
        results, scan_cost = self.range_scan(leaf, start, end)

        self.calculate_cost(path, extra=scan_cost)
        return results

    def range_scan(self, leaf, start, end):
        results = []
        scan_cost = 0
        current_leaf = leaf

        while current_leaf:
            scan_cost += 1
            
            for key in current_leaf.records:
                if start <= key <= end:
                    results.append(key)

            overflow = current_leaf.overflow
            while overflow:
                scan_cost += 1
                for key in overflow.records:
                    if start <= key <= end:
                        results.append(key)
                overflow = overflow.next_overflow

            if current_leaf.records and current_leaf.records[0] > end:
                break

            current_leaf = current_leaf.next_leaf

        return sorted(results), scan_cost

    def calculate_cost(self, path, extra=0):
        cost = len(path) + extra
        self.metrics.append(cost)

    def show_metrics(self):
        paginas_primarias = 6
        total_overflow = 0
        folhas = self.root.children[0].children + self.root.children[1].children

        for leaf in folhas:
            current_ov = leaf.overflow
            while current_ov:
                total_overflow += 1
                current_ov = current_ov.next_overflow
        tamanho_medio = total_overflow / paginas_primarias

        print(f"1. Quantidade de páginas folha primárias: {paginas_primarias}")
        print(f"2. Quantidade de páginas de overflow: {total_overflow}")
        print(f"3. Tamanho médio das cadeias de overflow: {tamanho_medio:.2f}")
        print(f"4. Quantidade de registros removidos: {self.removidos_count}")

        if self.metrics:
            custo_medio = sum(self.metrics) / len(self.metrics)
            print(f"5. Custo médio das buscas: {custo_medio:.2f} nós/páginas")
        else:
            print("5. Custo médio das buscas: Nenhuma busca realizada ainda.")

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