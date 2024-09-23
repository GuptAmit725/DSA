class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * 7

    def __hash(self, key):
        my_hash = 0
        for ch in key:
            my_hash = (my_hash + ord(ch)*23) % len(self.data_map)

        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ' : ', val)

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for val in self.data_map[index]:
                if val[0] == key:
                    return val[1]
        return None
    
    def keys(self):
        all_keys = []
        for pair in self.data_map:
            if pair is not None:
                for key_val in pair:
                    all_keys.append(key_val[0])
        return all_keys
    

my_hash_table = HashTable()

my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)

print(my_hash_table.keys())