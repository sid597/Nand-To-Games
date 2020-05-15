class Symbol_Table():
    """
    name : identifier
    type: int, char, boolean, class_name
    kind: field, static, local, argument
    index: 0, 1, 2, 3 ....
    scope: class level, subroutine level

    Symbol Table Format : Name, type, kind, Index
    """

    def __init__(self):
        self.class_table = {'varName': {},
                            'field': 0,
                            'static': 0
                            }
        self.function_table = {'varName': {},
                               'field': 0,
                               'static': 0
                               }
        # self.current_scope = None
        # self.current = None

    def new_class_table(self):
        self.class_table = {'varName': {},
                            'local': 0,
                            'argument': 0
                            }

    def new_function_table(self):
        self.function_table = {'varName': {},
                               'field': 0,
                               'static': 0
                               }

    def add_to_class(self, data):
        """Update the data in class for var_name
        Expected data format = [name,type,kind]

        :param data: Data to be updated with
        :return:
        """
        self.class_table['varName'][data[0]] = data + [self.class_table[data[-1]]]
        self.class_table[data[-1]] += 1

    def add_to_function(self, data):
        """Update the data in class for var_name
        Expected data format = [name,type,kind]

        :param data: Data to be updated with
        :return:
        """
        self.function_table['varName'][data[0]] = data + [self.function_table[data[-1]]]
        self.function_table[data[-1]] += 1

    def find_in_class(self, vari_name):
        return self.class_table['varName'][vari_name]

    def find_in_function(self, vari_name):
        return self.function_table['varName'][vari_name]


from pprint import pprint

d = Symbol_Table()
d.new_class_table()
print d.class_table
d.add_to_class(['x', 'int', 'field'])
d.add_to_class(['y', 'int', 'field'])
pprint(d.class_table)
print d.find_in_class('x')
