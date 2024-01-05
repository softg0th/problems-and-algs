class LruCache:     # неоптимально, но кого это волнует
    def __init__(self, size):
        self.__cache = []
        self.__size = size

    def add_object(self, data):
        if len(self.__cache) >= self.__size:
            self.__cache.pop()
        self.__cache.insert(0, data)

    def remove_object(self):
        self.__cache.pop()

    def show(self):
        return self.__cache

    def left_space(self):
        return self.__size - len(self.__cache)

    def invocate(self, data):
        if data in self.__cache:
            self.__cache.remove(data)
            self.__cache.insert(0, data)
