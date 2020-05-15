# def op(xml_command):
#     print xml_command.split()[1]
#     tokens = xml_command.split()
#     if tokens[0] == '<symbol>' and tokens[1] in {'-', '+', '*', '/', '&', '&gt;',
#                                                  '|', '<', '>', '=', '&lt;', '&amp;'}:
#         return tokens[1]
#     return False
#
#
# def var_name(xml_command):
#     tokens = xml_command.split()
#     if tokens[0] == '<identifier>':
#         return tokens[1]
#     return False
#
#
# def class_name(xml_command):
#     tokens = xml_command.split()
#     if tokens[0] == '<identifier>':
#         return tokens[1]
#     return False
#
#
# def subroutine_name(xml_command):
#     tokens = xml_command.split()
#     if tokens[0] == '<identifier>':
#         return tokens[1]
#     return False
#
#
# def keyword_constant(xml_command):
#     tokens = xml_command.split()
#     if tokens[0] == '<keyword>' and tokens[1] in {'true', 'false', 'null', 'this'}:
#         return tokens[1]
#     return False
#
#
# def string_constant(xml_command):
#     tokens = xml_command.split()
#     if tokens[0] == '<stringConstant>':
#         return tokens[1]
#     return False
#
#
# def integer_constant(xml_command):
#     tokens = xml_command.split()
#     if tokens[0] == '<integerConstant>':
#         return tokens[1]
#     return False
#
#
# def unary_op(xml_command):
#     tokens = xml_command.split()
#     if tokens[0] == '<symbol>' and tokens[1] in {'-', '~'}:
#         return tokens[1]
#     return False
#
#
# def op(xml_command):
#     tokens = xml_command.split()
#     if tokens[0] == '<symbol>' and tokens[1] in {'-', '+', '*', '/', '&', '&gt;',
#                                                  '|', '<', '>', '=', '&lt;', '&amp;'}:
#         if tokens[1] in {'&gt;': '>', '&lt;': '<', '&amp;': '&'}:
#             return {'&gt;': '>', '&lt;': '<', '&amp;': '&'}[tokens[1]]
#         return tokens[1]
#
#     return False
#
#
# def type_(xml_command):
#     tokens = xml_command.split()
#     classname = class_name(xml_command)
#     if tokens[0] == '<keyword>' and tokens[1] in ['int', 'char', 'boolean']:
#         return tokens[1]
#     elif classname:
#         return classname
#     return False
#
#
# class compilationEngine(object):
#
#     def __init__(self, tokenised_list):
#         self.tokenised_list = tokenised_list
#         self.start_ctr = 0
#         self.current_token = self.tokenised_list[self.start_ctr]
#         self.next_token = self.tokenised_list[self.start_ctr + 1]
#         self.current_token_value = self.current_token.split()[1]
#         self.current_token_tag = self.current_token.split()[0]
#         self.next_token_value = self.next_token.split()[1]
#         self.next_token_tag = self.next_token.split()[0]
#         self.xml = []
#         self.class_table_data = [None, None, None]
#         self.function_table_data = [None, None, None]
#         # self.symbol_table = Symbol_Table()
#         self.class_name = None
#         self.current_class_name = 'c1..'
#         self.current_function_name = 'f1..'
#
#     def increase_ctr(self, val=1):
#         self.start_ctr += val
#         self.current_token = self.tokenised_list[self.start_ctr]
#         self.current_token_value = self.current_token.split()[1]
#         self.current_token_tag = self.current_token.split()[0]
#         if self.start_ctr != len(self.tokenised_list) - 1:
#             self.next_token = self.tokenised_list[self.start_ctr + 1]
#             self.next_token_value = self.next_token.split()[1]
#             self.next_token_tag = self.next_token.split()[0]
#
#     def compile_statements(self):
#         """
#         Grammar : statement*
#         :return:
#         """
#
#         self.xml.append("<statements>")
#         # print self.current_token,'-----statements ---'
#         while self.current_token_value != '}':
#             if self.current_token_value == 'let':
#                 self.compile_let_statement()
#             elif self.current_token_value == 'if':
#                 self.compile_if_statement()
#             elif self.current_token_value == 'while':
#                 self.compile_while_statement()
#             elif self.current_token_value == 'do':
#                 self.compile_do_statement()
#             elif self.current_token_value == 'return':
#                 self.compile_return()
#             else:
#                 return False, self.start_ctr
#
#         self.xml.append("</statements>")
#
#     def compile_if_statement(self):
#         """
#         Grammar : 'if' '(' expression ')' '{' statements '}'
#                   ('else' '{' statements '}')?
#
#         :return:
#         """
#
#
#         # Unique lable for false statement
#         l1 = str(self.current_class_name) + str(self.current_function_name )+ str(self.start_ctr)
#         l2 = str(self.current_class_name) + str(self.current_function_name) + str(self.start_ctr) + '!~'
#
#         if self.current_token_value == 'if':
#
#             self.xml.append(self.current_token)
#             self.increase_ctr()
#             if self.current_token_value == '(':
#
#                 self.xml.append(self.current_token)
#                 self.increase_ctr()
#                 self.compile_expression()
#                 if self.current_token_value == ')':
#
#                     self.xml.append(self.current_token)
#                     self.increase_ctr()
#                     if self.current_token_value == '{':
#                         print 'not'
#                         print 'if-goto %s' % l1
#
#                         self.xml.append(self.current_token)
#                         self.increase_ctr()
#                         self.compile_statements()
#                         print 'statements 2'
#                         if self.current_token_value == '}':
#
#                             self.xml.append(self.current_token)
#                             self.increase_ctr()
#                             print 'goto %s' % l2
#                             if self.current_token_value == 'else':
#
#                                 self.xml.append(self.current_token)
#                                 self.increase_ctr()
#
#                                 print 'label %s' % l1
#                                 if self.current_token_value == '{':
#                                     print 'statements 2'
#
#                                     self.xml.append(self.current_token)
#                                     self.increase_ctr()
#                                     self.compile_statements()
#                                     if self.current_token_value == '}':
#
#                                         self.xml.append(self.current_token)
#                                         self.increase_ctr()
#                                         print 'label %s' % l2
#                                     else:
#                                         return False, self.start_ctr
#                                 else:
#                                     return False, self.start_ctr
#                         else:
#                             print
#                     else:
#                         print
#                 else:
#                     print
#             else:
#                 print
#         else:
#             return False, self.start_ctr
#         self.xml.append("</ifStatement>")
#
#     def compile_expression_list(self):
#         """
#         Grammar : (expression (',' expression)* )?
#
#         :return:
#         """
#         # print '<expressionList>'
#         # self.xml.append("<expressionList>")
#         self.compile_expression()
#         while self.current_token_value == ',':
#             # print self.current_token
#             # self.xml.append(self.current_token)
#             self.increase_ctr()
#             self.compile_expression()
#         if self.current_token_value == ')':
#             self.increase_ctr()
#         # print '</expressionList>'
#         # self.xml.append("</expressionList>")
#
#     def compile_subroutine_call(self):
#         """
#         Grammar : subroutineName '(' expressionList ')' | (className |
#                   varName) '.' subroutineName '(' expressionList ')'
#
#         :return:
#         """
#         current_call = self.current_token_value
#
#         if var_name(self.current_token):
#             if self.next_token_value == '(':
#                 self.increase_ctr(2)
#                 self.xml.append(self.current_token)
#                 if self.next_token_value != ')':
#                     self.compile_expression_list()
#                     print current_call
#                 else:
#                     print '<expressionList>'
#                     print '</expressionList>'
#                     self.xml.append('<expressionList>')
#                     self.xml.append('</expressionList>')
#                     self.increase_ctr()
#                     print self.current_token
#                     self.xml.append(self.current_token)
#                     self.increase_ctr()
#
#             elif self.next_token_value == '.':
#                 print self.current_token
#                 self.xml.append(self.current_token)
#                 self.increase_ctr()
#                 if self.current_token_value == '.':
#                     print self.current_token
#                     self.xml.append(self.current_token)
#
#                 self.increase_ctr()
#                 # print self.current_token, '--5'
#                 if subroutine_name(self.current_token):
#                     print self.current_token
#                     self.xml.append(self.current_token)
#                     self.increase_ctr()
#                     # print self.current_token, '--5'
#                     if self.current_token_value == '(':
#                         print self.current_token
#                         self.xml.append(self.current_token)
#
#                         # print self.current_token, '--7'
#                         if self.next_token_value == ')':
#                             print '<expressionList>'
#                             print '</expressionList>'
#                             self.xml.append('<expressionList>')
#                             self.xml.append('</expressionList>')
#
#                             self.increase_ctr()
#                             print self.current_token
#                             self.xml.append(self.current_token)
#                             self.increase_ctr()
#                         else:
#                             self.increase_ctr()
#                             self.compile_expression_list()
#                             print self.current_token
#                             self.xml.append(self.current_token)
#                             self.increase_ctr()
#
#                         # else:
#                         #     return False, self.start_ctr
#                     else:
#                         return False, self.start_ctr
#                 else:
#                     return False, self.start_ctr
#
#     def compile_term(self):
#         """
#         Grammar : integerConstant | stringConstant | keywordConstant |
#                 varName | varName '[' expression ']' | subroutineCall |
#                 '(' expression ')' | unaryOp term
#
#         :return:
#         """
#         # print '<term>'
#         self.xml.append("<term>")
#         # print self.current_token
#         if var_name(self.current_token):
#             if self.next_token_value == '[':
#
#                 self.xml.append(self.current_token)
#                 self.increase_ctr()
#
#                 self.xml.append(self.current_token)
#                 self.increase_ctr()
#                 self.compile_expression()
#                 if self.current_token_value == ']':
#
#                     self.xml.append(self.current_token)
#                     self.increase_ctr()
#                 else:
#                     return False, self.start_ctr
#
#             elif self.next_token_value == '(':
#                 self.compile_subroutine_call()
#
#             elif self.next_token_value == '.':
#                 self.compile_subroutine_call()
#
#             else:
#                 print 'push %s' % self.current_token_value
#                 self.xml.append(self.current_token)
#                 self.increase_ctr()
#                 # print self.current_token,'---inside compile else-------'
#         elif unary_op(self.current_token):
#             # print self.current_token,self.next_token, '+++++=========++++++='
#             # if integer_constant(self.next_token):
#             print "push %s" % self.next_token_value
#             print 'push %s' % self.current_token_value
#             self.increase_ctr()
#             self.xml.append(self.current_token)
#             self.increase_ctr()
#             self.compile_term()
#
#             # self.increase_ctr()
#
#         elif self.current_token_value == '(':
#
#             self.xml.append(self.current_token)
#             self.increase_ctr()
#             self.compile_expression()
#             if self.current_token_value == ')':
#                 self.xml.append(self.current_token)
#                 self.increase_ctr()
#             else:
#                 return False, self.start_ctr
#         else:
#             # print self.current_token, '+++++=========++++++='
#             if string_constant(self.current_token):
#                 print "push %s" % self.current_token_value
#                 self.xml.append(self.current_token)
#                 self.increase_ctr()
#             elif integer_constant(self.current_token):
#                 print "push %s" % self.current_token_value
#                 self.xml.append(self.current_token)
#                 self.increase_ctr()
#             elif keyword_constant(self.current_token):
#                 print "push %s" % self.current_token_value
#                 self.xml.append(self.current_token)
#                 self.increase_ctr()
#             else:
#                 return False
#         self.xml.append("</term>")
#
#     def compile_expression(self):
#         """
#
#         term (op term)*
#         :return:
#         """
#         # print '<expression>'
#         self.xml.append("<expression>")
#
#         self.compile_term()
#         # print self.current_token, '---4'
#         while op(self.current_token):
#             current_op = op(self.current_token)
#             self.xml.append(self.current_token)
#             self.increase_ctr()
#             self.compile_term()
#             print current_op
#
#         # self.increase_ctr()
#         # print self.current_token,'---4'
#
#         # print '</expression>'
#         self.xml.append("</expression>")
#
#
# from pprint import pprint
#
# with open('./testTT.xml', 'r') as exam:
#     com_lis = exam.read().splitlines()
#
# # pprint(com_lis)
# d = compilationEngine(com_lis)
# print d.compile_if_statement()
# with open('./out.xml', 'w') as ex:
#     for i in d.xml:
#         ex.write(i + '\n')
# # print d.xml
# # pprint(d.symbol_table.class_table)
# # pprint(d.symbol_table.function_table)
























