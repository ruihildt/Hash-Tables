# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    # def _hash_djb2(self, key):
    #     '''
    #     Hash an arbitrary key using DJB2 hash

    #     OPTIONAL STRETCH: Research and implement DJB2
    #     '''
    #     pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        # Create a new linked pair
        new_linked_pair = LinkedPair(key, value)
        # Create index from the hashed key
        index = self._hash_mod(key)
        storage_index = self.storage[index]

        # Check if there is a Linked Pair List at index
        if storage_index:
            # Traverse the Linked Pair List
            while storage_index.next is not None:
                # If the new linked pair key is already present, update the value and return
                if storage_index.key == key:
                    storage_index.value == value
                    return
                # Move to the next linked pair
                storage_index = storage_index.next
            # Add the new linked pair to the end of the Linked Pair List
            storage_index.next = new_linked_pair

        # Otherwise, insert the new Linked Pair at the index
        else:
            storage_index = new_linked_pair


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # TODO
        pass


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # TODO
        # Create index from the hashed key
        index = self._hash_mod(key)
        storage_index = self.storage[index]

        # Check if there is a Linked Pair List at index
        if storage_index:
            while storage_index.next is not None:
                # If there is a corresponding key, return its value
                if storage_index.key == key:
                    return storage_index.value
                # Move to the next linked pair
                storage_index = storage_index.next

        # Check if there's something at the index
        else:
            return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # TODO
        pass



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
