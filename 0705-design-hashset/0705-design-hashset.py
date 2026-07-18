class MyHashSet:

    def __init__(self):
        self.hash = [ [] for _ in range (1000)]

    def add(self, key: int) -> None:
        bucket= self.hash[key % 1000]
        if key not in bucket:
            bucket.append(key)

    def remove(self, key: int) -> None:
        bucket= self.hash[key % 1000]
        if key in bucket:
            bucket.remove(key)
    def contains(self, key: int) -> bool:
        bucket= self.hash[key % 1000]
        if key in bucket:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)