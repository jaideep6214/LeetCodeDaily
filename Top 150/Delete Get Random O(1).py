import random
class RandomizedSet(object):

    def __init__(self):
        self.set = []
        self.id_map = {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.set:
            return False
        else:
            self.set.append(val)
            self.id_map[val]=len(self.set)-1
            return True
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.set:
            id_to_remove = self.id_map[val]
            last_element = self.set[-1]

            #Replace by last element
            self.id_map[last_element] = id_to_remove
            self.set[id_to_remove] = last_element

            self.set.pop()
            del(self.id_map[val])

            return True
        else:
            return False
        

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.set)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
