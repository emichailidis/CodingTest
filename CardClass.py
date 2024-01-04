class Card:

    def __init__(self, p1, p2):
        self._suit = p1
        self._rank = p2
        self._value = self.get_value(self._suit, self._rank)

    # Getters and Setters for parameter1
    @property
    def parameter1(self):
        return self._suit

    @parameter1.setter
    def parameter1(self, value):
        if value > Card.MAX_VALUE:
            print(f"Warning: {value} exceeds the maximum value of {Card.MAX_VALUE}")
        self._suit = value

    # Getters and Setters for parameter2
    @property
    def parameter2(self):
        return self._rank

    @parameter2.setter
    def parameter2(self, value):
        self._rank = value

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
        if self._parameter1 > Card.MAX_VALUE:
            print(f"Parameter1 exceeds the maximum value of {Card.MAX_VALUE}")

    def method2(self, name=None):
        # Example method using constants and member data
        name = name or Card.DEFAULT_NAME
        print(f"Hello, {name}!")

    def get_value(self, s, r):
        pass