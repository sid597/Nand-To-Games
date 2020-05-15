"""

First implement the terminal commands
Tokens tags :

<keyword>
<symbol>
<identifier>
<stringConstant>
<integerConstant>


"""


def class_name(xml_command):
    tokens = xml_command.split()
    if tokens[0] == '<identifier>':
        return tokens[1]
    return False


def subroutine_name(xml_command):
    tokens = xml_command.split()
    if tokens[0] == '<identifier>':
        return tokens[1]
    return False


def var_name(xml_command):
    tokens = xml_command.split()
    if tokens[0] == '<identifier>':
        return tokens[1]
    return False


def keyword_constant(xml_command):
    tokens = xml_command.split()
    if tokens[0] == '<keyword>' and tokens[1] in {'true', 'false', 'null', 'this'}:
        return tokens[1]
    return False


def string_constant(xml_command):
    tokens = xml_command.split()
    if tokens[0] == '<stringConstant>':
        return tokens[1]
    return False


def integer_constant(xml_command):
    tokens = xml_command.split()
    if tokens[0] == '<integerConstant>':
        return tokens[1]
    return False


def unary_op(xml_command):
    tokens = xml_command.split()
    if tokens[0] == '<symbol>' and tokens[1] in {'-', '~'}:
        return tokens[1]
    return False


def op(xml_command):
    tokens = xml_command.split()
    if tokens[0] == '<symbol>' and tokens[1] in {'-', '+', '*', '/', '&', '&gt;',
                                                 '|', '<', '>', '=', '&lt;', '&amp;'}:
        if tokens[1] in {'&gt;': '>', '&lt;': '<', '&amp;': '&'}:
            return {'&gt;': '>', '&lt;': '<', '&amp;': '&'}[tokens[1]]
        return tokens[1]

    return False


def type_(xml_command):
    tokens = xml_command.split()
    classname = class_name(xml_command)
    if tokens[0] == '<keyword>' and tokens[1] in ['int', 'char', 'boolean']:
        return tokens[1]
    elif classname:
        return classname
    return False


from pprint import pprint


class Symbol_Table():
    """
    name : identifier
    type: int, char, boolean, class_name
    kind: field, static, local, argument
    index: 0, 1, 2, 3 ....
    scope: class level, subroutine level
    """

    def __init__(self):
        self.class_table = {'varName': {},
                            'field': 0,
                            'static': 0
                            }
        self.function_table = {'varName': {},
                               'local': 0,
                               'argument': 0
                               }
        # self.current_scope = None
        # self.current = None

    def new_class_table(self):
        self.class_table = {'varName': {},
                            'field': 0,
                            'static': 0
                            }

    def new_function_table(self):
        self.function_table = {'varName': {},
                               'local': 0,
                               'argument': 0
                               }

    def add_to_class(self, data):
        """Update the data in class for var_name
        Expected data format = [name,type,kind]

        :param data: Data to be updated with
        :return:
        """
        self.class_table['varName'][data[0]] = data + [self.class_table[data[-1]]]
        print self.class_table
        self.class_table[data[-1]] += 1

    def add_to_function(self, data):
        """Update the data in class for var_name
        Expected data format = [name,type,kind]

        :param data: Data to be updated with
        :return:
        """
        self.function_table['varName'][data[0]] = data + [self.function_table[data[-1]]]
        self.function_table[data[-1]] += 1

    def add_this(self, class_type):
        """
        Add a row to function argument if the current subroutine is method
        :param class_type:
        :return:
        """
        self.function_table['varName']['this'] = ['this', class_type, 'argument', self.function_table['argument']]
        self.function_table['argument'] += 1

    def find_in_class(self, vari_name):
        return self.class_table['varName'][vari_name]

    def find_in_function(self, vari_name):
        return self.function_table['varName'][vari_name]

    def find_in_both(self, vari_name):
        try:
            return ['this' if i == 'field' else i for i in self.find_in_class(vari_name)]
        except KeyError:

            try:
                return self.find_in_function(vari_name)
            except KeyError:
                return False








from pprint import pprint


# d = Symbol_Table()
# d.new_class_table()
# print d.class_table
# d.add_to_class(['x', 'int', 'field'])
# d.add_to_class(['y', 'int', 'field'])
# pprint(d.class_table)
# print d.find_in_class('x')

class compilationEngine(object):

    def __init__(self, tokenised_list):
        self.tokenised_list = tokenised_list
        self.start_ctr = 0
        self.current_token = self.tokenised_list[self.start_ctr]
        self.next_token = self.tokenised_list[self.start_ctr + 1]
        self.current_token_value = self.current_token.split()[1]
        self.current_token_tag = self.current_token.split()[0]
        self.next_token_value = self.next_token.split()[1]
        self.next_token_tag = self.next_token.split()[0]
        self.xml = []
        self.class_table_data = [None, None, None]
        self.function_table_data = [None, None, None]
        self.symbol_table = Symbol_Table()
        self.current_class_name = None
        self.current_function_name = None

    def increase_ctr(self, val=1):
        self.start_ctr += val
        self.current_token = self.tokenised_list[self.start_ctr]
        self.current_token_value = self.current_token.split()[1]
        self.current_token_tag = self.current_token.split()[0]
        if self.start_ctr != len(self.tokenised_list) - 1:
            self.next_token = self.tokenised_list[self.start_ctr + 1]
            self.next_token_value = self.next_token.split()[1]
            self.next_token_tag = self.next_token.split()[0]

    def compile_var_dec(self):
        """
        Grammar for varDec: 'var' type varName (',' varName)* ';'
        Implementation follows the grammar

        :return:
        """

        self.xml.append("<varDec>")

        if self.current_token_value == "var":
            # Set current function table data to local type variable
            self.function_table_data[2] = 'local'

            self.xml.append(self.current_token)
            self.increase_ctr()
        else:
            return False, self.start_ctr

        if type_(self.current_token):

            self.function_table_data[1] = type_(self.current_token)

            self.xml.append(self.current_token)
            self.increase_ctr()
        else:
            return False, self.start_ctr, self.current_token

        if var_name(self.current_token):
            self.function_table_data[0] = var_name(self.current_token)
            self.symbol_table.add_to_function(self.function_table_data)

            self.xml.append(self.current_token)
            # print self.current_token,self.next_token, '---0'

            self.increase_ctr()
        else:
            return False, self.start_ctr
        # print self.current_token,'---1'
        while self.current_token_value != ';':
            if self.current_token_value == ',':

                self.xml.append(self.current_token)
                self.increase_ctr()
            else:
                return False, self.start_ctr

            if var_name(self.current_token):
                self.function_table_data[0] = var_name(self.current_token)
                self.symbol_table.add_to_function(self.function_table_data)

                self.xml.append(self.current_token)
                self.increase_ctr()
            else:
                return False, self.start_ctr
        else:
            if self.current_token_value == ';':
                self.xml.append(self.current_token)
                self.increase_ctr()

        self.xml.append("</varDec>")

    def compile_expression_list(self):
        """
        Grammar : (expression (',' expression)* )?

        :return:
        """
        # print '<expressionList>'
        # self.xml.append("<expressionList>")
        self.compile_expression()
        while self.current_token_value == ',':
            # print self.current_token
            # self.xml.append(self.current_token)
            self.increase_ctr()
            self.compile_expression()
        if self.current_token_value == ')':
            self.increase_ctr()
        # print '</expressionList>'
        # self.xml.append("</expressionList>")

    def compile_subroutine_call(self):
        """
        Grammar : subroutineName '(' expressionList ')' | (className |
                  varName) '.' subroutineName '(' expressionList ')'

        :return:
        """
        current_call = self.current_token_value
        call_class = self.current_token_value
        if var_name(self.current_token):
            if self.next_token_value == '(':
                self.increase_ctr(2)
                self.xml.append(self.current_token)
                if self.next_token_value != ')':
                    self.compile_expression_list()

                else:

                    self.xml.append('<expressionList>')
                    self.xml.append('</expressionList>')
                    self.increase_ctr()

                    self.xml.append(self.current_token)
                    self.increase_ctr()
                print 'call %s' % call_class
            elif self.next_token_value == '.':

                self.xml.append(self.current_token)
                self.increase_ctr()
                if self.current_token_value == '.':
                    call_class += self.current_token_value

                    self.xml.append(self.current_token)

                self.increase_ctr()
                # print self.current_token, '--5'
                if subroutine_name(self.current_token):
                    call_class += self.current_token_value

                    self.xml.append(self.current_token)
                    self.increase_ctr()
                    # print self.current_token, '--5'
                    if self.current_token_value == '(':
                        print self.current_token
                        self.xml.append(self.current_token)

                        # print self.current_token, '--7'
                        if self.next_token_value == ')':

                            self.xml.append('<expressionList>')
                            self.xml.append('</expressionList>')

                            self.increase_ctr()

                            self.xml.append(self.current_token)
                            self.increase_ctr()
                        else:
                            self.increase_ctr()
                            self.compile_expression_list()

                            self.xml.append(self.current_token)
                            self.increase_ctr()

                        print 'call %s' % call_class

                        # else:
                        #     return False, self.start_ctr
                    else:
                        return False, self.start_ctr
                else:
                    return False, self.start_ctr

    def compile_term(self):
        """
        Grammar : integerConstant | stringConstant | keywordConstant |
                varName | varName '[' expression ']' | subroutineCall |
                '(' expression ')' | unaryOp term

        :return:
        """
        # print '<term>'
        self.xml.append("<term>")
        # print self.current_token
        if var_name(self.current_token):
            if self.next_token_value == '[':

                self.xml.append(self.current_token)
                self.increase_ctr()

                self.xml.append(self.current_token)
                self.increase_ctr()
                self.compile_expression()
                if self.current_token_value == ']':

                    self.xml.append(self.current_token)
                    self.increase_ctr()
                else:
                    return False, self.start_ctr

            elif self.next_token_value == '(':
                self.compile_subroutine_call()

            elif self.next_token_value == '.':
                self.compile_subroutine_call()

            else:
                if self.symbol_table.find_in_both(self.current_token_value):
                    row = self.symbol_table.find_in_both(self.current_token_value)
                    mem, ctr = row[-2], row[-1]
                    print 'push %s' % mem +' '+ str(ctr)
                self.xml.append(self.current_token)
                self.increase_ctr()
                # print self.current_token,'---inside compile else-------'
        elif unary_op(self.current_token):
            # print self.current_token,self.next_token, '+++++=========++++++='
            # if integer_constant(self.next_token):
            print "push %s" % self.next_token_value
            print 'push %s' % self.current_token_value
            self.increase_ctr()
            self.xml.append(self.current_token)
            self.increase_ctr()
            self.compile_term()

            # self.increase_ctr()

        elif self.current_token_value == '(':

            self.xml.append(self.current_token)
            self.increase_ctr()
            self.compile_expression()
            if self.current_token_value == ')':
                self.xml.append(self.current_token)
                self.increase_ctr()
            else:
                return False, self.start_ctr
        else:
            # print self.current_token, '+++++=========++++++='
            if string_constant(self.current_token):
                print "push %s" % self.current_token_value
                self.xml.append(self.current_token)
                self.increase_ctr()
            elif integer_constant(self.current_token):
                print "push %s" % self.current_token_value
                self.xml.append(self.current_token)
                self.increase_ctr()
            elif keyword_constant(self.current_token):
                print "push %s" % self.current_token_value
                self.xml.append(self.current_token)
                self.increase_ctr()
            else:
                return False
        self.xml.append("</term>")

    def compile_expression(self):
        """

        term (op term)*
        :return:
        """
        # print '<expression>'
        self.xml.append("<expression>")

        self.compile_term()
        # print self.current_token, '---4'
        while op(self.current_token):
            current_op = op(self.current_token)
            self.xml.append(self.current_token)
            self.increase_ctr()
            self.compile_term()
            print current_op

        # self.increase_ctr()
        # print self.current_token,'---4'

        # print '</expression>'
        self.xml.append("</expression>")

    def compile_let_statement(self):
        """
        'let' varName ('[' expression ']')? '=' expression ';'
        :return:
        """

        self.xml.append("<letStatement>")
        variable_name = ''

        if self.current_token_value == 'let':

            self.xml.append(self.current_token)
            self.increase_ctr()
            if var_name(self.current_token):
                variable_name = self.current_token_value

                self.xml.append(self.current_token)
                self.increase_ctr()
                # print self.current_token,'---2'
                if self.current_token_value == '[':

                    self.xml.append(self.current_token)
                    self.increase_ctr()
                    self.compile_expression()

                    self.xml.append(self.current_token)
                    self.increase_ctr()
                    if self.current_token_value == '=':

                        self.xml.append(self.current_token)
                        self.increase_ctr()
                        self.compile_expression()
                        # print self.current_token,'---2-----------------'
                        if self.current_token_value == ';':

                            self.xml.append(self.current_token)
                            self.increase_ctr()
                        else:
                            return False, self.start_ctr
                    else:
                        return False, self.start_ctr
                elif self.current_token_value == '=':

                    self.xml.append(self.current_token)
                    self.increase_ctr()
                    self.compile_expression()
                    print 'pop %s' % variable_name

                    self.xml.append(self.current_token)
                    self.increase_ctr()

            else:
                return False, self.start_ctr

        else:
            return False, self.start_ctr

        self.xml.append("</letStatement>")

    def compile_if_statement(self):
        """
        Grammar : 'if' '(' expression ')' '{' statements '}'
                  ('else' '{' statements '}')?

        :return:
        """

        # Unique lable for false statement
        l1 = str(self.current_class_name) + str(self.current_function_name) + str(self.start_ctr)
        l2 = str(self.current_class_name) + str(self.current_function_name) + str(self.start_ctr) + '!~'

        if self.current_token_value == 'if':

            self.xml.append(self.current_token)
            self.increase_ctr()
            if self.current_token_value == '(':

                self.xml.append(self.current_token)
                self.increase_ctr()
                self.compile_expression()
                if self.current_token_value == ')':

                    self.xml.append(self.current_token)
                    self.increase_ctr()
                    if self.current_token_value == '{':
                        print 'not'
                        print 'if-goto %s' % l1

                        self.xml.append(self.current_token)
                        self.increase_ctr()
                        self.compile_statements()

                        if self.current_token_value == '}':

                            self.xml.append(self.current_token)
                            self.increase_ctr()
                            print 'goto %s' % l2
                            if self.current_token_value == 'else':

                                self.xml.append(self.current_token)
                                self.increase_ctr()

                                print 'label %s' % l1
                                if self.current_token_value == '{':

                                    self.xml.append(self.current_token)
                                    self.increase_ctr()
                                    self.compile_statements()
                                    if self.current_token_value == '}':

                                        self.xml.append(self.current_token)
                                        self.increase_ctr()
                                        print 'label %s' % l2
                                    else:
                                        return False, self.start_ctr
                                else:
                                    return False, self.start_ctr
                        else:
                            print
                    else:
                        print
                else:
                    print
            else:
                print
        else:
            return False, self.start_ctr
        self.xml.append("</ifStatement>")

    def compile_while_statement(self):
        """

        Grammar : 'while' '(' expression ')' '{' statements '}'
        :return:
        """
        l1 = str(self.current_class_name) + str(self.current_function_name) + str(self.start_ctr)
        l2 = str(self.current_class_name) + str(self.current_function_name) + str(self.start_ctr) + '!~'

        # declare label 1
        print 'label %s' % l1

        self.xml.append("<whileStatement>")

        if self.current_token_value == 'while':

            self.xml.append(self.current_token)
            self.increase_ctr()
            if self.current_token_value == '(':

                self.xml.append(self.current_token)
                self.increase_ctr()
                self.compile_expression()
                if self.current_token_value == ')':

                    self.xml.append(self.current_token)
                    self.increase_ctr()
                    if self.current_token_value == '{':
                        # Negate the expression
                        print 'not'
                        print 'if-goto %s' % l2

                        self.xml.append(self.current_token)
                        self.increase_ctr()
                        self.compile_statements()
                        if self.current_token_value == '}':
                            print 'goto %s' % l1
                            print 'label %s' % l2
                            self.xml.append(self.current_token)
                            self.increase_ctr()
                        else:
                            return False, self.start_ctr
                    else:
                        return False, self.start_ctr
                else:
                    return False, self.start_ctr
            else:
                return False, self.start_ctr
        else:
            return False, self.start_ctr

        self.xml.append("</whileStatement>")

    def compile_do_statement(self):
        """
        Grammar : do' subroutineCall ';'

        DO basically is a goto command in vm
        :return:
        """

        self.xml.append("<doStatement>")

        if self.current_token_value == 'do':

            self.xml.append(self.current_token)
            self.increase_ctr()
            # print self.current_token,'0----'
            self.compile_subroutine_call()
            # print self.current_token,'0----'
            # print push
            # self.increase_ctr()
            if self.current_token_value == ';':

                self.xml.append(self.current_token)
                self.increase_ctr()
            else:
                return False, self.start_ctr
        else:
            return False, self.start_ctr

        self.xml.append("</doStatement>")

    def compile_return(self):
        """
         Grammar : 'return' expression? ';'

         just use return in vm to convert
        :return:
        """

        self.xml.append("<returnStatement>")

        if self.current_token_value == 'return':

            self.xml.append(self.current_token)
            self.increase_ctr()
            if self.current_token_value != ';':
                self.compile_expression()
            else:

                self.xml.append(self.current_token)
                self.increase_ctr()
            print 'return'
        self.xml.append("</returnStatement>")

    def compile_statements(self):
        """
        Grammar : statement*
        :return:
        """

        self.xml.append("<statements>")
        # print self.current_token,'-----statements ---'
        while self.current_token_value != '}':
            if self.current_token_value == 'let':
                self.compile_let_statement()
            elif self.current_token_value == 'if':
                self.compile_if_statement()
            elif self.current_token_value == 'while':
                self.compile_while_statement()
            elif self.current_token_value == 'do':
                self.compile_do_statement()
            elif self.current_token_value == 'return':
                self.compile_return()
            else:
                return False, self.start_ctr

        self.xml.append("</statements>")

    def compile_subroutine_body(self):
        """
        Grammar : '{' varDec* statements '}'
        :return:
        """

        self.xml.append("<subroutineBody>")

        self.xml.append(self.current_token)
        if self.current_token_value == '{':
            self.increase_ctr()
            # print self.current_token, '--3'
            while self.current_token_value == 'var':
                self.compile_var_dec()
            else:
                # while self.current_token_value != '}':
                self.compile_statements()

                self.xml.append(self.current_token)
        else:
            return False, self.start_ctr

        self.xml.append("</subroutineBody>")

    def compile_parameter_list(self):

        """
        parameterList: ((type varName) (',' type varName)*)?
        :return:
        """

        self.xml.append("<parameterList>")
        # Subroutine kind
        self.function_table_data[2] = 'argument'

        # Subroutine current argument Type
        if type_(self.current_token):

            self.xml.append(self.current_token)
            self.function_table_data[1] = self.current_token_value
            self.increase_ctr()

            # Current variable name
            if var_name(self.current_token):
                self.function_table_data[0] = self.current_token_value
                self.symbol_table.add_to_function(self.function_table_data)

                self.xml.append(self.current_token)
                self.increase_ctr()
                while self.current_token_value == ',':

                    self.xml.append(self.current_token)
                    self.increase_ctr()
                    if type_(self.current_token):
                        self.function_table_data[1] = self.current_token_value

                        self.xml.append(self.current_token)
                        self.increase_ctr()
                        if var_name(self.current_token):
                            self.function_table_data[0] = self.current_token_value
                            self.symbol_table.add_to_function(self.function_table_data)

                            self.xml.append(self.current_token)
                            self.increase_ctr()
                        else:
                            return False, self.start_ctr
                    else:
                        return False, self.start_ctr
            else:
                return False, self.start_ctr
        else:
            return False, self.start_ctr
        # pprint(self.symbol_table.function_table)

        self.xml.append("</parameterList>")

    def compile_subroutine_dec(self):
        """
        Grammar : ('constructor'|'function'|'method')
                ('void' | type) subroutineName '(' parameterList ')'
                subroutineBody

        Symbol Table Format : Name, type, kind, Index

        :return:
        """
        is_subroutine_method = False
        current_subroutine_type = self.current_token_value

        # Create a new function table for the current running subroutine
        self.symbol_table.new_function_table()

        self.xml.append("<subroutineDec>")
        # if this is a method we want to add 'this' entry to function symbol table
        if self.current_token_value == 'method':
            is_subroutine_method = True

        self.xml.append(self.current_token)
        self.increase_ctr()

        # Type of this subroutine
        if type_(self.current_token) or self.current_token_value == 'void':

            if is_subroutine_method:
                self.symbol_table.add_this(self.current_class_name)
            self.xml.append(self.current_token)
            self.increase_ctr()

            # Name of subroutine
            if subroutine_name(self.current_token):
                self.current_function_name = self.current_token_value

                self.xml.append(self.current_token)
                self.increase_ctr()

                if self.current_token_value == '(':

                    self.xml.append(self.current_token)
                    self.increase_ctr()

                    # Compile parameter list
                    self.compile_parameter_list()
                    self.xml.append(self.current_token)
                    self.increase_ctr()
                else:
                    return False, self.start_ctr
                if current_subroutine_type == 'constructor':
                    print 'push %s' % self.symbol_table.class_table['field']
                    print 'call Memory.alloc %s' % self.symbol_table.class_table['field']
                    print 'pop pointer 0'
                self.compile_subroutine_body()
            else:
                return False, self.start_ctr
        else:
            return False, self.start_ctr

        self.xml.append("</subroutineDec>")

    def compile_class_var_dec(self):
        """
        Grammar for this classVarDec :  ('static'|'field') type varName (',' varName)* ';'
        Implementation follows the grammar

        :return:
        """
        kind = ""
        var_type = ""
        name = ""

        self.xml.append("<classVarDec>")

        # Kind of variable
        if self.current_token_value in {'static', 'field'}:
            if self.current_token_value == 'static':
                self.class_table_data[2] = self.current_token_value

            else:
                self.class_table_data[2] = self.current_token_value

            self.xml.append(self.current_token)
            self.increase_ctr()
        else:
            return False, self.start_ctr

        # Type of variable
        if type_(self.current_token):
            self.class_table_data[1] = type_(self.current_token)

            self.xml.append(self.current_token)
            self.increase_ctr()
        else:
            return False, self.start_ctr

        # Name of the variable
        if var_name(self.current_token):
            self.class_table_data[0] = var_name(self.current_token)
            self.symbol_table.add_to_class(self.class_table_data)

            # print self.class_table_data

            self.xml.append(self.current_token)
            self.increase_ctr()
        else:
            return False, self.start_ctr

        while self.current_token_value != ';':
            if self.current_token_value == ',':

                self.xml.append(self.current_token)
                self.increase_ctr()
                if var_name(self.current_token):
                    self.class_table_data[0] = var_name(self.current_token)
                    self.symbol_table.add_to_class(self.class_table_data)

                    # print self.symbol_table.class_table

                    self.xml.append(self.current_token)
                    self.increase_ctr()
                else:
                    return "Not a valid varName"

            else:
                return False, self.start_ctr

        else:
            if self.current_token_value == ';':
                self.xml.append(self.current_token)
                self.increase_ctr()

        self.xml.append("</classVarDec>")
        return None

    def compile_class(self):
        """
        'class' className '{' classVarDec* subroutineDec* '}'

        :return:
        """

        if self.current_token_value != 'class':
            return False, "Not a class"
        else:

            self.xml.append('<class>')

            self.xml.append(self.current_token)
            self.increase_ctr()
            if not class_name(self.current_token):
                return False, self.start_ctr
            else:

                # Set current class name
                self.current_class_name = self.current_token_value
                self.xml.append(self.current_token)
                self.increase_ctr()
                if self.current_token_value != '{':
                    return False, self.start_ctr
                else:

                    self.xml.append(self.current_token)
                    self.increase_ctr()
                    if self.current_token_value == '}':

                        self.xml.append(self.current_token)
                    else:
                        while self.current_token_value in {'static', 'field'}:
                            self.compile_class_var_dec()

                        while self.current_token_value in {'constructor', 'function', 'method'}:
                            self.compile_subroutine_dec()
                            self.increase_ctr()

                        self.xml.append(self.current_token)

            self.xml.append('</class>')
        return None


class_list_test = ['<keyword> class </keyword>',
                   '<identifier> Main </identifier>',
                   '<symbol> { </symbol>',
                   '<keyword> static </keyword>',
                   '<keyword> boolean </keyword>',
                   '<identifier> test </identifier>',
                   '<symbol> ; </symbol>',
                   '<keyword> static </keyword>',
                   '<keyword> boolean </keyword>',
                   '<identifier> test </identifier>',
                   '<symbol> ; </symbol>',
                   '<symbol> } </symbol>',
                   ]
classVarDec_list_test = ['<keyword> class </keyword>',
                         '<identifier> Square </identifier>',
                         '<symbol> { </symbol>',
                         '<keyword> field </keyword>',
                         '<keyword> int </keyword>',
                         '<identifier> x </identifier>',
                         '<symbol> , </symbol>',
                         '<identifier> y </identifier>',
                         '<symbol> ; </symbol>',
                         '<keyword> field </keyword>',
                         '<keyword> int </keyword>',
                         '<identifier> size </identifier>',
                         '<symbol> ; </symbol>',
                         '<symbol> } </symbol>',
                         ]
parameter_list_test = ['<keyword> int </keyword>',
                       '<identifier> Ax </identifier>',
                       '<symbol> , </symbol>',
                       '<keyword> int </keyword>',
                       '<identifier> Ay </identifier>',
                       '<symbol> , </symbol>',
                       '<keyword> int </keyword>',
                       '<identifier> Asize </identifier>',
                       '<symbol> ) </symbol>']
var_dec_list_test = ['<keyword> var </keyword>',
                     '<keyword> int </keyword>',
                     '<identifier> i </identifier>',
                     '<symbol> , </symbol>',
                     '<identifier> j </identifier>',
                     '<symbol> ; </symbol>',
                     '<symbol> ) </symbol>']
return_test_list = ['<keyword> return </keyword>',
                    '<symbol> ; </symbol>',
                    '<symbol> ) </symbol>']

# pprint(return_test_list)

# dummy_input_list = [raw_input().strip() for i in range(2)]
# pprint(dummy_input_list)

# pprint(var_dec_list_test)
# d = compilationEngine(class_list_test)
# print d.compile_class()
#
# d = compilationEngine(classVarDec_list_test)
# print d.compile_class()

# d = compilationEngine(parameter_list_test)
# print d.compile_parameter_list()

# d = compilationEngine(var_dec_list_test)
# print d.compile_var_dec()

# d= compilationEngine(return_test_list)
# print d.compile_return()
with open('./testTT.xml', 'r') as exam:
    com_lis = exam.read().splitlines()

# pprint(com_lis)
d = compilationEngine(com_lis)
print d.compile_class()
with open('./out.xml', 'w') as ex:
    for i in d.xml:
        ex.write(i + '\n')
# print d.xml
pprint(d.symbol_table.class_table)
pprint(d.symbol_table.function_table)
print d.symbol_table.find_in_both('x')
