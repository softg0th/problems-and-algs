class DataTypeError:
    pass


class InputError:
    pass


class StaticArray:
    def __init__(self, dataType, length):
        self.__dataType = dataType
        self.__length = length
        self.__array = [0]*self.__length

    def len(self):
        return self.__length

    def push(self, value, index):
        if type(value) != self.__dataType:
            raise DataTypeError

        self.__array.insert(index, value)

    def pop(self, index):
        self.__array[index] = 0

    def view(self):
        print(self.__array)

