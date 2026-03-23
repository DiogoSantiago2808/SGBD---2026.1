class LeafPage:

    def __init__(self, initial_records=None):
        self.records = initial_records or []
        self.capacity = 2
        self.overflow = None
        self.next_leaf = None

    def is_full(self):
        return len(self.records) >= self.capacity

    def insert(self, key):
        # inserir ordenado
        pass

    def insert_overflow(self, key):
        if self.overflow is None:
            self.overflow = OverflowPage()

        self.overflow.insert(key)

    def remove(self, key):
        # remover da folha ou overflow
        pass

    def search(self, key):
        # procurar na folha e overflow
        pass


class OverflowPage:

    def __init__(self):
        self.records = []
        self.capacity = 2
        self.next_overflow = None

    def is_full(self):
        return len(self.records) >= self.capacity

    def insert(self, key):
        if not self.is_full():
            self.records.append(key)
        else:
            if self.next_overflow is None:
                self.next_overflow = OverflowPage()

            self.next_overflow.insert(key)

    def remove(self, key):
        pass

    def search(self, key):
        pass