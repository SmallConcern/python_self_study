
class HashNode(object):
    def __init__(self, key, data, next=None):
        self.key = key
        self.data = data
        self.next = next

class HashTable(object):
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.index = (0, None)

    def get(self, key, default=None):
        hash_val = self.hash(key)
        slot_node = self.slots[hash_val]
        data = None
        while slot_node and not data:
            if slot_node.key == key:
                data = slot_node.data
            else:
                slot_node = slot_node.next
        if not data and default:
            return default
        else:
            return data

    def put(self, key, data):
        hash_val = self.hash(key)
        if not self.slots[hash_val]:
            self.slots[hash_val] = HashNode(key, data)
        else:
            current = self.slots[hash_val]
            while True:
                if current.key == key:
                    current.data = data
                    break
                elif not current.next:
                    current.next = HashNode(key, data)
                    break
                current = current.next

        def remove(self, key):
            hash_val = self.hash(key)
            slot_node = self.slots[hash_val]
            previous_node = None
            found_item = False
            while slot_node and not found_item:
                if slot_node.key == key:
                    if previous_node:
                        previous_node.next = slot_node.next
                    else:
                        self.slots[hash_val] = slot_node.next
                    found_item = True
                else:
                    slot_node = slot_node.next
            if not found_item:
                raise KeyError("Key {} is not present in HashTable".format(key))

    def hash(self, key):
        s = sum([(idx+1)*ord(char) for idx, char in enumerate(key)])
        return s%self.size

    @property
    def keys(self):
        keys = []
        for x in range(0,self.size):
            current = self.slots[x]
            while current:
                keys.append(current.key)
                current = current.next
        return keys

    @property
    def values(self):
        values = []
        for x in range(0,self.size):
            current = self.slots[x]
            while current:
                values.append(current.data)
                current = current.next
        return values

    def __iter__(self):
        return self

    def next(self):
        slot_idx, slot_key = self.index
        if slot_idx == self.size and slot_key == None:
            raise StopIteration
        else:
            next_key = None
            while not next_key and slot_idx < self.size-1:
                if slot_key and slot_key.next:
                    next_key = slot_key.next
                else:
                    slot_idx += 1
                    next_key = self.slots[slot_idx]
            if not next_key:
                self.index = (0, None)
                raise StopIteration
            else:
                self.index = (slot_idx, next_key)
                return next_key.key, next_key.data


    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)
