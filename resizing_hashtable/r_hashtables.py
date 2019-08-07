# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# '''
# Fill this in

# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity


# '''
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381
    for char in string:
        hash = ((hash << 5) + hash) + ord(char)

    return hash % max


# '''
# Fill this in.

# Hint: Used the LL to handle collisions
# '''

def hash_table_insert(hash_table, key, value):
    # first resize
    # hash_table_resize(hash_table)

    # hash the key
    index = hash(key, hash_table.capacity)

    currentPair = hash_table.storage[index]
    newPair = LinkedPair(key, value)
    prevPair = None

    # bucket not empty & keys don't match
    while currentPair is not None and currentPair.key != key:
        prevPair = currentPair
        currentPair = prevPair.next

    if currentPair is not None and currentPair.key == key:
        currentPair.value = value  # update value of key

    elif currentPair is None:
        newPair.next = hash_table.storage[index]
        hash_table.storage[index] = newPair


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''

def hash_table_remove(hash_table, key):
    index = hash(key, hash_table.capacity)

    # get current pair at this index
    currentPair = hash_table.storage[index]

    if currentPair is not None:

        while currentPair is not None and currentPair.key != key:
            currentPair = currentPair.next

        if currentPair.key == key:
            # remove reference to key
            hash_table.storage[index] = currentPair.next

    else:
        print(f"WARNING: {key} does not exist in hash table.")


# '''
# Fill this in.

# Should return None if the key is not found.
# '''

def hash_table_retrieve(hash_table, key):
    index = hash(key, hash_table.capacity)
    currentPair = hash_table.storage[index]

    while currentPair is not None:
        if currentPair.key == key:
            return currentPair.value

        # if not, set to .next pair
        currentPair = currentPair.next

    # if empty bucket return none
    if hash_table.storage[index] is None:
        return None


# '''
# Fill this in
# '''

def hash_table_resize(hash_table):

    # create empty hash table with 2x capacity of original
    newHT = HashTable(2 * hash_table.capacity)

    # insert each elem in old ht storage to new ht storage
    for index in range(len(hash_table.storage)):
        currentPair = hash_table.storage[index]

        if currentPair != None:
            hash_table_insert(newHT, currentPair.key,
                              currentPair.value)  # ht, key, value
            currentPair = currentPair.next

    return newHT


def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")


Testing()
