class Game21:
    # Class-level constants
    RANK = [7, 8, 9, 10, 'A', 'K', 'D', 'B']
    SUITS = {"spade": '\u2660', "Heart": '\u2665', "Diamond": '\u2666', "Clubs": '\u2663'}

    def __init__(self, p1, p2):
        self._data_list = []
        self._data_dict = {}

    # Getters and Setters for parameter1
    @property
    def parameter1(self):
        return self._parameter1

    @parameter1.setter
    def parameter1(self, value):
        if value > MyClassWithConstants.MAX_VALUE:
            print(f"Warning: {value} exceeds the maximum value of {MyClassWithConstants.MAX_VALUE}")
        self._parameter1 = value

    # Getters and Setters for parameter2
    @property
    def parameter2(self):
        return self._parameter2

    @parameter2.setter
    def parameter2(self, value):
        self._parameter2 = value

    # Getters and Setters for data_list
    @property
    def data_list(self):
        return self._data_list

    @data_list.setter
    def data_list(self, value):
        self._data_list = value

    # Getters and Setters for data_dict
    @property
    def data_dict(self):
        return self._data_dict

    @data_dict.setter
    def data_dict(self, value):
        self._data_dict = value

    def method1(self):
        # Example method using constants and member data
        if self._parameter1 > MyClassWithConstants.MAX_VALUE:
            print(f"Parameter1 exceeds the maximum value of {MyClassWithConstants.MAX_VALUE}")

    def method2(self, name=None):
        # Example method using constants and member data
        name = name or MyClassWithConstants.DEFAULT_NAME
        print(f"Hello, {name}!")


# Example usage:
obj = MyClassWithConstants(42, "example", [1, 2, 3], {"a": 1.0, "b": 2.5})
obj.method1()
obj.method2()
print(obj.parameter1)  # Access using getter
obj.parameter1 = 120  # Access using setter
print(obj.parameter1)  # Access using getter
print(obj.data_list)  # Access using getter
obj.data_list = [4, 5, 6]  # Access using setter
print(obj.data_list)  # Access using getter
