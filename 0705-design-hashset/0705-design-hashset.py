class MyHashSet:

    def __init__(self,size=7):
        self.size=size
        self.bucket=[[] for _ in range(size)]

    def add(self, key: int) -> None:
        b = hash(key) % self.size
        if key not in self.bucket[b]:
            self.bucket[b].append(key)

    def remove(self, key: int) -> None:
        b = hash(key) % self.size
        if key in self.bucket[b]:
            self.bucket[b].remove(key)

    def contains(self, key: int) -> bool:
        b = hash(key) % self.size
        return key in self.bucket[b] 


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)