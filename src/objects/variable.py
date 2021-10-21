class Variable:

    def __init__(self):
        self.type : str
        self.name : str
        self.value : float

    def set_variable_type(self, type):
        self.type = type

    def set_variable_name(self, name):
        self.name = name

    def set_variable_value(self, value):
        self.value = value

    def get_variable_type(self):
        return self.type

    def get_variable_name(self):
        return self.name

    def get_variable_value(self):
        if self.value == None:
            if self.get_variable_type == 'str':
                self.value = ""
            elif self.get_variable_type == 'float':
                self.value = 0.0
            elif self.get_variable_type == 'int':
                self.value = 0
        return self.value