class Example:
    acceptableInputs = ('test1', 'test2', 'test3')

    def __init__(self, value):
        self._value = None  # Initialize a private variable
        self.value = value  # This will call the setter method

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if value not in self.acceptableInputs:  # Some arbitrary condition
            raise ValueError("Value not valid")
        self._value = value

# This will call the setter method during instantiation
e = Example('test1')

print(e.value)

#works. allows to remove redundant input validation code in __init__statements 
