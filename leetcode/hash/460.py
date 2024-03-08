class LFUCache:

    def __init__(self, capacity: int):
        self.cache = {}

    def get(self, key: int) -> int:
        pass

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            self.cache[key] = 1

