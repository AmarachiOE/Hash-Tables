

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
        # ord returns unicode point/ascii value for single char
        # << or >> is binary shifting
        hash = ((hash << 5) + hash) + ord(char)

    # returns a hashed integer between 0 and max
    return hash % max


# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):

    # hash the key, max = hash table capacity
    index = hash(key, hash_table.capacity)  # where the pair object is going
    print("Hashed Key: ", index)

    # create a pair
    pair = Pair(key, value)

    # check if overwriting value with different key
    if hash_table.storage[index]:  # if not empty
        # if keys, not hashes, are different
        if hash_table.storage[index].key != key:
            print(
                f"WARNING: You're overwriting the value at {hash_table.storage[index].key}.")

    # add pair to hash table
    hash_table.storage[index] = pair


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):

    # hash the key, max is hash table capacity
    index = hash(key, hash_table.capacity)

    if not hash_table.storage[index].key:
        print(f"WARNING: {key} does not exist in hash table.")

    # set new value of key to None
    hash_table.storage[index] = None


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):

    # hash the key, max is hash table capacity
    index = hash(key, hash_table.capacity)

    # if nothing in bucket at that index, return None (no pair exists)
    if not hash_table.storage[index]:
        return None

    # if key at index pair is not the key we're looking for, return None
    if hash_table.storage[index].key != key:
        return None

    print("Index Key: ", hash_table.storage[index].key)
    print("Index Value: ", hash_table.storage[index].value)
    return hash_table.storage[index].value


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
