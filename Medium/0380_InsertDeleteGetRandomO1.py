import random


class RandomizedSet(object):

    def __init__(self):
        # Create a dictionary and a list to be used by rest of the program
        self.dic = {}
        self.ls = []

    def insert(self, val):
        # If it exists insert it and return true if not present, false if it was present
        if val in self.dic:
            return False
        # The key is val, its value is the position
        self.dic[val] = len(self.ls)
        self.ls.append(val)
        return True

    def remove(self, val):
        # If it exists delete it and return true if not present, false if it was present
        if val in self.dic:
            # Swap their places
            last_val, val_index = self.ls[-1], self.dic[val]
            self.ls[-1], self.ls[val_index] = val, last_val

            # Update the dictionaries value
            self.dic[last_val] = val_index

            # Delete the last element
            self.ls.pop()
            del self.dic[val]
            return True
        return False

    def getRandom(self):
        return random.choice(self.ls)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
