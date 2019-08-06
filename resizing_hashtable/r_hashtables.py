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
    print("Index: ", index, "Key: ", key)

    # get current pair at this index and create new linked pair
    currentPair = hash_table.storage[index]
    newPair = LinkedPair(key, value)

    # while bucket not empty and key of currentPair does not match passed in Key
    while currentPair is not None and currentPair.key != key:
        currentPair = currentPair.next

    if currentPair and currentPair.key == key:
        currentPair.value = value

    elif currentPair is None:
        oldPair = hash_table.storage[index]
        newPair.next = oldPair
        hash_table.storage[index] = newPair

        # delete later
        if oldPair is not None:
            print("Old Pair Value: ", oldPair.value,
                  "Old Pair Key: ", oldPair.key)
        else:
            print("Old Pair None")


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''

def hash_table_remove(hash_table, key):
    index = hash(key, hash_table.capacity)
    print("Hashed Key: ", index)

    # get current pair at this index
    currentPair = hash_table.storage[index]
    # prev = None

    if currentPair is not None:

        while currentPair is not None and currentPair.key != key:
            currentPair = currentPair.next

        if currentPair.key == key:
            hash_table.storage[index] = currentPair.next

    # set new value of key to None
    else:
        print(f"WARNING: {key} does not exist in hash table.")


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    index = hash(key, hash_table.capacity)

    # if empty bucket return none
    if not hash_table.storage[index]:
        return None

    while hash_table.storage[index] is not None:
        if hash_table.storage[index].key == key:
            return hash_table.storage[index].value

        # if not, set to .next pair
        hash_table.storage[index] = hash_table.storage[index].next


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


def hash_table_resize1(hash_table):

    filledSpots = 0
    for i in range(0, len(hash_table.storage)):
        if hash_table.storage[i] != None:
            filledSpots += 1
            # keyName = [key for (key, value) in hash_table.storage[i]]
            # print("Elem = ", keyName)
    # print("Filled = ", filledSpots)

    # check if load factor reached
    if filledSpots >= 0.7 * (hash_table.capacity):
        # create empty hash table with 2x capacity of original
        newHT = HashTable(2 * hash_table.capacity)
        # hash_table.newStorage = [None] * (2*hash_table.capacity) # double capacity

        # insert each elem in old ht storage to new ht storage
        for elem in range(len(hash_table.storage)):
            # record = hash_table.storage[elem]
            # ht, key, value
            hash_table_insert(newHT, elem, hash_table.storage[elem])

            # then set value in old ht to None
            hash_table.storage[elem] = None

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
