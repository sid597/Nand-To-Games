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
    if tokens[0] == '<symbol>' and tokens[1] in {'-', '+', '*', '/', '&',
                                                 '|', '<', '>', '='}:
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


# l = ['<symbol> ( </symbol>',
#      '<symbol> ( </symbol>',
#      '<identifier> y </identifier>',
#      '<symbol> + </symbol>',
#      '<identifier> size </identifier>',
#      '<symbol> ) </symbol>',
#      '<symbol> &lt; </symbol>',
#      '<integerConstant> 254 </integerConstant>',
#      '<symbol> ) </symbol>'
#      ]
from pprint import pprint


# pprint(['<symbol> ( </symbol>','<symbol> ( </symbol>', '<identifier> y </identifier>', '<symbol> + </symbol>',
# '<identifier> size </identifier>', '<symbol> ) </symbol>', '<symbol> &lt; </symbol>','<integerConstant> 254
# </integerConstant>','<symbol> ) </symbol>'] ) print term(l, 0)


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

        print '<varDec>'
        self.xml.append("<varDec>")

        if self.current_token_value == "var":
            print self.current_token
            self.xml.append(self.current_token)
            self.increase_ctr()
        else:
            return False, self.start_ctr

        if type_(self.current_token):
            print self.current_token
            self.xml.append(self.current_token)
            self.increase_ctr()
        else:
            return False, self.start_ctr, self.current_token

        if var_name(self.current_token):
            print self.current_token
            self.xml.append(self.current_token)
            print self.current_token,self.next_token, '---0'

            self.increase_ctr()
        else:
            return False, self.start_ctr
        print self.current_token,'---1'
        while self.current_token_value != ';':
            if self.current_token_value == ',':
                print self.current_token
                self.xml.append(self.current_token)
                self.increase_ctr()
            else:
                return False, self.start_ctr

            if var_name(self.current_token):
                print self.current_token
                self.xml.append(self.current_token)
                self.increase_ctr()
            else:
                return False, self.start_ctr
        else:
            if self.current_token_value == ';':
                print self.current_token
                self.xml.append(self.current_token)
                self.increase_ctr()
        print '</varDec>'
        self.xml.append("</varDec>")

    def compile_expression_list(self):
        print '<expressionList>'
        self.xml.append("<expressionList>")

        self.compile_expression_list()
        while self.current_token_value == ',':
            print self.current_token
            self.xml.append(self.current_token)
            self.compile_expression()
        print '</expressionList>'
        self.xml.append("</expressionList>")

    def compile_subroutine_call(self):
        if var_name(self.current_token):
            if self.next_token_value == '(':
                print self.current_token
                self.xml.append(self.current_token)
                self.increase_ctr()
                if self.next_token_value != ')':
                    self.compile_expression_list()
                if self.current_token_value == ')':
                    print self.current_token
                    self.xml.append(self.current_token)
                    self.increase_ctr()

            elif self.next_token_value == '.':
                self.increase_ctr()
                print self.current_token
                self.xml.append(self.current_token)
                self.increase_ctr()
                # print self.current_token, '--5'
                if subroutine_name(self.current_token):
                    print self.current_token
                    self.xml.append(self.current_token)
                    self.increase_ctr()
                    # print self.current_token, '--5'
                    if self.current_token_value == '(':
                        print self.current_token
                        self.xml.append(self.current_token)

                        # print self.current_token, '--7'
                        if self.next_token_value != ')':
                            self.compile_expression_list()
                        if self.next_token_value == ')':
                            self.increase_ctr()
                            # print self.current_token,'--8'
                            self.xml.append(self.current_token)
                            self.increase_ctr()
                            # print self.current_token, '--8'
                        else:
                            return False, self.start_ctr
                    else:
                        return False, self.start_ctr
                else:
                    return False, self.start_ctr

    def compile_term(self):
        print '<term>'
        self.xml.append("<term>")
        print self.current_token,self.next_token,'--compile_term--beforeif-----'
        if var_name(self.current_token):
            if self.next_token == '[':
                print self.current_token
                self.xml.append(self.current_token)
                self.increase_ctr()
                self.compile_expression()
                if self.current_token_value == ']':
                    print self.current_token
                    self.xml.append(self.current_token)
                    self.increase_ctr()
                else:
                    return False, self.start_ctr

            elif self.next_token == '(':
                self.compile_subroutine_call()

            elif self.next_token == '.':
                self.compile_subroutine_call()

            else:
                print self.current_token
                self.xml.append(self.current_token)
                self.increase_ctr()
                print self.current_token,'---inside compile else-------'
        elif unary_op(self.current_token):
            print self.current_token
            self.xml.append(self.current_token)
            self.increase_ctr()
            self.compile_term()
            self.increase_ctr()

        elif self.current_token_value == '(':
            print self.current_token
            self.xml.append(self.current_token)
            self.increase_ctr()
            self.compile_expression()
            if self.current_token_value == ')':
                print self.current_token
                self.xml.append(self.current_token)()
                self.increase_ctr()
            else:
                return False, self.start_ctr
        else:
            if string_constant(self.current_token):
                print self.current_token
                self.xml.append(self.current_token)
                self.increase_ctr()
            if integer_constant(self.current_token):
                print self.current_token
                self.xml.append(self.current_token)
                self.increase_ctr()
            if keyword_constant(self.current_token):
                print self.current_token
                self.xml.append(self.current_token)
                self.increase_ctr()
            else:
                return False
        print '</term>'
        self.xml.append("</term>")

    def compile_expression(self):
        print '<expression>'
        self.xml.append("<expression>")

        self.compile_term()
        print self.current_token, '---4'
        while op(self.current_token_value):
            print self.current_token
            self.xml.append(self.current_token)
            self.increase_ctr()
            self.compile_term()
        # self.increase_ctr()
        print self.current_token,'---4'
        print '</expression>'
        self.xml.append("</expression>")

    def compile_let_statement(self):
        print '<letStatement>'
        self.xml.append("<letStatement>")

        if self.current_token_value == 'let':
            print self.current_token
            self.xml.append(self.current_token)
            self.increase_ctr()
            if var_name(self.current_token):
                print self.current_token
                self.xml.append(self.current_token)
                self.increase_ctr()
                # print self.current_token,'---2'
                if self.current_token_value == '[':
                    print self.current_token
                    self.xml.append(self.current_token)
                    self.increase_ctr()
                    self.compile_expression()
                    print self.current_token
                    self.xml.append(self.current_token)
                    self.increase_ctr()
                    if self.current_token_value == '=':
                        print self.current_token
                        self.xml.append(self.current_token)
                        self.increase_ctr()
                        self.compile_expression()
                        # print self.current_token,'---2'
                        if self.current_token_value == ';':
                            print self.current_token
                            self.xml.append(self.current_token)
                            self.increase_ctr()
                        else:
                            return False, self.start_ctr
                    else:
                        return False, self.start_ctr
                elif self.current_token_value == '=':
                    print self.current_token
                    self.xml.append(self.current_token)
                    self.increase_ctr()
                    self.compile_expression()
                    print self.current_token,'---2'
                    self.xml.append(self.current_token)
                    self.increase_ctr()

            else:
                return False, self.start_ctr

        else:
            return False, self.start_ctr

        print '</letStatement>'
        self.xml.append("</letStatement>")

    def compile_if_statement(self):
        print '<ifStatement>'
        self.xml.append("<ifStatement>")

        if self.current_token_value == 'if':
            print self.current_token
            self.xml.append(self.current_token)
            self.increase_ctr()
            if self.current_token_value == '(':
                print self.current_token
                self.xml.append(self.current_token)
                self.compile_expression()
                if self.current_token_value == ')':
                    print self.current_token
                    self.xml.append(self.current_token)
                    self.increase_ctr()
                    if self.current_token_value == '{':
                        print self.current_token
                        self.xml.append(self.current_token)
                        self.increase_ctr()
                        self.compile_statements()
                        if self.current_token_value == '}':
                            print self.current_token
                            self.xml.append(self.current_token)
                            self.increase_ctr()
                            if self.current_token_value == 'else':
                                print self.current_token
                                self.xml.append(self.current_token)
                                self.increase_ctr()
                                if self.current_token_value == '{':
                                    print self.current_token
                                    self.xml.append(self.current_token)
                                    self.increase_ctr()
                                    self.compile_statements()
                                    if self.current_token_value == '}':
                                        print self.current_token
                                        self.xml.append(self.current_token)
                                        self.increase_ctr()
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
        print '</ifStatement>'
        self.xml.append("</ifStatement>")

    def compile_while_statement(self):
        print '<whileStatement>'
        self.xml.append("</whileStatement>")

        if self.current_token_value == 'while':
            print self.current_token
            self.xml.append(self.current_token)
            self.increase_ctr()
            if self.current_token_value == '(':
                print self.current_token
                self.xml.append(self.current_token)
                self.increase_ctr()
                self.compile_expression()
                if self.current_token_value == ')':
                    print self.current_token
                    self.xml.append(self.current_token)
                    self.increase_ctr()
                    if self.current_token_value == '{':
                        print self.current_token
                        self.xml.append(self.current_token)
                        self.increase_ctr()
                        self.compile_statements()
                        if self.current_token_value == '}':
                            print self.current_token
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
        print '</whileStatement>'
        self.xml.append("</whileStatement>")

    def compile_do_statement(self):
        print '<doStatement>'
        self.xml.append("<doStatement>")

        if self.current_token_value == 'do':
            print self.current_token
            self.xml.append(self.current_token)
            self.increase_ctr()
            self.compile_subroutine_call()
            if self.current_token_value == ';':
                print self.current_token
                self.xml.append(self.current_token)
                self.increase_ctr()
            else:
                return False, self.start_ctr
        else:
            return False, self.start_ctr

        print '</doStatement>'
        self.xml.append("</doStatement>")

    def compile_return(self):
        print '<returnStatement>'
        self.xml.append("</returnStatement>")

        if self.current_token_value == 'return':
            print self.current_token
            self.xml.append(self.current_token)
            self.increase_ctr()
            if self.current_token_value != ';':
                self.compile_expression()
            if self.current_token_value == ';':
                print self.current_token
                self.xml.append(self.current_token)
                self.increase_ctr()
            else:
                return False, self.start_ctr
        else:
            return False, self.start_ctr

        print '</returnStatement>'
        self.xml.append("</returnStatement>")

    def compile_statements(self):
        print '<statements>'
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
        print '</statements>'
        self.xml.append("</statements>")

    def compile_subroutine_body(self):
        print '<subroutineBody>'
        self.xml.append("<subroutineBody>")

        print self.current_token
        self.xml.append(self.current_token), '--2'
        if self.current_token_value == '{':
            self.increase_ctr()
            # print self.current_token, '--3'
            self.xml.append(self.current_token)
            while self.current_token_value == 'var':
                self.compile_var_dec()
            else:
                # while self.current_token_value != '}':
                self.compile_statements()
                print self.current_token
                self.xml.append(self.current_token)
        else:
            return False, self.start_ctr
        print '</subroutineBody>'
        self.xml.append("</subroutineBody>")

    def compile_parameter_list(self):

        """
        parameterList: ((type varName) (',' type varName)*)?
        :return:
        """
        print '<parameterList>'
        self.xml.append("<parameterList>")

        if type_(self.current_token):
            print self.current_token
            self.xml.append(self.current_token)
            self.increase_ctr()
            if var_name(self.current_token):
                print self.current_token
                self.xml.append(self.current_token)
                self.increase_ctr()
                while self.current_token_value == ',':
                    print self.current_token
                    self.xml.append(self.current_token)
                    self.increase_ctr()
                    if type_(self.current_token):
                        print self.current_token
                        self.xml.append(self.current_token)
                        self.increase_ctr()
                        if var_name(self.current_token):
                            print self.current_token
                            self.xml.append(self.current_token)
                            self.increase_ctr()
        #                 else:
        #                     return False, self.start_ctr
        #             else:
        #                 return False, self.start_ctr
        #     else:
        #         return False, self.start_ctr
        # else:
        #     return False, self.start_ctr
        print '</parameterList>'
        self.xml.append("</parameterList>")

    def compile_subroutine_dec(self):
        print '<subroutineDec>'
        self.xml.append("<subroutineDec>")

        print self.current_token
        self.xml.append(self.current_token)
        self.increase_ctr()
        if type_(self.current_token) or self.current_token_value == 'void':
            print self.current_token
            self.xml.append(self.current_token)
            self.increase_ctr()
            if subroutine_name(self.current_token):
                print self.current_token
                self.xml.append(self.current_token)
                self.increase_ctr()

                if self.current_token_value == '(':
                    print self.current_token
                    self.xml.append(self.current_token)
                    self.increase_ctr()
                    # if self.current_token_value == ')':
                    #     print self.current_token
                    # self.xml.append(self.current_token)
                    #     self.increase_ctr()
                    # else:
                    self.compile_parameter_list()
                    print self.current_token
                    self.xml.append(self.current_token)
                    self.increase_ctr()
                else:
                    return False, self.start_ctr
                self.compile_subroutine_body()
            else:
                return False, self.start_ctr
        else:
            return False, self.start_ctr

        print '</subroutineDec>'
        self.xml.append("</subroutineDec>")

    def compile_class_var_dec(self):
        """
        Grammar for this classVarDec :  ('static'|'field') type varName (',' varName)* ';'
        Implementation follows the grammar

        :return:
        """
        print "<classVarDec>"
        self.xml.append("<classVarDec>")

        if self.current_token_value in {'static', 'field'}:
            print self.current_token
            self.xml.append(self.current_token)
            self.increase_ctr()
        else:
            return False, self.start_ctr

        if type_(self.current_token):
            print self.current_token
            self.xml.append(self.current_token)
            self.increase_ctr()
        else:
            return False, self.start_ctr

        if var_name(self.current_token):
            print self.current_token
            self.xml.append(self.current_token)
            self.increase_ctr()
        else:
            return False, self.start_ctr

        while self.current_token_value != ';':
            if self.current_token_value == ',':
                print self.current_token
                self.xml.append(self.current_token)
                self.increase_ctr()

            else:
                return False, self.start_ctr
            if var_name(self.current_token):
                print self.current_token
                self.xml.append(self.current_token)
                self.increase_ctr()
            else:
                return "Not a valid varName"

        else:
            if self.current_token_value == ';':
                print self.current_token
                self.xml.append(self.current_token)
                self.increase_ctr()

        print "</classVarDec>"
        self.xml.append("</classVarDec>")
        return None

    def compile_class(self):

        if self.current_token_value != 'class':
            return False, "Not a class"
        else:
            print '<class>'
            self.xml.append('<class>')
            print self.current_token
            self.xml.append(self.current_token)
            self.increase_ctr()
            if not class_name(self.current_token):
                return False, self.start_ctr
            else:
                print self.current_token
                self.xml.append(self.current_token)
                self.increase_ctr()
                if self.current_token_value != '{':
                    return False, self.start_ctr
                else:
                    print self.current_token
                    self.xml.append(self.current_token)
                    self.increase_ctr()
                    if self.current_token_value == '}':
                        print self.current_token
                        self.xml.append(self.current_token)
                    else:
                        while self.current_token_value in {'static', 'field'}:
                            self.compile_class_var_dec()

                        while self.current_token_value in {'constructor', 'function', 'method'}:
                            self.compile_subroutine_dec()
            print '</class>'
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
with open('./ExpressionLessSquare/MainTT.xml', 'r') as exam:
    com_lis = exam.read().splitlines()

# pprint(com_lis)
d = compilationEngine(com_lis)
print d.compile_class()
with open('./ExpressionLessSquare/main_exam.xml', 'w') as ex:
    for i in d.xml:
        ex.write(i + '\n')
print d.xml
