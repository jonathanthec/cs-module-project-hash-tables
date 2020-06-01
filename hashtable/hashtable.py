class HashTableEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


MIN_CAPACITY = 8


class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity if capacity > 8 else 8
        self.storage = [None] * capacity
        self.key_count = 0

    def get_num_slots(self):
        return self.capacity

    def get_load_factor(self):
        """Return the load factor for this hash table."""
        return self.key_count/self.capacity

    def fnv1(self, key):
        pass

    @staticmethod
    def djb2(key):
        k = 5381
        for x in key:
            k = ((k << 5) + ord(x))
        return k & 0xFFFFFFFF

    def hash_index(self, key):
        """Take an arbitrary key and return a valid integer index between within the storage capacity of table."""
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """Store the value with the given key. Hash collisions should be handled with Linked List Chaining."""
        index = self.hash_index(key)
        table_entry = HashTableEntry(key, value)
        if self.storage[index] is not None:
            current = self.storage[index]
            while current.next and current.key != key:
                current = current.next
            if current.key == key:
                current.value = value
            else:
                current.next = table_entry
        else:
            self.storage[index] = table_entry

        self.key_count += 1

        # if self.get_load_factor() > 0.5:
        #     self.resize(self.capacity * 2)

    def delete(self, key):
        """Remove the value stored with the given key. Print a warning if the key is not found."""
        index = self.hash_index(key)

        if self.storage[index] is None:
            print("The key is not found.")
            return

        current = self.storage[index]
        while current.next and current.key is not key:
            current = current.next
        if current.key is key:
            current.value = None

        # if self.capacity > 8 and self.get_load_factor() < 0.2:
        #     self.resize(self.capacity / 2)

    def get(self, key):
        """Retrieve the value stored with the given key. Returns None if the key is not found."""
        index = self.hash_index(key)
        if self.storage[index] is None:
            return None

        current = self.storage[index]
        while current.next and current.key != key:
            current = current.next
        if current.key == key:
            return current.value

    def resize(self, new_capacity):
        """Changes the capacity of the hash table and rehashes all key/value pairs."""
        self.capacity = new_capacity if new_capacity > 8 else 8
        new_storage = [None] * self.capacity
        for pair in self.storage:
            if pair is None:
                continue
            current_pair = pair
            while current_pair:
                index = self.hash_index(current_pair.key)
                new_storage[index] = HashTableEntry(current_pair.key, current_pair.value)
                current_pair = current_pair.next
        self.storage = new_storage


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")
    print("")

    # Test storing beyond capacity
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))
    #
    # print(ht.get_num_slots())

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")

