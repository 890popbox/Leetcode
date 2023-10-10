# HashTable implementation, This uses a chaining implementation
# We store everything as a node with a key:value pair
# In this example we provide a key:value and use the key to figure out the hashed index.
# In a more complex version we would want to use prime numbers and other math procedures to hash an index.

class HashNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    # Creating a default HashTable with a size of 10, O(N) where N is the size given.
    # However values will just be appended to the same hash_spot if need be, think of these lists as "Buckets"
    def __init__(self, size=10):
        self.table = []
        for i in range(size):
            self.table.append([])

    # Create hash key, O(1) constant creation
    def create_hash_key(self, key):
        return int(key) % len(self.table)

    # Insert package into hash table, O(1) because we are not checking for duplicates
    def insert(self, key, value):
        key_hash = self.create_hash_key(key)
        key_value = HashNode(key, value)

        # If the list is empty, add a list with value as start
        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
        else:
            self.table[key_hash].append(key_value)

    # Get a value from hash table, Best case O(1), worse case O(N) depending on number of contents in that Bucket.
    def search(self, key):
        key_hash = self.create_hash_key(key)
        if self.table[key_hash] is not None:
            for item in self.table[key_hash]:
                if item.key == key:
                    return item.value
        return None

    # Delete a value from hash table, O(N)
    def remove(self, key):
        key_hash = self.create_hash_key(key)

        if self.table[key_hash] is None:
            return False
        for i in range(0, len(self.table[key_hash])):
            if self.table[key_hash][i].key == key:
                self.table[key_hash].pop(i)
                return True
        return False
