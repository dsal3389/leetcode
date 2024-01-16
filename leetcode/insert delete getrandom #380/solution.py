import random


class RandomizedSet:

    def __init__(self):
        self._data = set()
        
    def insert(self, val: int) -> bool:
        present = val in self._data
        if not present:
            self._data.add(val)
        return not present
        
    def remove(self, val: int) -> bool:
        present = val in self._data
        if present:
            self._data.remove(val)
        return present
        
    def getRandom(self) -> int:
        return random.choice(list(self._data))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
