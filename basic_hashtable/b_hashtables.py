

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity


# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381
    for char in string:
        # ord returns unicode point for one-char string
        hash = ((hash << 5) + hash) + ord(char)

    return hash % max  # returns a hashed integer between 0 and max


# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):

    # hash the key, max = hash table capacity
    hashedKey = hash(key, hash_table.capacity)
    print("Hashed Key: ", hashedKey)

    # check if hashed key is already in hash table
    if hash_table.storage[hashedKey]:
        print(
            f"WARNING: {key} already exists in hash table. You are overwriting the current value.")

    # set value to the hashed key
    hash_table.storage[hashedKey] = value


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):

    # hash the key, max is hash table capacity
    hashedKey = hash(key, hash_table.capacity)

    if not hash_table.storage[hashedKey]:
        print(f"WARNING: {key} does not exist in hash table.")

    # set new value of key to None
    hash_table.storage[hashedKey] = None


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):

    # hash the key, max is hash table capacity
    hashedKey = hash(key, hash_table.capacity)

    if not hash_table.storage[hashedKey]:
        return None

    return hash_table.storage[hashedKey]


def Testing():
    ht = BasicHashTable(16)
    print(ht.storage)

    hash_table_insert(ht, "line", "Here today...\n")  # ht, key, value
    print(ht.storage)

    hash_table_remove(ht, "line")
    print(ht.storage)

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
