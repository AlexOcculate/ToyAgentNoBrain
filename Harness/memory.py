# Line 1:  Define the Memory class for persistent key-value storage.
class Memory:
    # Line 2:  Constructor that initializes an empty dictionary for storage.
    def __init__(self):
        # Line 3:  Dictionary to hold stored data.
        self._store = {}

    # Line 4:  Method to store a value under a specific key.
    def store(self, key: str, value: str):
        # Line 5:  Assign the value to the key in the internal dictionary.
        self._store[key] = value

    # Line 6:  Method to recall a value by its key.
    def recall(self, key: str):
        # Line 7:  Return the value if key exists, otherwise None.
        return self._store.get(key, None)

    # Line 8:  Method to list all keys currently in memory.
    def list_keys(self):
        # Line 9:  Return a list of all keys in the store.
        return list(self._store.keys())
