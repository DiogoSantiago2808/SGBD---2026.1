class LeafPage:

    def __init__(self, initial_records=None):
        self.records = initial_records or []
        self.capacity = 2
        self.overflow = None
        self.next_leaf = None

    def is_full(self):
        return len(self.records) >= self.capacity


    def insert(self, key):
        self.records.append(key)
        self.records.sort()

    def insert_overflow(self, key):
        if self.overflow is None:
            self.overflow = OverflowPage()

        self.overflow.insert(key)

 
    def remove(self, key):
       
        if key in self.records:
            self.records.remove(key)
            return True

       
        current = self.overflow
        while current:
            if key in current.records:
                current.records.remove(key)
                return True
            current = current.next_overflow

        return False

    
    def search(self, key):
       
        if key in self.records:
            return True

        
        current = self.overflow
        while current:
            if key in current.records:
                return True
            current = current.next_overflow

        return False


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
        
        if key in self.records:
            self.records.remove(key)
            return True

        prev = None
        current = self.overflow

        while current:
            if key in current.records:
                current.records.remove(key)

                if len(current.records) == 0:
                    if prev is None:
                        self.overflow = current.next_overflow
                    else:
                        prev.next_overflow = current.next_overflow

                return True

            prev = current
            current = current.next_overflow

        return False

    def search(self, key):
        if key in self.records:
            return True

        if self.next_overflow:
            return self.next_overflow.search(key)

        return False