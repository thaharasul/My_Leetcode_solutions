class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.freq = {}
        self.minfreq = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        value, frequency = self.cache[key]

        self.freq[frequency].remove(key)

        if not self.freq[frequency]:
            del self.freq[frequency]

            if self.minfreq == frequency:
                self.minfreq += 1

        frequency += 1
        self.cache[key] = (value, frequency)

        if frequency not in self.freq:
            self.freq[frequency] = []

        self.freq[frequency].append(key)

        return value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.cache:
            self.get(key)
            frequency = self.cache[key][1]
            self.cache[key] = (value, frequency)
            return

        if len(self.cache) == self.capacity:
            key_to_remove = self.freq[self.minfreq].pop(0)
            del self.cache[key_to_remove]

        self.cache[key] = (value, 1)

        if 1 not in self.freq:
            self.freq[1] = []

        self.freq[1].append(key)
        self.minfreq = 1
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)